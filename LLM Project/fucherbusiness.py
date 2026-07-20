import google.generativeai as genai
import streamlit as st

# ✅ Page title and header

st.title("🎓 AI Fucher Business Path Advisor")
st.write("Fill in your preferences and get a Business roadmap!")

#API Configuration
genai.configure(api_key="Enter your API key")
model = genai.GenerativeModel('gemini-1.5-flash')

