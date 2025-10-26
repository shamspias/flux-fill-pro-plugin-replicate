from typing import Any, Generator
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin import Tool
import requests
import base64


class FluxFillProTool(Tool):
    """
    FLUX Fill Pro inpainting and outpainting tool with automatic mask resizing.
    """

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        """
        Invoke the tool to edit images using FLUX Fill Pro.
        """
        try:
            import replicate
            from PIL import Image
            from io import BytesIO

            # Get API token from credentials
            api_token = self.runtime.credentials.get("api_token", "")
            if not api_token:
                yield self.create_text_message("API token is required.")
                return

            # Initialize Replicate client
            client = replicate.Client(api_token=api_token)

            # Get required parameters
            image = tool_parameters.get("image", "")
            prompt = tool_parameters.get("prompt", "")

            if not image:
                yield self.create_text_message("Image URL is required.")
                return

            if not prompt:
                yield self.create_text_message("Prompt is required.")
                return

            # Get optional parameters
            mask = tool_parameters.get("mask", "")
            steps = tool_parameters.get("steps", 50)
            guidance = tool_parameters.get("guidance", 60)
            outpaint = tool_parameters.get("outpaint", "None")
            output_format = tool_parameters.get("output_format", "png")
            safety_tolerance = tool_parameters.get("safety_tolerance", 2)
            prompt_upsampling = tool_parameters.get("prompt_upsampling", False)

            # Handle mask validation and auto-resizing if mask is provided and doing inpainting
            mask_to_use = mask
            if mask and outpaint == "None":
                try:
                    yield self.create_text_message("🔍 Checking mask and image dimensions...")

                    # Download and check both images
                    image_response = requests.get(image, timeout=30)
                    mask_response = requests.get(mask, timeout=30)

                    if image_response.status_code != 200:
                        yield self.create_text_message(
                            f"❌ Failed to download source image.\n"
                            f"Status code: {image_response.status_code}\n"
                            f"URL: {image}"
                        )
                        return

                    if mask_response.status_code != 200:
                        yield self.create_text_message(
                            f"❌ Failed to download mask image.\n"
                            f"Status code: {mask_response.status_code}\n"
                            f"URL: {mask}"
                        )
                        return

                    # Load images
                    source_img = Image.open(BytesIO(image_response.content))
                    mask_img = Image.open(BytesIO(mask_response.content))

                    source_size = source_img.size
                    mask_size = mask_img.size

                    if source_size != mask_size:
                        yield self.create_text_message(
                            f"⚠️ Dimension mismatch detected!\n"
                            f"   Source: {source_size[0]} × {source_size[1]} pixels\n"
                            f"   Mask: {mask_size[0]} × {mask_size[1]} pixels\n\n"
                            f"🔧 Auto-resizing mask to match source..."
                        )

                        # Resize mask to match source dimensions
                        # Use LANCZOS for high-quality resize that preserves edges
                        mask_resized = mask_img.resize(source_size, Image.Resampling.LANCZOS)

                        # Convert to RGB if needed (remove alpha channel)
                        if mask_resized.mode == 'RGBA':
                            # Create white background
                            background = Image.new('RGB', mask_resized.size, (255, 255, 255))
                            background.paste(mask_resized, mask=(mask_resized.split()[3]))
                            mask_resized = background
                        elif mask_resized.mode != 'RGB':
                            mask_resized = mask_resized.convert('RGB')

                        # Convert resized mask to base64 data URI
                        buffered = BytesIO()
                        mask_resized.save(buffered, format="PNG")
                        mask_base64 = base64.b64encode(buffered.getvalue()).decode()
                        mask_to_use = f"data:image/png;base64,{mask_base64}"

                        yield self.create_text_message(
                            f"✅ Mask auto-resized successfully!\n"
                            f"   New size: {source_size[0]} × {source_size[1]} pixels\n"
                            f"   Now matching source image perfectly!"
                        )
                    else:
                        yield self.create_text_message(
                            f"✓ Dimensions match perfectly!\n"
                            f"  Both images: {source_size[0]} × {source_size[1]} pixels"
                        )

                except ImportError:
                    yield self.create_text_message(
                        "⚠️ Warning: Cannot validate/resize - PIL not installed.\n"
                        "Install with: pip install Pillow\n"
                        "Proceeding with original mask..."
                    )
                except Exception as validation_error:
                    yield self.create_text_message(
                        f"⚠️ Warning: Could not validate/resize mask: {str(validation_error)}\n"
                        f"Proceeding with original mask..."
                    )

            # Prepare input parameters
            input_params = {
                "image": image,
                "prompt": prompt,
                "steps": steps,
                "guidance": guidance,
                "outpaint": outpaint,
                "output_format": output_format,
                "safety_tolerance": safety_tolerance,
                "prompt_upsampling": prompt_upsampling,
            }

            # Add mask (potentially resized) if provided
            if mask_to_use:
                input_params["mask"] = mask_to_use

            yield self.create_text_message("🎨 Generating image with FLUX Fill Pro...")

            # Run the model
            output = client.run(
                "black-forest-labs/flux-fill-pro",
                input=input_params
            )

            # Download and yield the image
            if output:
                # Handle different Replicate output formats
                try:
                    # Try as FileOutput with url() method
                    if hasattr(output, 'url') and callable(getattr(output, 'url', None)):
                        image_url = output.url()
                    # Try as FileOutput with url property
                    elif hasattr(output, 'url'):
                        image_url = output.url
                    # Try as direct string
                    else:
                        image_url = str(output)
                except Exception as url_error:
                    # Fallback to string conversion
                    image_url = str(output)

                # Download the image
                response = requests.get(image_url, timeout=60)
                if response.status_code == 200:
                    image_bytes = response.content

                    # Determine mime type based on format
                    mime_type = f"image/{output_format}"

                    # Create blob message for the image
                    yield self.create_blob_message(
                        blob=image_bytes,
                        meta={"mime_type": mime_type}
                    )

                    yield self.create_text_message("✅ Image generated successfully!")
                else:
                    yield self.create_text_message(
                        f"Failed to download generated image. Status code: {response.status_code}")
            else:
                yield self.create_text_message("No output received from FLUX Fill Pro.")

        except ImportError as ie:
            missing_module = str(ie).split("'")[1] if "'" in str(ie) else str(ie)
            if "PIL" in missing_module or "Pillow" in missing_module:
                yield self.create_text_message(
                    f"❌ Missing module: Pillow\n\n"
                    f"This is required for automatic mask resizing.\n"
                    f"Install with: pip install Pillow requests replicate"
                )
            elif "replicate" in missing_module:
                yield self.create_text_message(
                    f"❌ Missing module: replicate\n\n"
                    f"Install with: pip install replicate"
                )
            else:
                yield self.create_text_message(
                    f"❌ Missing required module: {missing_module}\n\n"
                    f"Install all dependencies with: pip install replicate Pillow requests"
                )
        except Exception as e:
            error_message = str(e)

            # Provide helpful error messages for common issues
            if "mask size" in error_message.lower() or "does not match" in error_message.lower():
                # This should rarely happen now with auto-resize
                yield self.create_text_message(
                    f"⚠️ MASK SIZE ERROR (Auto-resize failed)\n\n"
                    f"Error details: {error_message}\n\n"
                    f"💡 The plugin tried to auto-resize but encountered an issue.\n"
                    f"Please try:\n"
                    f"1. Manually resize mask using: https://www.iloveimg.com/resize-image\n"
                    f"2. Check that both URLs are publicly accessible\n"
                    f"3. Ensure both images are in standard formats (PNG/JPG)"
                )
            elif "mask" in error_message.lower():
                yield self.create_text_message(
                    f"❌ Mask Error: {error_message}\n\n"
                    f"💡 Checklist:\n"
                    f"✓ Is mask URL publicly accessible?\n"
                    f"✓ Is mask in a valid format (PNG/JPG)?\n"
                    f"✓ White = edit, Black = preserve\n\n"
                    f"💡 The plugin auto-resizes masks, so size shouldn't be an issue.\n"
                    f"For outpainting (extending image), set 'Outpaint' and skip the mask!"
                )
            elif "base64" in error_message.lower() or "data:" in error_message.lower():
                yield self.create_text_message(
                    f"❌ Image Encoding Error: {error_message}\n\n"
                    f"💡 The auto-resized mask couldn't be encoded properly.\n"
                    f"Please try:\n"
                    f"1. Providing mask URL that exactly matches source size\n"
                    f"2. Using a simpler mask (pure black/white, no transparency)\n"
                    f"3. Converting mask to PNG format before upload"
                )
            elif "image" in error_message.lower() and (
                    "not" in error_message.lower() or "invalid" in error_message.lower()):
                yield self.create_text_message(
                    f"❌ Image Error: {error_message}\n\n"
                    f"💡 Checklist:\n"
                    f"✓ Is image URL publicly accessible?\n"
                    f"✓ Does URL point directly to an image file?\n"
                    f"✓ Is format supported (JPG/PNG/WebP)?\n"
                    f"✓ Is file size reasonable (<20MB)?\n"
                    f"✓ Try opening URL in a browser to verify"
                )
            elif "unauthorized" in error_message.lower() or "authentication" in error_message.lower():
                yield self.create_text_message(
                    f"❌ Authentication Error: {error_message}\n\n"
                    f"💡 Solution:\n"
                    f"1. Check your Replicate API token is valid\n"
                    f"2. Get/refresh token at: https://replicate.com/account/api-tokens\n"
                    f"3. Re-enter token in Dify: Tools → FLUX Fill Pro → Authorize\n"
                    f"4. Make sure you have billing enabled on Replicate"
                )
            elif "rate limit" in error_message.lower() or "quota" in error_message.lower():
                yield self.create_text_message(
                    f"❌ Rate Limit Error: {error_message}\n\n"
                    f"💡 Solution:\n"
                    f"1. You've hit Replicate API rate limits\n"
                    f"2. Wait a few minutes and try again\n"
                    f"3. Check your usage at: https://replicate.com/account/billing\n"
                    f"4. Consider upgrading your Replicate plan"
                )
            else:
                yield self.create_text_message(
                    f"❌ Error: {error_message}\n\n"
                    f"💡 Common issues to check:\n"
                    f"1. All URLs are publicly accessible\n"
                    f"2. Images are in supported formats (JPG/PNG/WebP)\n"
                    f"3. Replicate API token is valid and has billing enabled\n"
                    f"4. Internet connection is stable\n"
                    f"5. Try with simpler images first\n\n"
                    f"💡 Note: Mask resizing is automatic - size shouldn't be an issue!\n\n"
                    f"Need help? Visit: https://replicate.com/black-forest-labs/flux-fill-pro"
                )
