import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Choose model
model = genai.GenerativeModel("gemini-1.5-flash")

print("👋 Welcome to Gemini Chat! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        print("👋 Goodbye!")
        break

    response = model.generate_content(user_input)
    print("Gemini:", response.text, "\n")
