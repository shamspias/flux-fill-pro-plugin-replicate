# FLUX Fill Pro Plugin for Dify

![Version](https://img.shields.io/badge/version-0.0.1-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Platform](https://img.shields.io/badge/platform-Dify-purple.svg)

**Professional image inpainting and outpainting powered by FLUX Fill Pro**

[English](#english) • [বাংলা](#বাংলা) • [Русский](#русский) • [中文](#中文) • [日本語](#日本語) • [Português](#português)

---

## English

### Overview

FLUX Fill Pro Plugin brings state-of-the-art image editing capabilities to Dify. Edit or extend images with natural, seamless results using Black Forest Labs' professional inpainting and outpainting model.

### Features

- 🎨 **Professional Quality** - State-of-the-art inpainting and outpainting
- 🖼️ **Seamless Results** - Natural blending that preserves lighting and perspective
- ✂️ **Inpainting** - Remove or replace objects in images
- 📐 **Outpainting** - Extend images in any direction
- 🎯 **Full Control** - Adjust steps, guidance, and safety filters
- 🌍 **Multi-language Support** - 6 languages supported

### Quick Start

#### 1. Get API Token

Visit [Replicate](https://replicate.com/account/api-tokens) and create your API token.

#### 2. Install Plugin

1. Go to **Tools** → **Plugin Management** in Dify
2. Search for **"FLUX Fill Pro"**
3. Click **Install**

#### 3. Configure

1. Navigate to **Tools** → **FLUX Fill Pro** → **Authorize**
2. Enter your Replicate API token
3. Click **Save**

### Usage

Add the tool to your workflow or agent and start editing images!

**Use Cases:**
- Remove unwanted objects from photos
- Replace parts of an image
- Extend image borders naturally
- Fill in missing parts of images
- Creative image modifications

### Parameters

#### Required:
- **Image URL**: URL of the image to edit
- **Prompt**: Description of what to add or change

#### Optional:
- **Mask URL**: Mask image for inpainting (white=edit, black=preserve)
- **Steps**: 4-50 (default: 50) - More steps = better quality
- **Guidance**: 0-100 (default: 60) - How closely to follow prompt
- **Outpaint**: None/Left/Right/Top/Bottom/All - Direction to extend image
- **Output Format**: PNG/JPG/WebP
- **Safety Tolerance**: 0-6 (default: 2)
- **Prompt Upsampling**: Enhance prompt automatically

### Examples

#### Inpainting (Remove/Replace Objects):
1. Provide image URL
2. Provide mask URL (white areas will be edited)
3. Describe what you want instead
4. Adjust steps and guidance as needed

#### Outpainting (Extend Image):
1. Provide image URL
2. Set outpaint direction (Left/Right/Top/Bottom/All)
3. Describe what should be in the extended area
4. No mask needed!

### Pricing

FLUX Fill Pro costs **$0.05 per output image** on Replicate.

### Support

- **Documentation**: [Replicate FLUX Fill Pro](https://replicate.com/black-forest-labs/flux-fill-pro)
- **Issues**: Create an issue in the repository

---

## বাংলা

### সংক্ষিপ্ত বিবরণ

FLUX Fill Pro Plugin Dify-তে অত্যাধুনিক ইমেজ এডিটিং ক্ষমতা নিয়ে আসে। Black Forest Labs-এর পেশাদার ইনপেইন্টিং এবং আউটপেইন্টিং মডেল ব্যবহার করে স্বাভাবিক, নিরবচ্ছিন্ন ফলাফল সহ ইমেজ সম্পাদনা বা প্রসারিত করুন।

### বৈশিষ্ট্য

- 🎨 **পেশাদার মান** - অত্যাধুনিক ইনপেইন্টিং এবং আউটপেইন্টিং
- 🖼️ **নিরবচ্ছিন্ন ফলাফল** - প্রাকৃতিক মিশ্রণ যা আলো এবং দৃষ্টিভঙ্গি সংরক্ষণ করে
- ✂️ **ইনপেইন্টিং** - ইমেজে অবজেক্ট সরান বা প্রতিস্থাপন করুন
- 📐 **আউটপেইন্টিং** - যেকোনো দিকে ইমেজ প্রসারিত করুন

### দ্রুত শুরু

1. [Replicate](https://replicate.com/account/api-tokens) থেকে API টোকেন নিন
2. Dify-তে প্লাগইন ইনস্টল করুন
3. API টোকেন দিয়ে কনফিগার করুন

---

## Русский

### Обзор

FLUX Fill Pro Plugin приносит передовые возможности редактирования изображений в Dify. Редактируйте или расширяйте изображения с естественными результатами, используя профессиональную модель заполнения и расширения от Black Forest Labs.

### Возможности

- 🎨 **Профессиональное качество** - Передовое заполнение и расширение
- 🖼️ **Бесшовные результаты** - Естественное смешивание с сохранением освещения
- ✂️ **Заполнение** - Удаление или замена объектов на изображениях
- 📐 **Расширение** - Расширение изображений в любом направлении

### Быстрый старт

1. Получите API токен на [Replicate](https://replicate.com/account/api-tokens)
2. Установите плагин в Dify
3. Настройте с помощью API токена

---

## 中文

### 概述

FLUX Fill Pro 插件为 Dify 带来最先进的图像编辑功能。使用 Black Forest Labs 的专业修复和扩展模型，以自然、无缝的效果编辑或扩展图像。

### 功能特点

- 🎨 **专业品质** - 最先进的修复和扩展
- 🖼️ **无缝效果** - 保持照明和透视的自然融合
- ✂️ **图像修复** - 移除或替换图像中的对象
- 📐 **图像扩展** - 向任意方向扩展图像

### 快速开始

1. 在 [Replicate](https://replicate.com/account/api-tokens) 获取 API 令牌
2. 在 Dify 中安装插件
3. 使用 API 令牌配置

---

## 日本語

### 概要

FLUX Fill Pro PluginはDifyに最先端の画像編集機能をもたらします。Black Forest Labsのプロフェッショナルなインペインティングとアウトペインティングモデルを使用して、自然でシームレスな結果で画像を編集または拡張します。

### 機能

- 🎨 **プロフェッショナル品質** - 最先端のインペインティングとアウトペインティング
- 🖼️ **シームレスな結果** - 照明と視点を保持する自然な融合
- ✂️ **インペインティング** - 画像内のオブジェクトを削除または置換
- 📐 **アウトペインティング** - 任意の方向に画像を拡張

### クイックスタート

1. [Replicate](https://replicate.com/account/api-tokens)でAPIトークンを取得
2. Difyでプラグインをインストール
3. APIトークンで設定

---

## Português

### Visão Geral

O FLUX Fill Pro Plugin traz recursos de edição de imagem de ponta para o Dify. Edite ou estenda imagens com resultados naturais e perfeitos usando o modelo profissional de inpainting e outpainting da Black Forest Labs.

### Recursos

- 🎨 **Qualidade Profissional** - Inpainting e outpainting de última geração
- 🖼️ **Resultados Perfeitos** - Mesclagem natural que preserva iluminação e perspectiva
- ✂️ **Inpainting** - Remova ou substitua objetos em imagens
- 📐 **Outpainting** - Estenda imagens em qualquer direção

### Início Rápido

1. Obtenha o token API no [Replicate](https://replicate.com/account/api-tokens)
2. Instale o plugin no Dify
3. Configure com o token API

---

## Technical Details

### Installation

```bash
# Clone repository
git clone https://github.com/shamspias/flux-fill-pro-plugin-replicate
cd flux-fill-pro-plugin-replicate

# Install dependencies
pip install -r requirements.txt

# Package plugin
dify plugin package .
```

### Configuration

The plugin requires:
- Replicate API token
- Python 3.12
- dify_plugin==0.5.0
- replicate>=0.25.0
- pillow>=12.0.0

### Privacy & Security

See [PRIVACY.md](PRIVACY.md) for detailed privacy policy.

Key points:
- No data collection beyond API requests
- Images not stored permanently
- API tokens encrypted
- Secure HTTPS communication

## License

MIT License - See [LICENSE](LICENSE) file for details.

## Credits

- **Black Forest Labs** - For FLUX Fill Pro model
- **Replicate** - For API infrastructure
- **Dify Team** - For the AI platform

## Troubleshooting

### Common Issues

**Issue**: "API token is required"
- **Solution**: Make sure you've entered your Replicate API token in the plugin settings

**Issue**: "Invalid API token"
- **Solution**: Check that your token is correct and active on Replicate

**Issue**: "Mask error"
- **Solution**: Ensure mask image URL is valid and accessible. Mask should be the same size as the input image.

**Issue**: Image generation fails
- **Solution**: Check that all URLs are publicly accessible and image formats are supported

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.