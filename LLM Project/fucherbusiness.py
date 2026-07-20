import google.generativeai as genai
import streamlit as st

# ✅ Page title and header

st.title("🎓 AI Fucher Business Path Advisor")
st.write("Fill in your preferences and get a Business roadmap!")

#API Configuration
genai.configure(api_key="Enter your API key")
model = genai.GenerativeModel('gemini-1.5-flash')


def career_advice(filled, Amount, profit,timeperiod):
    prompt = f"""
    your are my personal AI assistant that helps me with Bast Business advice.
    I'm planning to start a Business in {filled}
    I am able to invest in starting of a business {Amount}
    I want to get profit in this percent {profit}
    I want to achieve the best growth and profit in  {timeperiod}
    
    Please Suggest me 
    1. The best learning path to 
    2. The best resources to learn business
    3. The best place to start business 
    4. The best way to build a stable business
    5. The best way to connect and find clients 
    6. The best way to prepare for interviews
    7. Any other tips or advice to help me succeed in my life
    8. Suggest me a weekly schedule to follow to achieve my goal in the given time
    """
    response = model.generate_content(prompt)
    return response.text if response else "Sorry, I couldn't process that request."

# Streamlit UI
tech = st.selectbox("Select Technology", ["AI", "Data Science", "Web Development", "Cybersecurity", "Cloud Computing"])
career = st.text_input("Enter Career Goal (e.g. Data Scientist, ML Engineer, Web Developer)")
course = st.selectbox("Select Course Type", ["Bootcamp", "Certification", "Degree", "Self-paced Learning"])
timeperiod = st.selectbox("Select Time Period", ["3 months", "6 months", "1 year", "2 years"])
