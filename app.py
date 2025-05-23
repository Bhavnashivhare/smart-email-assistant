import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from orchestrator import handle_email

st.title("📬 Smart Email Assistant")

email_text = st.text_area("Paste Email Content Here")

if st.button("Analyze"):
    if email_text.strip():
        result = handle_email(email_text)
        st.json(result)
    else:
        st.warning("Please enter an email.")