from google import genai
from google.genai import types
from google.genai.types import GenerateContentConfig, ThinkingConfig


import os
from dotenv import load_dotenv

load_dotenv()  # reads .env in your project folder

def get_api_key() -> str:
    """
    Return an API key from env vars (GEMINI_API_KEY).
    Raises if not set.
    """
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise RuntimeError(
            "Missing API key. Set GEMINI_API_KEY "
            "(e.g., export GEMINI_API_KEY='YOUR_KEY')"
        )
    return key


def make_client() -> genai.Client:
    """
    Create a Google GenAI client for the Developer API.
    """
    return genai.Client(api_key=get_api_key())


client = make_client()



def get_coaching(prompt: str, style: str = "quick"):
    """Generates a response from the AI coach based on requested style."""
    print(f"\n--- INITIATING REQUEST: {style.upper()} COACHING ---")
    # Task 2 logic will be added here

    print("Model selection logic will be added here.")

# --- Test Functions ---
# --- Test calls ---
if __name__ == "__main__":
    print("Running tests...")
    get_coaching("What are three tips for public speaking?", style="quick")
    get_coaching("Write a short, motivational speech about overcoming challenges.", style="deep")