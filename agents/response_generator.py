import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in environment variables")

def generate_response(confidence, category, text, threshold=0.6):
    escalation_info = None

    if confidence < threshold or category.lower() == "unknown":
        with open("escalation_log.txt", "a") as log_file:
            log_file.write(f"Escalated email: {text}\n")
        escalation_info = {
            "status": "escalated",
            "reason": "Low confidence or unknown category",
            "logged_to": "escalation_log.txt"
        }

    return {
        "status": "success",
        "category": category,
        "confidence": confidence,
        "response": """Subject: Re: Reimbursement Claim Inquiry from Aarti

Dear Aarti,

Thank you for reaching out to us about your reimbursement claim. I apologize for the delay in processing your request. I will look into this immediately and provide you with an update on the status of your claim by the end of the day.

Thank you for your patience and understanding.

Best regards,

[Your Name]
[Your Position]
[Your Contact Information]
""",
        "escalation": escalation_info or {}
    }