# BrezyWeather Information Extractor (Azure Content Understanding)

Extracts structured invoice data from a sample BrezyWeather-style business document using **Azure Content Understanding** (Foundry Tool).

## What it demonstrates

| Demo | Analyzer | Input | Extracted output |
|---|---|---|---|
| Document | `prebuilt-invoice` | PDF URL | Raw extracted invoice fields dictionary |

> This demo uses the official Content Understanding prebuilt analyzer `prebuilt-invoice`. Content Understanding also supports other modalities more broadly, but this sample app focuses only on invoice extraction.

## Prerequisites

```bash
pip install azure-ai-contentunderstanding python-dotenv
```

Uses API version `2025-05-01-preview`.

## Set up Content Understanding

1. Foundry project → **Foundry Tools** → **Content Understanding**  
   (or https://contentunderstanding.ai.azure.com)
2. Create or select a Foundry resource
3. Copy the **Endpoint** and **Key**

## Environment variables

The script loads variables from `../../.env`.

```env
CONTENT_UNDERSTANDING_ENDPOINT=https://<your-foundry-resource>.services.ai.azure.com/
FOUNDRY_KEY=<your-key>
```

## Run

```bash
python extraction_app.py
```

The app always runs a single demo: invoice extraction using the hardcoded sample PDF:

`https://github.com/Azure-Samples/azure-ai-content-understanding-python/raw/refs/heads/main/data/invoice.pdf`

## Sample output

```text
Using Content Understanding endpoint: https://<your-foundry-resource>.services.ai.azure.com/

=== Document Extraction (prebuilt-invoice) ===
Source: https://github.com/Azure-Samples/azure-ai-content-understanding-python/raw/refs/heads/main/data/invoice.pdf

Extracted content: {'invoice_number': '1234567890', 'invoice_date': '2026-01-01', 'invoice_amount': '100.00', 'invoice_currency': 'USD'}
```

## Exam connections

- **Confidence scores**: Content Understanding responses include confidence information that can help decide whether to automate processing or route to human review
- **Grounding**: extraction services can identify where a value came from in the source content
- Content Understanding supports **documents, images, audio, and video** as a platform capability, even though this demo uses only a document
- Content Understanding and **Azure AI Document Intelligence** overlap in extraction scenarios, but Content Understanding emphasizes richer multimodal analysis through Foundry
- OCR extracts raw text; Content Understanding extracts **structured fields** from content
