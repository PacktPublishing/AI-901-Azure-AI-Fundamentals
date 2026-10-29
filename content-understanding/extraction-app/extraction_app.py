"""
BrezyWeather Information Extractor - Extract structured data from documents using Azure Content Understanding.
Demonstrates: prebuilt analyzers for invoice extraction.

See README.md for sample output.
"""

import os
from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv("../../.env")

ENDPOINT = os.getenv("CONTENT_UNDERSTANDING_ENDPOINT")
FOUNDRY_KEY = os.getenv("FOUNDRY_KEY")
API_VERSION = "2025-11-01"
SAMPLE_INVOICE_URL = "https://github.com/Azure-Samples/azure-ai-content-understanding-python/raw/refs/heads/main/data/invoice.pdf"

print(f"Using Content Understanding endpoint: {ENDPOINT}")

client = ContentUnderstandingClient(endpoint=ENDPOINT, credential=AzureKeyCredential(FOUNDRY_KEY), api_version=API_VERSION)


def extract_from_invoice():
    print("\n=== Document Extraction (prebuilt-invoice) ===")
    print(f"Source: {SAMPLE_INVOICE_URL}\n")
    
    # Get results from API
    poller = client.begin_analyze(analyzer_id="prebuilt-invoice", inputs=[{"url": SAMPLE_INVOICE_URL}])
    results = poller.result().contents
    
    # Process each result
    for content in results:
        print(f"Extracted content: {content.fields}")
    
    print()


if __name__ == "__main__":
    extract_from_invoice()
