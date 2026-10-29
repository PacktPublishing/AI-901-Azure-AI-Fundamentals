# BrezyWeather Chat Client

Multi-turn conversational assistant for the BrezyWeather app using Microsoft Foundry.

## What it demonstrates

| Concept | Details |
|---|---|
| `AIProjectClient` | Connects to a Foundry project endpoint |
| Responses API | `openai.responses.create()` — the current Foundry chat pattern |
| Multi-turn context | `previous_response_id` carries conversation history across turns |
| `DefaultAzureCredential` | Managed identity auth — no hardcoded keys |

## Prerequisites

```bash
pip install azure-ai-projects>=2.1.0 azure-identity python-dotenv
```

Sign in to Azure (for local development):

```bash
az login
```

## Environment variables

Create a `.env` file in this folder (or in the parent `course-demo/` folder):

```
PROJECT_ENDPOINT=https://<your-foundry-resource>.services.ai.azure.com/api/projects/<your-project>
DEPLOYMENT_NAME=gpt-5.4
```

`PROJECT_ENDPOINT` is shown in the Foundry portal under your project → **Overview**.

## Run

```bash
python chat_client.py
```

Type weather questions at the prompt. The assistant remembers context across turns. Type `quit` to exit.

## Sample session

```text
Using Foundry project endpoint: https://brezyweather-bvp.services.ai.azure.com/api/projects/brezyweather
Using OpenAI deployment: gpt-5.4

BrezyWeather Assistant (type 'quit' to exit)

You: Explain the difference between a thunderstorm watch and a warning.

BrezyBot: A **thunderstorm watch** means **conditions are favorable** for thunderstorms to develop.
- Think: **“Be prepared.”**
- Storms may happen, but they are not necessarily occurring yet in your area.

A **thunderstorm warning** means a thunderstorm is **happening now or expected soon** in the warned area.
- Think: **“Take action.”**
- This is more urgent, especially if the storm could bring **damaging winds, hail, heavy rain, or frequent lightning**.

### Easy way to remember
- **Watch = Watch out** for possible storms
- **Warning = Warning!** Storm is imminent or already occurring

If you want, I can also explain the difference between a **severe thunderstorm warning** and a **tornado warning**.

You: What are the best weather apps for real-time storm alerts?

BrezyBot: For **real-time storm alerts**, the best apps are usually the ones that combine **official alerts**, **fast notifications**, and **good radar**.

### Top picks
1. **The Weather Channel**
   - Strong push alerts
   - Good radar and storm tracking
   - Easy for most people to use

2. **AccuWeather**
   - Timely warnings and minute-by-minute precipitation alerts
   - Good for everyday use plus severe weather

3. **Weather Underground**
   - Good radar and local conditions
   - Useful if you like detailed weather data

4. **MyRadar**
   - Excellent radar-focused app
   - Great for watching storm movement in real time

5. **NOAA / National Weather Service-based apps**
   - Best for **official U.S. alerts**
   - Good if you want direct alert information without much extra clutter

6. **RadarScope**
   - Best for weather enthusiasts and advanced users
   - Very detailed radar, but less beginner-friendly

### Best by need
- **Best overall for most people:** The Weather Channel or AccuWeather
- **Best radar:** MyRadar
- **Best official alerts:** NOAA/NWS-based apps
- **Best for advanced storm tracking:** RadarScope

### What to look for in a storm alert app
- **Push notifications for severe weather**
- **Official NWS/NOAA alerts**
- **Live radar**
- **Lightning tracking**
- **Location-based warnings**
- **Reliable background updates**

### Important tip
No single app is perfect. For the best coverage, many weather-aware users rely on:
- **one general weather app**, plus
- **one radar app**

If you want, I can recommend the **best storm alert app for iPhone or Android specifically**.

You: exit

BrezyBot: Stay dry out there!
```
