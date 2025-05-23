from agents.classification_agent import EmailClassifier
from agents.response_generator import generate_response
from agents.escalation_agent import escalate_email

classifier = EmailClassifier()

def handle_email(email_text):
    prediction = classifier.predict(email_text)
    category = prediction['predicted_category']
    confidence = prediction['confidence']

    # Always generate response
    response = generate_response(confidence, category, email_text)

    # Attach escalation info if needed
    if confidence < 0.6 or category == "Other":
        response["escalation"] = {
            "status": "escalated",
            "reason": "Low confidence or unknown category",
            "logged_to": "escalation_log.txt"
        }

    return response