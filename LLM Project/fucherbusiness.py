import google.generativeai as genai
import streamlit as st

# ✅ Page title and header

st.title("🎓 AI Fucher Business Path Advisor")
st.write("Fill in your preferences and get a Business roadmap!")

#API Configuration
genai.configure(api_key="Enter your API key")
model = genai.GenerativeModel('gemini-1.5-flash')


def career_advice(tech, career, course, timeperiod):
    prompt = f"""
    your are my personal AI assistant that helps me with Bast Business advice.
    I'm planning to start a B in {tech}
    My goal is to become a {career}
    I want to pursue a course in {course}
    I want to achieve this goal in {timeperiod}
    
    Please Suggest me 
    1. The best learning path to achieve my goal
    2. The best resources to learn from
    3. The best projects to work on
    4. The best way to build a portfolio
    5. The best way to network and find job opportunities
    6. The best way to prepare for interviews
    7. Any other tips or advice to help me succeed in my career
    8. Suggest me a weekly schedule to follow to achieve my goal in the given time
    """
    response = model.generate_content(prompt)
    return response.text if response else "Sorry, I couldn't process that request."

