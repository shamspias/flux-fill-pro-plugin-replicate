from typing import Any
from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class FluxFillProToolProvider(ToolProvider):
    """
    FLUX Fill Pro image editing tool provider.
    """

    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        """
        Validate the credentials by attempting to initialize the Replicate client.
        """
        try:
            import replicate

            api_token = credentials.get("api_token", "")
            if not api_token:
                raise ToolProviderCredentialValidationError("API token is required.")

            # Test the API token by initializing the client
            client = replicate.Client(api_token=api_token)

            # Try to get account info to validate the token
            try:
                # This will raise an error if the API token is invalid
                client.models.get("black-forest-labs/flux-fill-pro")
            except Exception as e:
                error_msg = str(e).lower()
                if "unauthorized" in error_msg or "authentication" in error_msg or "invalid" in error_msg:
                    raise ToolProviderCredentialValidationError(f"Invalid API token: {str(e)}")
                # If it's a different error (like network), still consider token valid
                # since we can't definitively say it's invalid

        except ImportError:
            raise ToolProviderCredentialValidationError("Replicate SDK is not installed.")
        except ToolProviderCredentialValidationError:
            raise
        except Exception as e:
            raise ToolProviderCredentialValidationError(f"Credential validation failed: {str(e)}")
