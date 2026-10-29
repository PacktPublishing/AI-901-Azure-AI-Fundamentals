# BrezyWeather Feedback Analyzer

Analyzes user reviews from the BrezyWeather app using **Azure AI Language** (Foundry Tool).

## What it demonstrates

| Capability | SDK method |
|---|---|
| Language detection | `client.detect_language()` |
| PII detection & redaction | `client.recognize_pii_entities()` |
| Sentiment analysis | `client.analyze_sentiment()` |
| Key phrase extraction | `client.extract_key_phrases()` |

The sample reviews include English, Spanish, and German to show multilingual support.

> **Two approaches in Foundry:** This demo uses the **Azure Language SDK** (`azure-ai-textanalytics`) for deterministic, structured output. You can also do text analysis with a **general-purpose model** via the OpenAI Responses API (`https://<resource>.openai.azure.com/openai/v1/`) when you want flexible, prompt-driven analysis. For agents, the **Azure Language MCP server** exposes these capabilities as a tool.

## Prerequisites

```bash
pip install azure-ai-textanalytics==5.4.0 python-dotenv
```

## Set up a Language resource

1. In your Foundry project → **Foundry Tools** → **Language**
2. Create or select an Azure AI Language resource
3. Copy the **Endpoint** and **Key** from the resource

Alternatively, access via Language Studio: https://language.cognitive.azure.com/

## Environment variables

```
LANGUAGE_ENDPOINT=https://<your-language-resource>.cognitiveservices.azure.com/
FOUNDRY_KEY=<your-language-key>
```

## Run

```bash
python text_analysis_app.py
```

## Sample output

```text
Using Azure Language endpoint: https://<your-language-resource>.cognitiveservices.azure.com/

Press Enter to continue to language detection...

=== Language Detection ===

Language: English (Code: en, Confidence: 1.00)
Text: The hourly forecast is incredibly accurate! Saved me from getting caught in a thunderstorm last Tuesday.

Language: English (Code: en, Confidence: 1.00)
Text: The wind speed alerts keep triggering when it's perfectly calm outside. Very frustrating and unreliable.

Language: English (Code: en, Confidence: 1.00)
Text: Nice app overall, but the radar map takes too long to load on slower connections.

Language: Spanish (Code: es, Confidence: 1.00)
Text: La aplicación es muy intuitiva y los mapas de lluvia son excelentes.

Language: German (Code: de, Confidence: 1.00)
Text: Die Wettervorhersage ist präzise, aber die Benutzeroberfläche könnte moderner sein.

Press Enter to continue to sentiment analysis...

=== Sentiment Analysis ===

Sentiment: Positive
    Positive: 0.91
    Neutral : 0.08
    Negative: 0.01
    Text: "The hourly forecast is incredibly accurate! Saved me from getting caught in a thunderstorm last Tuesday."

Sentiment: Negative
    Positive: 0.00
    Neutral : 0.00
    Negative: 1.00
    Text: "The wind speed alerts keep triggering when it's perfectly calm outside. Very frustrating and unreliable."

Sentiment: Negative
    Positive: 0.11
    Neutral : 0.01
    Negative: 0.89
    Text: "Nice app overall, but the radar map takes too long to load on slower connections."

Sentiment: Positive
    Positive: 0.99
    Neutral : 0.00
    Negative: 0.00
    Text: "La aplicación es muy intuitiva y los mapas de lluvia son excelentes."

Sentiment: Neutral
    Positive: 0.08
    Neutral : 0.91
    Negative: 0.00
    Text: "Die Wettervorhersage ist präzise, aber die Benutzeroberfläche könnte moderner sein."

Press Enter to continue to key phrase extraction...

=== Key Phrase Extraction ===

    Key phrases: ['hourly forecast', 'thunderstorm']
    Text: The hourly forecast is incredibly accurate! Saved me from getting caught in a thunderstorm last Tuesday.

    Key phrases: ['wind speed alerts']
    Text: The wind speed alerts keep triggering when it's perfectly calm outside. Very frustrating and unreliable.

    Key phrases: ['Nice app', 'radar map', 'slower connections']
    Text: Nice app overall, but the radar map takes too long to load on slower connections.

    Key phrases: ['aplicación', 'mapas', 'lluvia']
    Text: La aplicación es muy intuitiva y los mapas de lluvia son excelentes.

    Key phrases: ['Benutzeroberfläche', 'Wettervorhersage']
    Text: Die Wettervorhersage ist präzise, aber die Benutzeroberfläche könnte moderner sein.

Press Enter to continue to PII detection...

=== PII Detection & Redaction ===

    Redacted: Hi, this is ************. Call me back or email ********************** about my
    - Maria Garcia | category=Person | confidence=1.00
    - maria@brezyweather.com | category=Email | confidence=0.80
```
