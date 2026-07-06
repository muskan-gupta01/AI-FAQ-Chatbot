# 🤖 AI FAQ Chatbot

An AI-powered FAQ Chatbot built using **Python, Streamlit, NLP, TF-IDF, Cosine Similarity, and Groq LLM**. The chatbot answers user questions by matching them with a FAQ dataset and can also generate intelligent responses using an LLM when required.

---

# 📌 Project Overview

The AI FAQ Chatbot is designed to provide quick and accurate answers to frequently asked questions related to Artificial Intelligence, Machine Learning, Python, NLP, Data Science, and Streamlit.

The project combines traditional NLP techniques with Large Language Models (Groq LLM) to improve response quality and user experience.

---

# ✨ Features

- 🤖 AI-powered chatbot interface
- 🧠 NLP text preprocessing
- 📊 TF-IDF Vectorizer
- 📈 Cosine Similarity matching
- ⚡ Groq LLM integration
- 🎯 Confidence Score
- 🔍 Similar Question Suggestions
- 💬 Chat History
- ⬇ Download Chat History
- 📚 FAQ Dataset Preview
- 📊 Dashboard Statistics
- 🌙 Modern Dark UI
- 📱 Responsive Streamlit Interface

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Streamlit | Web Interface |
| Pandas | Dataset Handling |
| Scikit-learn | TF-IDF & Cosine Similarity |
| NLTK | Text Preprocessing |
| Groq API | AI Response Generation |
| JSON | Chat History Download |

---

# 📂 Project Structure

```
FAQ-Chatbot/
│
├── .streamlit/
│   └── config.toml
│
├── assets/
│
├── Screenshots/
│   ├── home_page.png
│   ├── chat_page.png
│   ├── features_page.png
│   └── demo.mp4
│
├── .env
├── .gitignore
├── app.py
├── chatbot.py
├── llm.py
├── utils.py
├── faq.csv
├── requirements.txt
└── README.md
```

---

# ⚙ Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/FAQ-Chatbot.git
```

## 2. Open Project

```bash
cd FAQ-Chatbot
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

## 4. Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 6. Configure Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_api_key_here
```

## 7. Run the Application

```bash
streamlit run app.py
```

---

# 💻 How It Works

1. User enters a question.
2. The question is preprocessed using NLP.
3. TF-IDF converts text into vectors.
4. Cosine Similarity finds the closest FAQ.
5. Confidence Score is calculated.
6. Similar questions are displayed.
7. If required, Groq LLM generates an intelligent response.
8. Chat history can be downloaded as JSON.

---

# 📸 Screenshots

## Home Page

> Add: `screenshots/home_page.png`

---

## Chat Interface

> Add: `screenshots/chat_page.png`

---

## Features Page

> Add: `screenshots/features_page.png`

---

# 🎥 Demo Video

Project demo video is available inside the project folder.

```
screenshots/demo.mp4
```

---

# 🚀 Future Improvements

- 🎤 Voice Input
- 🔊 Text-to-Speech
- 🌐 Multi-language Support
- 👤 User Authentication
- 🗄 Database Integration
- 📄 PDF Knowledge Base
- 📊 Chat Analytics

---

# 📈 Learning Outcomes

Through this project I learned:

- Natural Language Processing (NLP)
- Text Preprocessing
- TF-IDF Vectorization
- Cosine Similarity
- Streamlit Application Development
- REST API Integration
- Groq LLM Integration
- Prompt Engineering
- Git & GitHub
- AI Chatbot Development

---

# 👩‍💻 Developer

**Muskan Gupta**

AI & Python Enthusiast

---

# 📄 License

This project is developed for learning purposes and submitted as part of the **Alpha Internship**.

---

# ⭐ Acknowledgements

- Streamlit
- Scikit-learn
- NLTK
- Groq
- Python Community

---

## Thank You ❤️