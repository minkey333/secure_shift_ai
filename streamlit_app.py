import streamlit as st
from app.agents.langgraph_agent import run_langgraph_agent
from datetime import datetime

st.set_page_config(page_title="SecureShift.AI", layout="wide")
st.title("🔐 SecureShift.AI — Code Security Reviewer")

st.sidebar.title("About")
st.sidebar.markdown(
    "Scan Python, Java, or SQL code for security vulnerabilities using static rules and GPT explanations."
)

code_input = st.text_area("✍️ Paste your code below:", height=300, value="""import os
user_input = input("Enter name: ")
os.system("echo " + user_input)
""")

if st.button("🚀 Run Secure Analysis"):
    with st.spinner("Running SecureShift Agent..."):
        result = run_langgraph_agent(code_input)
        st.success("✅ Analysis completed!")

        st.markdown("### 🔍 Step 1: Static Scan Results")
        st.json(result.get("static_results", "None"))

        st.markdown("### 🤖 Step 2: GPT Explanation")
        st.markdown(result.get("gpt_response", "None"))

        st.markdown("### 🧾 Final Markdown Report")
        st.markdown(result.get("report", "No report generated"))

        st.download_button(
            label="📥 Download Markdown Report",
            data=result.get("report", ""),
            file_name=f"SecureShift_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
            mime="text/markdown"
        )