"""
Image Generator - Generate images via GPT Image in Azure AI Foundry.
Demonstrates: OpenAI client, images.generate, base64 decoding, saving to disk.

See README.md for sample output.
"""

import os
import base64
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv

load_dotenv("../../.env")

OPENAI_ENDPOINT = os.getenv("OPENAI_ENDPOINT_VISION")
DEPLOYMENT_NAME = os.getenv("IMAGE_MODEL", "gpt-image-1-mini")

print(f"Using endpoint: {OPENAI_ENDPOINT}")
print(f"Using deployment: {DEPLOYMENT_NAME}")

def generate_image():
    print("\n=== Image Generation ===\n")
    prompt = "Generate a professional image of a developer building an AI agent using Microsoft Foundry, photorealistic style"
    print(f"Generating: \"{prompt}\"")
    
    input("\nPress Enter to continue to generate image...")

    # Initialize OpenAI client
    token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")
    client = OpenAI(
        base_url=OPENAI_ENDPOINT,
        api_key=token_provider,
    )

    # Generate image
    img = client.images.generate(
        model=DEPLOYMENT_NAME,
        prompt=prompt,
        n=1,
        size="1024x1024",
    )

    # Decode and save image
    image_bytes = base64.b64decode(img.data[0].b64_json)
    filename = "output.png"
    with open(filename, "wb") as f:
        f.write(image_bytes)
    
    print(f"Image saved to: {filename}\n")


if __name__ == "__main__":
    generate_image()
