# 📬 Smart Email Assistant

Smart Email Assistant is a lightweight Python tool that uses AI to automatically generate professional replies to email messages. It also includes an escalation mechanism for messages with low confidence or unknown categories.

---

## 🚀 Features

- 🤖 Uses OpenRouter AI to generate responses
- ⚠️ Escalates uncertain messages and logs them
- 🔐 Uses `.env` file to securely store API keys
- 📁 Easy to integrate and extend for email workflows

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smart-email-assistant.git
cd smart-email-assistant

python3 -m venv venv
source venv/bin/activate  # For Windows use: venv\Scripts\activate

pip install -r requirements.txt

OPENROUTER_API_KEY=your_openrouter_api_key_here
