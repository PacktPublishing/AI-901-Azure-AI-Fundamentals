# BrezyWeather Image Generator (GPT-Image via Foundry)

Generates a BrezyWeather-style visual using a **GPT-Image deployment** in Microsoft Foundry. In this simplified demo, the app sends one fixed prompt for a polished weather-app narrative scene: a developer building an AI agent with Microsoft Foundry.

## What it demonstrates

| Concept | Details |
|---|---|
| OpenAI client with Entra auth | `OpenAI(...)` authenticated with `DefaultAzureCredential` + `get_bearer_token_provider(...)` |
| Classic Images API | `client.images.generate(model=..., prompt=..., n=1, size="1024x1024")` |
| Base64 output decoding | Decodes `img.data[0].b64_json` and writes the image to disk |

## Prerequisites

```bash
pip install openai azure-identity python-dotenv
```

Before running the sample, make sure `DefaultAzureCredential` can obtain a token in your environment, for example by signing in with the Azure CLI.

## Deploy a GPT-Image model in Foundry

1. Foundry project → **Model catalog** → search for `gpt-image-1` (or a compatible GPT-Image deployment)
2. Click **Deploy** → name it (for example, `gpt-image-1-mini`)
3. Copy the OpenAI-compatible endpoint for your Azure AI Foundry resource

## Environment variables

The script loads variables from `../../.env`.

```env
OPENAI_ENDPOINT=https://<your-foundry-resource>.openai.azure.com/openai/v1/
IMAGE_MODEL=gpt-image-1-mini
```

- `OPENAI_ENDPOINT`: the base URL passed to the OpenAI client
- `IMAGE_MODEL`: your deployed image model name; defaults to `gpt-image-1-mini` if not set

## Run

```bash
python image_generation_app.py
```

What happens when you run it:

- The app prints `Using endpoint: ...` and `Using deployment: ...`
- It shows `=== Image Generation ===`
- It uses this fixed prompt: `Generate a professional image of a developer building an AI agent using Microsoft Foundry, photorealistic style`
- It pauses with `Press Enter to continue to generate image...`
- It generates one `1024x1024` image and saves it as `output.png`
- It prints `Image saved to: output.png`

## Sample output

```text
Using endpoint: https://brezyweather-bvp.cognitiveservices.azure.com/
Using deployment: gpt-image-1.5

=== Image Generation ===

Generating: "Generate a professional image of a developer building an AI agent using Microsoft Foundry, photorealistic style"

Press Enter to continue to generate image...

Image saved to: output.png
```

## Exam connection

- This demo shows **image generation** with a deployed **GPT-Image** model in Azure AI Foundry
- It uses Microsoft Entra ID authentication through `DefaultAzureCredential`, a common Azure SDK pattern
- The generated image payload is returned as **base64** and then decoded before saving locally
- The sample uses the classic OpenAI Images API via `client.images.generate(...)`, which is the exact pattern implemented in the code
