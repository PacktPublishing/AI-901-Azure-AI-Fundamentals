"""
BrezyWeather Chat Client - Multi-turn AI assistant for BrezyWeather app using Microsoft Foundry.
Demonstrates: AIProjectClient, openai Responses API, context maintenance via previous_response_id.

See README.md for sample output.
"""

import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from dotenv import load_dotenv

load_dotenv("../../.env")

PROJECT_ENDPOINT = os.getenv("PROJECT_ENDPOINT")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME", "gpt-5.4")
SYSTEM_PROMPT = "You are BrezyBot, the AI assistant for BrezyWeather — a weather forecasting app. Help users understand forecasts, interpret weather alerts, plan outdoor activities, and answer meteorological questions. Be concise, friendly, and weather-focused."

print(f"Using Foundry project endpoint: {PROJECT_ENDPOINT}\nUsing OpenAI deployment: {DEPLOYMENT_NAME}\n")

if __name__ == "__main__":
    openai = AIProjectClient(
        endpoint=PROJECT_ENDPOINT,
        credential=DefaultAzureCredential(),
    ).get_openai_client()
    
    previous_response_id = None
    print("BrezyWeather Assistant (type 'quit' to exit)\n")
    
    while True:
        if (user_input := input("You: ").strip()):
            if user_input.lower() in ("quit", "exit", "q"):
                print("BrezyBot: Stay dry out there!")
                break
            
            params = {"model": DEPLOYMENT_NAME, "instructions": SYSTEM_PROMPT, "input": user_input}
            if previous_response_id:
                params["previous_response_id"] = previous_response_id
            
            response = openai.responses.create(**params)
            previous_response_id = response.id
            print(f"\nBrezyBot: {response.output_text}\n")
