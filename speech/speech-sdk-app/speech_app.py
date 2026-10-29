"""
BrezyWeather Voice Interface - STT for spoken weather queries, TTS for weather alerts.
Demonstrates: SpeechRecognizer, SpeechSynthesizer, continuous recognition, HD neural voice.

See README.md for sample output.
"""
import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

load_dotenv()

SPEECH_KEY = os.getenv("FOUNDRY_KEY")
SPEECH_ENDPOINT = os.getenv("SPEECH_ENDPOINT")
print(f"Using Azure Speech endpoint: {SPEECH_ENDPOINT}\n")


def listen_for_weather_query(config):
    """Recognize spoken weather query using Speech-to-Text."""
    recognizer = speechsdk.SpeechRecognizer(
        speech_config=config,
        audio_config=speechsdk.audio.AudioConfig(use_default_microphone=True)
    )
    print("BrezyWeather is listening... ask your weather question.")
    
    # Get speech recognition result
    result = recognizer.recognize_once_async().get()
    
    # Process recognition result
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print(f"  Recognized: \"{result.text}\"")
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("  No speech detected.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        details = speechsdk.CancellationDetails.from_result(result)
        print(f"  Recognition canceled: {details.reason} — {details.error_details}")
    
    return ""


def announce_weather_alert(config, alert_text):
    """Announce weather alert using Text-to-Speech."""
    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=config,
        audio_config=speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    )
    print(f"\n  Announcing alert: \"{alert_text[:80]}...\"")
    
    # Get synthesis result
    result = synthesizer.speak_text_async(alert_text).get()
    
    # Check synthesis status
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("  Alert announced successfully.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        details = speechsdk.CancellationDetails.from_result(result)
        print(f"  Synthesis canceled: {details.reason} — {details.error_details}")


if __name__ == "__main__":
    # Configure speech settings
    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY,
        endpoint=SPEECH_ENDPOINT
    )
    speech_config.speech_recognition_language = "en-US"
    speech_config.speech_synthesis_voice_name = "en-US-Ava:DragonHDLatestNeural"

    print("=== BrezyWeather Voice Interface ===\n")

    # Speech-to-text: Listen for a spoken weather query
    query = listen_for_weather_query(speech_config)

    # Text-to-speech: Announce a sample weather alert response
    # (In a real app you would pass the query to a model and speak its response)
    alert = (
        "BrezyWeather alert: A severe thunderstorm watch is in effect for your area until 8 PM tonight. "
        "Expect heavy rain and sustained winds up to 50 miles per hour. "
        "Avoid outdoor activities and seek shelter indoors."
    )
    announce_weather_alert(speech_config, alert)
