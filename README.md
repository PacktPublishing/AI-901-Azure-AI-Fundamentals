# AI-901-Azure-AI-Fundamentals
AI-901 Azure AI Fundamentals, published by Packt

# Microsoft Azure AI Fundamentals - Exam Prep

Standalone Python scripts used to demonstrate Azure AI Foundry SDK usage, as part of the **AI-901: Microsoft Azure AI Fundamentals** exam-prep video course. Each demo is a single-file script, fronted by its own `README.md`, that illustrates one Azure AI capability end-to-end.

These are demo/teaching scripts, not a deployable application. They all revolve around **BrezyWeather**, a fictional weather app, used as a running example persona for narrative continuity across the course.

## Demos

| Folder                                                                         | Demo               | What it shows                                                        |
| ------------------------------------------------------------------------------ | ------------------ | -------------------------------------------------------------------- |
| `[computer-vision/image-analysis](computer-vision/image-analysis)`             | Image Analyzer     | Multimodal Responses API — text + image input (URL and local base64) |
| `[computer-vision/image-generation](computer-vision/image-generation)`         | Image Generator    | Generating images with a Foundry image model                         |
| `[content-understanding/extraction-app](content-understanding/extraction-app)` | Content Extraction | Azure AI Content Understanding for structured data extraction        |
| `[generative-ai/chat-client](generative-ai/chat-client)`                       | Chat Client        | Multi-turn conversational assistant using the Responses API          |
| `[generative-ai/agent-client](generative-ai/agent-client)`                     | Agent Client       | Foundry Agent with a knowledge base (file-based grounding)           |
| `[speech/speech-sdk-app](speech/speech-sdk-app)`                               | Voice Interface    | Azure AI Speech SDK — speech-to-text and text-to-speech              |
| `[text-analysis/text-analysis-app](text-analysis/text-analysis-app)`           | Text Analysis      | Azure AI Language — sentiment, key phrases, entity recognition       |

Each subfolder's `README.md` has demo-specific prerequisites, setup steps, and sample output.

## Common setup

All demos share one dependency list and one `.env` file.

1. Create and activate a virtual environment, then install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Sign in to Azure (used by `DefaultAzureCredential` for local development):

   ```bash
   az login
   ```

3. Create a `.env` file in this folder (`content/demo/.env`) and populate only the variables required by the demo(s) you plan to run:

   ```env
   PROJECT_ENDPOINT=https://<your-foundry-resource>.services.ai.azure.com/api/projects/<your-project>
   DEPLOYMENT_NAME=gpt-5.4
   AGENT_NAME=<your-agent-name>
   LANGUAGE_ENDPOINT=https://<your-language-resource>.cognitiveservices.azure.com/
   SPEECH_ENDPOINT=https://<your-speech-resource>.cognitiveservices.azure.com/
   CONTENT_UNDERSTANDING_ENDPOINT=https://<your-content-understanding-resource>.cognitiveservices.azure.com/
   IMAGE_MODEL=<your-image-model-deployment>
   ```

   Never commit real endpoint or key values.

4. Run any demo script directly, e.g.:

   ```bash
   python computer-vision/image-analysis/image_analysis_app.py
   ```