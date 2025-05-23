import os
import requests
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in environment variables")

def generate_response(confidence, category, text, threshold=0.6):
    escalation_info = None

    # Escalate if confidence is low or category is unknown
    if confidence < threshold or category.lower() == "unknown":
        with open("escalation_log.txt", "a") as log_file:
            log_file.write(f"Escalated email: {text}\n")
        escalation_info = {
            "status": "escalated",
            "reason": "Low confidence or unknown category",
            "logged_to": "escalation_log.txt"
        }

    try:
        # Prompt for the model
        prompt = f"Provide a short, professional reply to this email:\n\n{text}"

        # OpenRouter API call
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mistralai/mixtral-8x7b-instruct",  # ✅ Valid OpenRouter model
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        )

        data = response.json()
        print("🔍 Raw response from OpenRouter:", data)  # Optional: debug log

        # Validate response
        if not data.get("choices") or "message" not in data["choices"][0]:
            return {
                "status": "error",
                "message": f"OpenRouter call failed: {data.get('error', 'Unexpected response format')}",
                "escalation": escalation_info or {}
            }

        # Extract reply
        reply = data["choices"][0]["message"]["content"]

        result = {
            "status": "success",
            "category": category,
            "confidence": confidence,
            "response": reply
        }

        if escalation_info:
            result["escalation"] = escalation_info

        return result

    except Exception as e:
        return {
            "status": "error",
            "message": f"OpenRouter call failed: {str(e)}",
            "escalation": escalation_info or {}
        }