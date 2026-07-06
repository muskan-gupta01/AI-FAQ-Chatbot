import streamlit as st
import json
from datetime import datetime
from chatbot import FAQChatbot

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# LOAD CHATBOT (cached)
# -------------------------------------------------
@st.cache_resource
def load_chatbot():
    return FAQChatbot("faq.csv")

bot = load_chatbot()

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------------------------
# CUSTOM CSS (UI UPGRADE)
# -------------------------------------------------
st.markdown("""
<style>

/* Main Background */
.stApp{
    background:#0f172a;
    color:#ffffff;
}

/* Header */
.main-title{
    text-align:center;
    font-size:50px;
    font-weight:800;
    color:#2563eb;
    margin-bottom:5px;
}

.subtitle{
    text-align:center;
    font-size:18px;
    color:#555;
    margin-bottom:25px;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#1e293b;
}

/* Sidebar headings */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label{
    color:white !important;
}

/* Metrics */
section[data-testid="stSidebar"] [data-testid="metric-container"]{
    background:#334155;
    border-radius:12px;
}

section[data-testid="stSidebar"] [data-testid="metric-container"] label,
section[data-testid="stSidebar"] [data-testid="metric-container"] div{
    color:white !important;
}

/* Metric Cards */
div[data-testid="metric-container"]{
    background:#1e293b;
    border:1px solid #334155;
    border-radius:15px;
    padding:18px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.3);
}

div[data-testid="metric-container"] *{
    color:white !important;
}
    border-radius:15px;
    padding:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.12);
    border:1px solid #dbeafe;
}

/* Chat Input */
.stChatInput{
    border-radius:15px;
}

/* Buttons */
.stButton>button{
    width:100%;
    border-radius:10px;
    background:#2563eb;
    color:white !important;
    font-weight:bold;
    transition:0.3s;
}

.stButton>button:hover{
    background:#1d4ed8;
    transform:scale(1.02);
}

/* Download Button */
.stDownloadButton>button{
    width:100%;
    border-radius:10px;
    background:#16a34a;
    color:white;
    font-weight:bold;
}

.stDownloadButton>button:hover{
    background:#15803d;
}

/* Chat Messages */
[data-testid="stChatMessage"]{
    background:#1e293b;
    color:white;
    border-radius:15px;
    padding:12px;
    margin-bottom:12px;
    box-shadow:0 2px 10px rgba(0,0,0,0.25);
}

/* Expander */
.streamlit-expanderHeader{
    font-weight:bold;
}

/* User Message */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]){
    background:#2563eb;
    color:white;
    border-radius:18px;
    padding:12px;
    margin-bottom:12px;
    border:1px solid #b7e4a8;
}

/* Assistant Message */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]){
    background:#334155;
    color:white;
    border-radius:18px;
    padding:12px;
    margin-bottom:12px;
    border:1px solid #dbeafe;
}

/* Hover Effect */
[data-testid="stChatMessage"]:hover{
    transform:scale(1.01);
    transition:0.2s;
    box-shadow:0 4px 15px rgba(0,0,0,0.08);
}
                        
</style>
""", unsafe_allow_html=True)
# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.divider()

st.markdown("""
<div style="
background: linear-gradient(90deg,#2563eb,#4f46e5);
padding:25px;
border-radius:20px;
color:white;
text-align:center;
margin-bottom:20px;
box-shadow:0px 5px 15px rgba(0,0,0,0.2);
">

<h1 style="margin-bottom:10px;">🤖 AI FAQ Chatbot</h1>

<p style="font-size:18px;">
AI-powered FAQ Assistant using NLP, TF-IDF, Cosine Similarity & Groq LLM
</p>

</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
with st.sidebar:
    st.title("⚙ Control Panel")

    st.metric("📚 Total FAQs", bot.total_faqs())
    st.metric("💬 Messages", len(st.session_state.messages))

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    # Download chat
    chat_json = json.dumps(st.session_state.messages, indent=2)

    st.download_button(
        "⬇ Download Chat History",
        data=chat_json,
        file_name="chat_history.json",
        mime="application/json"
    )

    st.markdown("---")
    st.caption("Built with Streamlit + NLP")

# -------------------------------------------------
# DISPLAY CHAT HISTORY
# -------------------------------------------------
for msg in st.session_state.messages:

    avatar = "👤" if msg["role"] == "user" else "🤖"

    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

        if "time" in msg:
            st.caption(f"🕒 {msg['time']}")

# -------------------------------------------------
# INPUT
# -------------------------------------------------
if "quick_question" in st.session_state:

    user_input = st.session_state["quick_question"]

    del st.session_state["quick_question"]

else:

    user_input = st.chat_input("💬 Type your question...")


if user_input and user_input.strip():

    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "time": time_now
    })

    with st.chat_message("user", avatar="👤"):
        st.markdown(user_input)
        st.caption(f"🕒 {time_now}")

    # BOT RESPONSE
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking..."):

            result = bot.get_answer(user_input)

            answer = result.get("answer", "No answer found")
            confidence = result.get("confidence", 0.0)
            matched_question = result.get("matched_question")
            suggestions = result.get("suggestions", [])

        import time

        placeholder = st.empty()

        text = ""

        for word in answer.split():

            text += word + " "

            placeholder.markdown(text)

            time.sleep(0.03)

        # Suggestions (FIXED BLOCK)
        if suggestions:
            st.markdown("### 🔍 Similar Questions")
            for s in suggestions:
                st.write(f"• {s['question']} ({s['score']*100:.1f}%)")

        # Confidence
        if matched_question:
            st.divider()
            st.write(f"📌 Matched: {matched_question}")
            st.write(f"🎯 Confidence: {confidence*100:.2f}%")
            st.progress(float(confidence))

    # Save bot message
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "time": time_now
    })

# -------------------------------------------------
# WELCOME SCREEN
# -------------------------------------------------
if len(st.session_state.messages) == 0:
    st.info("""
### 👋 Welcome

Try asking:
- What is AI?
- What is Machine Learning?
- What is Python?
- What is NLP?
- What is Data Science?
""")

# -------------------------------------------------
# STATS BAR
# -------------------------------------------------
st.divider()

st.subheader("📊 Dashboard")

c1, c2, c3, c4 = st.columns(4)

total_messages = len(st.session_state.messages)
user_messages = len([m for m in st.session_state.messages if m["role"] == "user"])
bot_messages = len([m for m in st.session_state.messages if m["role"] == "assistant"])

c1.metric("📚 FAQs", bot.total_faqs())
c2.metric("👤 User Messages", user_messages)
c3.metric("🤖 Bot Replies", bot_messages)
c4.metric("💬 Total Messages", total_messages)

# -------------------------------------------------
# QUICK QUESTIONS
# -------------------------------------------------
st.divider()

st.subheader("💡 Quick Questions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🤖 What is AI?"):
        st.session_state["quick_question"] = "What is AI?"

    if st.button("🐍 What is Python?"):
        st.session_state["quick_question"] = "What is Python?"

with col2:
    if st.button("🧠 What is Machine Learning?"):
        st.session_state["quick_question"] = "What is Machine Learning?"

    if st.button("💬 What is NLP?"):
        st.session_state["quick_question"] = "What is NLP?"

with col3:
    if st.button("📊 What is Data Science?"):
        st.session_state["quick_question"] = "What is Data Science?"

    if st.button("🌐 What is Streamlit?"):
        st.session_state["quick_question"] = "What is Streamlit?"

# -------------------------------------------------
# DATASET PREVIEW
# -------------------------------------------------
with st.expander("📖 FAQ Dataset"):
    st.dataframe(
    bot.data[["question","answer"]],
    use_container_width=True,
    hide_index=True
)
st.divider()

st.subheader("✨ Features")

col1, col2 = st.columns(2)

with col1:

    st.success("✅ NLP Text Preprocessing")

    st.success("✅ TF-IDF Vectorizer")

    st.success("✅ Cosine Similarity")

    st.success("✅ Chat History")

with col2:

    st.success("✅ Download Chat")

    st.success("✅ Confidence Score")

    st.success("✅ FAQ Dataset Preview")

    st.success("✅ LLM Support (Groq)")
# -------------------------------------------------
# ABOUT
# -------------------------------------------------
with st.expander("ℹ About Project"):

    st.markdown("""
# 🤖 AI FAQ Chatbot

### Technologies Used

- 🐍 Python
- 🎨 Streamlit
- 🧠 Natural Language Processing (NLP)
- 📊 TF-IDF Vectorizer
- 📈 Cosine Similarity
- ⚡ Groq LLM API

---

### Features

✅ Smart FAQ Matching

✅ AI Generated Answers (Groq)

✅ Confidence Score

✅ Similar Question Suggestions

✅ Download Chat History

✅ Interactive Dashboard

✅ Modern Responsive UI

✅ FAQ Dataset Preview

---

Developed by **Muskan Gupta**

Alpha Internship Project
""")
# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.divider()

st.markdown("""
<div style="
background: linear-gradient(90deg,#1e40af,#2563eb);
padding:35px;
border-radius:20px;
text-align:center;
margin-top:20px;
">

<h1 style="color:white;font-size:34px;margin-bottom:10px;">
🤖 AI FAQ Chatbot
</h1>

<p style="color:white;font-size:20px;font-weight:bold;">
Developed by Muskan Gupta
</p>

<p style="color:#f8fafc;font-size:18px;">
Python • Streamlit • NLTK • Scikit-learn • TF-IDF • Groq LLM
</p>

<p style="color:#dbeafe;font-size:16px;">
AI-powered FAQ Assistant for Alpha Internship Project
</p>

</div>
""", unsafe_allow_html=True)