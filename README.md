# 🎥 YouTube Transcript Summarizer

An AI-powered application that extracts transcripts from YouTube videos and generates concise, meaningful summaries using Large Language Models (LLMs).

## 🚀 Overview

The **YouTube Transcript Summarizer** helps users quickly understand the content of long YouTube videos without watching the entire video.

The application:

1. Accepts a YouTube video URL.
2. Extracts the video's transcript.
3. Processes the transcript.
4. Sends the content to an LLM.
5. Generates an easy-to-understand summary.

This project is built as part of my journey toward becoming an **AI Engineer**, focusing on practical implementation of LLM-based applications.

## 🏗️ Project Architecture

```text
YouTube Video URL
        │
        ▼
┌─────────────────────┐
│  Extract Video ID   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Fetch Transcript    │
│ YouTube Transcript  │
│       API           │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Process Transcript  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│       LLM           │
│  Generate Summary   │
└──────────┬──────────┘
           │
           ▼
     📄 Summary
```

## 🛠️ Tech Stack

* **Python**
* **YouTube Transcript API**
* **LangChain**
* **OpenAI / LLM**
* **Virtual Environment (venv)**
* **Git & GitHub**

## 📂 Project Structure

```text
Youtube-Transcript-Summarizer/
│
├── src/
│   ├── get_transcript.py
│   └── ...
│
├── .gitignore
├── README.md
├── requirements.txt
└── ...
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Youtube-Transcript-Summarizer
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

⚠️ **Never commit your `.env` file or API keys to GitHub.**

Make sure `.env` is included in `.gitignore`.

## ▶️ Usage

Run the required Python script from the project root:

```bash
python src/get_transcript.py
```

Provide a valid YouTube video URL when prompted.

The application will fetch the transcript and process it for summarization.

## 🧠 What I Learned

Through this project, I practiced:

* Working with external APIs
* Extracting YouTube video transcripts
* Understanding transcript data structures
* Python project organization
* Virtual environment management
* Working with LLM APIs
* Prompt-based text summarization
* Environment variables and API-key security
* Git and GitHub workflow

## 🔮 Future Improvements

Planned improvements include:

* [ ] Add a Streamlit web interface
* [ ] Support multiple languages
* [ ] Add transcript chunking for long videos
* [ ] Improve summarization prompts
* [ ] Add timestamps to summaries
* [ ] Add key-points extraction
* [ ] Add downloadable summaries
* [ ] Add error handling for videos without transcripts
* [ ] Deploy the application

## 📌 Project Status

🚧 **Currently under development**

The core transcript extraction functionality is implemented, with LLM-based summarization and additional application features being developed incrementally.

## 👨‍💻 Author

**Shailesh Vishwakarma**

Data Analyst → AI Engineer

Currently building practical AI/LLM projects to strengthen my AI Engineering skills.

---

⭐ If you find this project useful, consider giving the repository a star!
