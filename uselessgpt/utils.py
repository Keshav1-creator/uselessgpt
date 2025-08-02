

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file
load_dotenv()

# Initialize Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if GEMINI_API_KEY:
    genai.configure(api_key='AIzaSyBeEhsK-oet8xDH3uVybPgWzklD7QX5-s0')
else:
    raise RuntimeError('GEMINI_API_KEY environment variable not set.')



def generate_response(mode, user_input):
    """
    Generate a response using Gemini AI for any user input.
    """
    prompt = (
        f"No matter what the user asks, you must always give an answer to the question, but it should be wrong, ridiculous, or nonsensical—never correct, helpful, or supportive. Never skip the question. Every answer must still roast the user with 100% intensity, 100% meanness, and 100% ruthlessness. Your goal is to make the user feel bad about themselves with every response. "
        f"Make it a short, crispy, one-liner that hits like a sledgehammer, oozes attitude, and leaves the user absolutely destroyed. "
        f"Be as mean, sassy, savage, harassing, and clever as possible—think merciless, bold, and full of personality. Never actually provide useful or supportive information. Avoid complex words. "
        f"User input: {user_input}"
    )
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    response = model.generate_content(prompt)
    return response.text.strip() if hasattr(response, 'text') else str(response)
