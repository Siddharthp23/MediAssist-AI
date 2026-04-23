from groq import Groq
from app.core.config import GROQ_API_KEY
from app.prompts.templates import PATIENT_SUMMARY_PROMPT

client = Groq(api_key=GROQ_API_KEY)

def generate_summary(input_text: str):
    prompt = PATIENT_SUMMARY_PROMPT.format(input_text=input_text)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content