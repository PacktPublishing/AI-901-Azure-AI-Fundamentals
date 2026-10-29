"""
BrezyWeather Feedback Analyzer - Analyze user reviews with Azure AI Language (detection, PII, sentiment, phrases).
Demonstrates: language detection, PII redaction, sentiment analysis, key phrase extraction.

See README.md for sample output.
"""

import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv("../../.env")

LANGUAGE_ENDPOINT = os.getenv("LANGUAGE_ENDPOINT")
LANGUAGE_KEY = os.getenv("FOUNDRY_KEY")

print(f"Using Azure Language endpoint: {LANGUAGE_ENDPOINT}\n")

REVIEWS = [
    "The hourly forecast is incredibly accurate! Saved me from getting caught in a thunderstorm last Tuesday.",
    "The wind speed alerts keep triggering when it's perfectly calm outside. Very frustrating and unreliable.",
    "Nice app overall, but the radar map takes too long to load on slower connections.",
    "La aplicación es muy intuitiva y los mapas de lluvia son excelentes.",
    "Die Wettervorhersage ist präzise, aber die Benutzeroberfläche könnte moderner sein.",
]

SUPPORT_MESSAGES = [
    "Hi, this is Maria Garcia. Call me back or email maria@brezyweather.com about my premium subscription.",
]

client = TextAnalyticsClient(endpoint=LANGUAGE_ENDPOINT, credential=AzureKeyCredential(LANGUAGE_KEY))


def detect_languages(texts):
    print("\n=== Language Detection ===")
    
    # Get results from API
    results = client.detect_language(documents=texts)
    
    # Process each result
    for text, result in zip(texts, results):
        if not result.is_error:
            lang_name = result.primary_language.name
            lang_code = result.primary_language.iso6391_name
            confidence = result.primary_language.confidence_score
            print(f"Language: {lang_name} (Code: {lang_code}, Confidence: {confidence:.2f})")
            print(f"Text: {text}\n")
       
    print()


def analyze_sentiment(texts):
    print("\n=== Sentiment Analysis ===")
    sentiment_icon = {"positive": "✅", "neutral": "➡️", "negative": "❌"}
    
    # Get results from API
    results = client.analyze_sentiment(documents=texts)
    
    # Process each result
    for text, result in zip(texts, results):
        if not result.is_error:
            print(f"Sentiment: {result.sentiment.capitalize()}")
            print(f"  Positive: {result.confidence_scores.positive:.2f}")
            print(f"  Neutral : {result.confidence_scores.neutral:.2f}")
            print(f"  Negative: {result.confidence_scores.negative:.2f}")
            print(f"  Text: \"{text}\"\n")
       
    print()


def extract_key_phrases(texts):
    print("\n=== Key Phrase Extraction ===")
    
    # Get results from API
    results = client.extract_key_phrases(documents=texts)
    
    # Process each result
    for text, result in zip(texts, results):
        if not result.is_error and result.key_phrases:
            print("  Key phrases:", result.key_phrases)
            print("  Text:", text)
           
    print()


def detect_pii(texts):
    print("\n=== PII Detection & Redaction ===")
    
    # Get results from API
    results = client.recognize_pii_entities(documents=texts)
    
    # Process each result
    for text, result in zip(texts, results):
        if not result.is_error and result.entities:
            print(f"  Redacted: {result.redacted_text[:80]}")
            for entity in result.entities:
                print(f"    - {entity.text} | category={entity.category} | confidence={entity.confidence_score:.2f}")
            print()
    
    print()


if __name__ == "__main__":
    input("Press Enter to continue to language detection...")
    detect_languages(REVIEWS)

    input("Press Enter to continue to sentiment analysis...")
    analyze_sentiment(REVIEWS)
    
    input("Press Enter to continue to key phrase extraction...")
    extract_key_phrases(REVIEWS)
    
    input("Press Enter to continue to PII detection...")
    detect_pii(SUPPORT_MESSAGES)
