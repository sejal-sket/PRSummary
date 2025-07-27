# 🔍 PR Summarizer using Ollama + Python

This project is a lightweight tool to generate **summaries of GitHub pull requests (PRs)** using locally running LLMs via the [Ollama](https://ollama.com) API. It is designed for developers who want fast, offline summarization with minimal setup.

---

## 🚀 Features

- ✅ Takes a PR description or message as input
- ✅ Sends the prompt to a **local Ollama model** (e.g., `gemma:2b`)
- ✅ Handles streamed responses from the Ollama API
- ✅ Displays the **AI-generated summary**
- ✅ Kept modular in an `independent/` folder for reuse or future API integration

---

## 🧱 Project Structure

project-root/
│
├── independent/
│ └── summarize_pr.py # Main script that interacts with Ollama API
│
└── README.md # This file


---

## ⚙️ Setup Instructions (Windows)

### 1. ✅ Install Python

Make sure Python 3.8+ is installed.  
To check:
```bash
"python --version"

---

### 2. ✅ Install Ollama
Ollama allows you to run LLMs locally.

Download & install from: https://ollama.com/download

Once installed, pull a model (e.g., gemma:2b):


ollama pull gemma:2b
Start the Ollama server (if not auto-started):

ollama run gemma:2b

This runs the server at:
http://localhost:11434

Clone or Create the Script


Open terminal in the independent/ folder and run:
python summarize_pr.py


Next Steps (Suggestions)
 Convert this into a Flask API

 Take user input interactively or from GitHub

 Add file-based input/output

 Deploy as a lightweight internal tool for your team

Powered By
Ollama

Gemma Model

Python Requests


Contributions
This project is experimental and modular. Feel free to fork and build your own enhancements.

