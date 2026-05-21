# =========================================
# Gemini AI Coach
# =========================================

# Install required packages:
# pip install google-genai
# pip install python-dotenv

from google import genai
from google.genai.types import GenerateContentConfig, ThinkingConfig

from dotenv import load_dotenv
import os

# =========================================
# Load Environment Variables
# =========================================

load_dotenv()

# =========================================
# Get API Key
# =========================================

def get_api_key() -> str:
    """
    Gets Gemini API key from .env file
    """

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not found in .env file"
        )

    return api_key

# =========================================
# Create Gemini Client
# =========================================

def make_client() -> genai.Client:
    """
    Creates Gemini client
    """
    return genai.Client(api_key=get_api_key())

# =========================================
# AI Coach Function
# =========================================

def get_coaching(prompt: str, style: str = "quick") -> None:
    """
    Generates coaching response using different Gemini models

    Styles:
    quick = Fast response using Flash model
    deep  = Detailed response using Pro model + Thinking
    """

    print(f"\n--- STARTING {style.upper()} COACHING ---")

    # Convert style to lowercase
    style = style.lower()

    # Select model based on style
    if style == "quick":

        model_name = "gemini-2.5-flash-lite"

        # No thinking for quick mode
        config = None

    elif style == "deep":

        model_name = "gemini-2.5-flash"

        # Enable thinking for deep mode
        config = GenerateContentConfig(
            thinking_config=ThinkingConfig(
                thinking_budget=1024
            )
        )

    else:
        raise ValueError(
            "Invalid style. Use 'quick' or 'deep'."
        )

    print(f"Selected Model: {model_name}")

    try:
        # Create Gemini client
        client = make_client()

        # Send request to Gemini
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
            config=config
        )

        # Print response
        print("\n--- AI COACH RESPONSE ---\n")

        print(response.text)

    except Exception as e:
        print(f"\n[ERROR] {e}")

    finally:
        print("\nProgram completed.")

# =========================================
# Test Calls
# =========================================

if __name__ == "__main__":

    print("Running AI Coach Tests...")

    # Quick coaching
    get_coaching(
        "What are 3 tips for public speaking?",
        style="quick"
    )

    # Deep coaching
    get_coaching(
        "Write a motivational speech about overcoming challenges.",
        style="deep"
    )