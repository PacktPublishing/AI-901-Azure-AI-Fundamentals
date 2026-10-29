# BrezyWeather Agent Client

Connects to the **BrezyWeather Forecast Agent** deployed in Microsoft Foundry and runs a multi-turn conversation.

## What it demonstrates


| Concept                  | Details                                                              |
| ------------------------ | -------------------------------------------------------------------- |
| `AIProjectClient`        | Connects to a Foundry project endpoint                               |
| `agent_reference`        | Routes requests to a named, versioned Foundry agent via `extra_body` |
| Multi-turn sessions      | `previous_response_id` preserves conversation context                |
| `DefaultAzureCredential` | Managed identity auth — no hardcoded keys                            |


## Prerequisites

```bash
pip install azure-ai-projects>=2.1.0 azure-identity python-dotenv
```

Sign in for local development:

```bash
az login
```



## Set up the agent in Foundry first

1. Go to your Foundry project → **Agents** → **+ New agent**
2. Name: `brezy-forecast-agent`
3. Model: your deployed GPT-4o (e.g., `gpt-5.4`)
4. Instructions: *"You are the BrezyWeather Forecast Agent. Answer questions about weather conditions, forecasts, and alerts. Be concise and accurate."*
5. Enable **File search** and upload the files under the `brezyweather-files` folder.
6. Save and note the agent name



## Environment variables

```
PROJECT_ENDPOINT=https://<your-foundry-resource>.services.ai.azure.com/api/projects/<your-project>
AGENT_NAME=brezy-forecast-agent
AGENT_VERSION=1
```



## Run

```bash
python agent_client.py
```

## Sample output

```text
BrezyWeather Forecast Agent [brezy-forecast-agent v2]
Ask about forecasts, alerts, or weather conditions. Type 'quit' to exit.

You: How will I receive weather alerts?

Agent: You’ll receive BrezyWeather alerts through four channels: **push notifications** in the mobile app, **SMS text messages**, **email notifications**, and **in-app banner alerts**.

If you want, I can also help you figure out **how to turn each alert type on or off**.

You: Can you explain the difference between a watch and a warning?

Agent: Yes — the key difference is:

- A **watch** means **conditions are favorable** for severe weather to develop. You should **stay alert, monitor updates, and be ready to act**. Examples include a **Tornado Watch** or **Flood Watch**.
- A **warning** means severe weather has been **observed or is imminent**. You should **take action immediately**. Examples include a **Tornado Warning** or **Severe Thunderstorm Warning**.

A simple way to remember it:
- **Watch = Be prepared**
- **Warning = Take action now**

If you’d like, I can also explain what to do during a **tornado**, **thunderstorm**, or **flood** warning.

You: exit
Agent: Check the BrezyWeather app for live updates. Goodbye!
```

## Key concept: agent vs. model call

Unlike `chat_client.py` (which calls a model directly), this client uses `agent_reference` in the request body to invoke a **Foundry agent** — which may have tools, instructions, and memory configured in the portal.