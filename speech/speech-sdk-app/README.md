# BrezyWeather Voice Interface (Azure AI Speech SDK)

Voice-in / voice-out loop for the BrezyWeather app using the **Azure AI Speech SDK**.

## What it demonstrates


| Capability                     | SDK class                                       |
| ------------------------------ | ----------------------------------------------- |
| Speech-to-text (single phrase) | `SpeechRecognizer.recognize_once_async()`       |
| Text-to-speech                 | `SpeechSynthesizer` — text → speaker            |
| HD neural voice                | `en-US-Ava:DragonHDLatestNeural` (configurable) |


## Prerequisites

```bash
pip install azure-cognitiveservices-speech python-dotenv
```

> **macOS note**: the Speech SDK requires microphone permission. Allow it in  
> **System Settings → Privacy & Security → Microphone**.



## Set up a Speech resource

1. In your Foundry project → **Foundry Tools** → **Speech**
2. Create or select an Azure AI Speech resource
3. Copy the **Key** and **Endpoint** from the resource

Alternatively access via Speech Studio: [https://speech.microsoft.com/portal](https://speech.microsoft.com/portal)

## Environment variables

```
FOUNDRY_KEY=<your-speech-key>
SPEECH_ENDPOINT=https://<region>.api.cognitive.microsoft.com
```



## Run

```bash
python speech_app.py
```

The app listens for a spoken weather question, then reads back a sample weather alert.

## Sample output

```text
Using Azure Speech endpoint: https://brezyweather-bvp.cognitiveservices.azure.com/

=== BrezyWeather Voice Interface ===

BrezyWeather is listening... ask your weather question.
  Recognized: "What's the good dress to wear in Chennai?"

  Announcing alert: "BrezyWeather alert: A severe thunderstorm watch is in effect for your area until..."
  Alert announced successfully.
```

