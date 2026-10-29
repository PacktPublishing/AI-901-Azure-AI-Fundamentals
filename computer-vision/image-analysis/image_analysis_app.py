"""
BrezyWeather Image Analyzer - Analyze images with Azure AI Vision (describe, extract text, classify, generate).
Demonstrates: image , text extraction, image classification.

See README.md for sample output.
"""

import base64
import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv("../../.env")

PROJECT_ENDPOINT = os.getenv("PROJECT_ENDPOINT")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME", "gpt-5.4")

# Initialize project client and OpenAI client
project = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
)
client = project.get_openai_client()


def analyze_image_via_url(image_url):
    print("\n=== Analyze Image via URL ===")

    # Get response from API
    response = client.responses.create(
        model=DEPLOYMENT_NAME,
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "Describe this image in detail. What objects do you see? What text is visible?",
                    },
                    {
                        "type": "input_image",
                        "image_url": image_url,
                    },
                ],
            }
        ],
        temperature=0.7,
    )

    # Display result
    print(response.output_text)
    print()


def analyze_local_image_from_base64(image_path):
    print("=== Analyze Local Image from Base64 ===")

    # Encode local image
    with open(image_path, "rb") as image_file:
        local_image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

    # Get response from API
    response = client.responses.create(
        model=DEPLOYMENT_NAME,
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "What is the primary subject of this image?",
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{local_image_base64}",
                    },
                ],
            }
        ],
    )

    # Display result
    print(response.output_text)
    print()


if __name__ == "__main__":
    input("Press Enter to continue to analyze image via URL...")
    image_url = "https://images.pexels.com/photos/1181676/pexels-photo-1181676.jpeg"
    analyze_image_via_url(image_url)

    input("Press Enter to continue to analyze local image from base64...")
    image_path = "tech-girl.jpg"
    analyze_local_image_from_base64(image_path)