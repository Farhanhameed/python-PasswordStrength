import streamlit as st
import re
st.set_page_config(page_title="Password strengthen check", page_icon="🔒")
st.title("🔒Password Strengthen checker")
st.markdown("""
## Welcome to password checker strengthen
            We will help you to choose the stronger password 🔒
            """)
password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password:
    if len(password) >=8:
        score += 1
    else:
        feedback.append("❌Password should be 8 characters long")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌Password should contain both upper & lower case characters")
    
    if re.search(r"\d", password):
        score +=1
    else:
        feedback.append("❌Password should contain at least one number")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score +=1
    else:
        feedback.append("❌Password should contain at least one special character")
    
    if score == 4:
        feedback.append("✔ Your password is strong")
    elif score == 3:
        feedback.append("🟡 Your password is medium strength. Kindly make it stronger")
    else:
        feedback.append("🟠 Your password is weak. Kindly make it stronger")

    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter your password to get started")