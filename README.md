# 🤖 AI Chat Bot (Streamlit + LangChain + Hugging Face)

An interactive AI-powered chatbot built using **Streamlit**, **LangChain**, and **Hugging Face LLMs**.
This chatbot supports conversational memory and provides intelligent responses in real-time.

---

## 🚀 Features

* 💬 ChatGPT-style UI using Streamlit
* 🧠 Conversation memory (remembers previous messages)
* 🤖 Powered by LLaMA 3.1 (via Hugging Face)
* ⚡ Fast and simple interface
* 🌐 Ready for deployment on Streamlit Cloud
* 👤 Custom system prompt (includes creator identity)

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Hugging Face (LLM API)
* dotenv

---

## 📂 Project Structure

```
├── app.py                # Main Streamlit app
├── requirements.txt     # Dependencies
├── .env                 # API keys (not uploaded)
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add API Key

Create a `.env` file:

```
HUGGINGFACEHUB_API_TOKEN=your_api_key_here
```

---

### 5️⃣ Run the app

```bash
streamlit run app.py
```

---

## ☁️ Deployment (Streamlit Cloud)

1. Push your code to GitHub
2. Go to Streamlit Cloud
3. Connect your repository
4. Add your API key in **Secrets**:

```
HUGGINGFACEHUB_API_TOKEN="your_api_key_here"
```

5. Deploy 🚀

---

## 🧠 How It Works

* User inputs a message via chat UI
* Messages are stored using `st.session_state`
* Converted into LangChain message format
* Sent to Hugging Face LLM
* Response is displayed in chat format

---

## 🔐 Environment Variables

| Variable                 | Description              |
| ------------------------ | ------------------------ |
| HUGGINGFACEHUB_API_TOKEN | API key for Hugging Face |

---

## 🚀 Future Improvements

* 🌍 Real-time data integration (news/search)
* 📄 Chat with PDF (RAG system)
* 💳 SaaS model with API keys
* 🎨 Advanced UI customization
* 📊 Analytics dashboard

---

## 👨‍💻 Author

**Pervez Abbas**
AI Intern at SDA Technology Hub, Gilgit Baltistan, Pakistan 🇵🇰

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
