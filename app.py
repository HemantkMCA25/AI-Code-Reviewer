import streamlit as st
from review import run_review

st.set_page_config(page_title="AI Code Reviewer", layout="wide")

st.title("🤖 AI Code Reviewer (Hybrid Version)")
st.caption("Static Analysis + Optional AI Enhancement")

code = st.text_area("Paste your Python code here", height=250)

col1, col2 = st.columns([1, 3])

with col1:
    review_btn = st.button("🧑‍💻 Review Code")

if review_btn and code.strip():

    result = run_review(code)

    st.subheader("📊 Final Score")
    st.metric(label="Score (0-100)", value=result["score"])

    st.subheader("🧠 Analysis Mode")

    if result.get("mode") == "AI":
        st.success("🤖 AI-Enhanced Explanation")
    else:
        st.info("🧠 Rule-Based Explanation (No API (fallback) mode)")

    st.subheader("📌 Metrics")
    st.json(result["metrics"])

    st.subheader("📝 Feedback")
    st.write(result["feedback"])

elif review_btn:
    st.warning("Please paste some code before reviewing.")