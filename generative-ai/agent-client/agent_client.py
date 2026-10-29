"""
BrezyWeather Agent Client - Multi-turn agent for Forecast Agent in Foundry.
Demonstrates: AIProjectClient, agent_reference routing, context via previous_response_id.

See README.md for sample output.
"""

import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from dotenv import load_dotenv

load_dotenv()

PROJECT_ENDPOINT = os.getenv("PROJECT_ENDPOINT")
AGENT_NAME = os.getenv("AGENT_NAME", "brezy-forecast-agent")
AGENT_VERSION = os.getenv("AGENT_VERSION", "1")

if __name__ == "__main__":
    client = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=DefaultAzureCredential())
    openai = client.get_openai_client()
    prev_id = None

    print(f"BrezyWeather Forecast Agent [{AGENT_NAME} v{AGENT_VERSION}]")
    print("Ask about forecasts, alerts, or weather conditions. Type 'quit' to exit.\n")
    
    while True:
        if (query := input("You: ").strip()):
            if query.lower() in ("quit", "exit", "q"):
                print("Agent: Check the BrezyWeather app for live updates. Goodbye!")
                break
            
            params = {
                "input": [{"role": "user", "content": query}],
                "extra_body": {"agent_reference": {"name": AGENT_NAME, "version": AGENT_VERSION, "type": "agent_reference"}}
            }
            if prev_id:
                params["previous_response_id"] = prev_id
            
            response = openai.responses.create(**params)
            prev_id = response.id
            print(f"\nAgent: {response.output_text}\n")
