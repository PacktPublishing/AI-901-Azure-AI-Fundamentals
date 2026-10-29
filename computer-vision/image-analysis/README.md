# BrezyWeather Image Analyzer (Responses API multimodal)

Analyzes images with a **multimodal foundation model** in Microsoft Foundry. This demo sends both **text + image** to the **Responses API** and shows two input patterns: a remote image URL and a local image encoded as base64.

## What it demonstrates

| Concept | Details |
|---|---|
| Responses API multimodal input | `client.responses.create()` with `input_text` + `input_image` content blocks |
| Image analysis via URL | Sends a public image URL directly to the model for description and text visibility checks |
| Local image analysis via base64 encoding | Reads `tech-girl.jpg`, encodes it, and sends it as a `data:image/jpeg;base64,...` URL |

## Prerequisites

```bash
pip install openai azure-ai-projects azure-identity python-dotenv
```

Sign in for local development:

```bash
az login
```

## Set up your Foundry project

1. Open your Microsoft Foundry project
2. Copy the project endpoint from **Overview**
3. Make sure you have a deployed multimodal model available (default used here: `gpt-5.4`)

## Environment variables

This script loads environment variables from `../../.env`.

```env
PROJECT_ENDPOINT=https://<your-foundry-resource>.services.ai.azure.com/api/projects/<your-project>
DEPLOYMENT_NAME=gpt-5.4
```

`DEPLOYMENT_NAME` is optional in this demo; if omitted, it defaults to `gpt-5.4`.

## Run

```bash
python image_analysis_app.py
```

Keep `tech-girl.jpg` in the same folder as the script so the local-image example can be loaded successfully.

The script runs two steps:

1. Analyze a remote image from a URL
2. Analyze a local JPEG after base64 encoding

## Sample output

```text
Press Enter to continue to analyze image via URL...

=== Analyze Image via URL ===
This image shows a person working at a standing desk in a bright office with large floor-to-ceiling windows overlooking a city.

### Main subject
- A woman is standing at the desk, viewed from the side.
- She is wearing:
  - **yellow/orange over-ear headphones**
  - **glasses**
  - a **red-and-black plaid shirt**
- She appears to be typing on a **laptop** and looking toward the screens.

### Desk and computer equipment
- A **white standing desk** is visible.
- On the desk there is:
  - a **laptop** open in front of her
  - **two external monitors**
  - some **cables/wires**
  - a small **device or dock** near the monitors
- The laptop screen and at least one of the monitors display what looks like **computer code** or terminal output on dark backgrounds.
- The left monitor clearly shows multiple columns/sections of text in code-like formatting.
- The right monitor appears darker and less readable.

### Room and background
- The office has **very large windows** wrapping around the corner.
- Outside the windows are many **tall city buildings**, suggesting a downtown urban setting.
- The room has **white walls** and a clean, modern appearance.
- There are **window shades/blinds** partially lowered at the top.

### Visible text
There is **no clearly readable text** in the image.
The screens contain lines of code or terminal text, but the text is too small and indistinct to read accurately.

### Objects visible
- woman/person
- yellow headphones
- glasses
- plaid shirt
- standing desk
- laptop
- two monitors
- monitor stand
- cables
- windows
- blinds/shades
- city buildings outside

If you want, I can also give:
1. a **short caption** for the image,
2. an **accessibility-style alt text** description, or
3. a **more detailed breakdown of the workstation setup**.

Press Enter to continue to analyze local image from base64...
=== Analyze Local Image from Base64 ===
The primary subject is **a person working at a computer workstation**, likely **coding or programming**, in an office with large city-view windows.
```

## Exam connection

- This demo shows **image analysis using a multimodal foundation model** through the **Responses API**
- That is different from the classic **Azure AI Vision** REST API / Image Analysis 4.0 SDK approach
- Use this pattern for **description, question answering, and OCR-style interpretation** of images in a model-first workflow
- By contrast, **DALL-E / GPT-Image** models are for **image generation**, not image understanding
