def escalate_email(email_text, category, confidence):
    log_entry = f"ESCALATION NEEDED\nCategory: {category}\nConfidence: {confidence}\nEmail: {email_text}\n\n"
    with open("escalation_log.txt", "a") as file:
        file.write(log_entry)
    return {
        "status": "escalated",
        "reason": "Low confidence or unknown category",
        "logged_to": "escalation_log.txt"
    }