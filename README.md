# 🤖 AI FAQ Chatbot

<p align="center">
  <b>An AI-powered FAQ Chatbot built using Python, Streamlit, NLP, TF-IDF, Cosine Similarity, Scikit-learn, and Groq LLM.</b>
</p>

<p align="center">
This chatbot intelligently answers user questions by first searching a FAQ knowledge base using NLP and semantic similarity. If no relevant FAQ is found, it generates an AI-powered response using the Groq Large Language Model (LLM).
</p>

---

# 🚀 Features

- 🤖 AI-powered FAQ Chatbot
- 🧠 Groq LLM Integration
- 🔍 TF-IDF Vectorization
- 📊 Cosine Similarity Matching
- 📝 NLP Text Preprocessing
- 💬 Interactive Chat Interface
- 📜 Chat History
- ⬇ Download Chat History (JSON)
- 📈 Dashboard with Statistics
- 💡 Quick Question Buttons
- 📖 FAQ Dataset Preview
- ⚡ Fast & Responsive Streamlit UI

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application |
| Pandas | Data Handling |
| NLTK | NLP Preprocessing |
| Scikit-learn | Machine Learning |
| TF-IDF | Text Vectorization |
| Cosine Similarity | FAQ Matching |
| Groq LLM | AI Response Generation |
| JSON | Chat Export |

---

# 📂 Project Structure

```text
AI-FAQ-Chatbot/
│
├── app.py
├── chatbot.py
├── utils.py
├── faq.csv
├── requirements.txt
├── README.md
├── .gitignore
├── images/
│   ├── home_page1.png
│   ├── home_page2.png
│   ├── home_page3.png
│   └── home_page4.png
└── venv/
```

---

# 📸 Project Screenshots

## 🏠 Home Page

![Home Page](images/home_page1.png)

---

## 💬 Chat Interface

![Chat Interface](images/home_page2.png)

---

## 🤖 AI Response

![AI Response](images/home_page3.png)

---

## 📊 Dashboard & Features

![Dashboard](images/home_page4.png)

---

# ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/muskan-gupta01/AI-FAQ-Chatbot.git
```

### 2️⃣ Open Project

```bash
cd AI-FAQ-Chatbot
```

### 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 4️⃣ Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure Groq API Key

Create a `.env` file inside the project folder and add:

```text
GROQ_API_KEY=your_groq_api_key_here
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 🧠 How It Works

1. User enters a question.
2. NLP preprocesses the input.
3. TF-IDF converts text into vectors.
4. Cosine Similarity finds the most relevant FAQ.
5. If a matching FAQ is found, its answer is displayed.
6. Otherwise, the chatbot generates an AI response using Groq LLM.
7. The conversation is saved in chat history.
8. Users can download the chat history in JSON format.

---

# ✨ Key Highlights

- NLP-based FAQ Search
- AI-powered Responses using Groq LLM
- Confidence Score Display
- Similar Question Suggestions
- Interactive Dashboard
- Download Chat History
- FAQ Dataset Preview
- Modern Streamlit UI
- Cached Model Loading
- Fast Response Time

---

# 🔮 Future Improvements

- 🎤 Voice Input
- 🔊 Text-to-Speech
- 🌍 Multi-language Support
- 📄 PDF Knowledge Base
- 🗄 Database Integration
- 👤 User Authentication
- ☁️ Cloud Deployment

---

# 👩‍💻 Developer

**Muskan Gupta**

### 🔗 LinkedIn

https://linkedin.com/in/muskan-gupta-551293386

### 💻 GitHub

https://github.com/muskan-gupta01

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is developed for educational, learning, internship, and portfolio purposes.

© 2026 Muskan Gupta. All Rights Reserved.
