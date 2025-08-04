import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# 🔐 Gemini API key
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash-latest")

# Instruction as part of the prompt
SYSTEM_INSTRUCTION = (
    "You are a helpful assistant that only answers questions related to flood safety, give preventive measures, short points on flood safety, "
    "emergency preparedness, evacuation planning, and disaster relief. "
    "If a question is outside this scope, politely redirect the user."
)

def ask_gemini_bot(user_question):
    try:
        full_prompt = f"{SYSTEM_INSTRUCTION}\n\nUser: {user_question}"
        response = model.generate_content(full_prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Gemini error: {str(e)}"


