# 🚀 Project Title: RESUME_KEYWORD_EXTRACTOR

## 📌 Problem Statement
Recruiters face challenges in manually screening large volumes of resumes.
Identifying relevant technical skills from unstructured PDF resumes is time-consuming.
There is a need for an automated tool to extract, filter, and rank resumes efficiently.
This project fetches resumes from Gmail, matches them with required skills, and ranks them.
An interactive Streamlit interface helps recruiters preview and shortlist top candidates.

## 🎯 Objectives
- **Automate Resume Collection**: Fetch resumes directly from Gmail inbox using email credentials.  
- **Skill Extraction**: Extract text from PDF resumes and identify relevant technical skills.  
- **Candidate Ranking**: Score and rank candidates based on the number of matched keywords.  
- **Interactive UI**: Provide a Streamlit-based interface to view matches, scores, and resume previews.  
- **Enable Shortlisting**: Help recruiters efficiently identify and preview top candidate resumes for further action.
  


## 🧠 Tech Stack / Tools Used
- **Language**: Python 🐍  
- **Libraries**: `pandas`, `pdfplumber`, `dotenv`, `streamlit`, `imaplib`, `email`, `os`, `re`  
- **IDE/Editor**: VS Code 💻  
- **File Formats**: `.pdf`, `.csv`, `.env`  
- **Optional**: Streamlit for app demo 🌐

### 📂 Project Structure
<pre> ```
📁 resume-keyword-extractor/
├── 📁 data/
│   ├── 📁 raw/                     – Raw dataset for database model
│   └── 📁 processed/               – Cleaned/parsed resumes (PDF to text)
├── 📁 outputs/
│   └── 📄 ranked_candidates.csv    – Final ranked candidate results
├── 📁 src/
│   ├── 📄 extract_keywords.py      – Extracts matching keywords from resumes
│   ├── 📄 main.py                  – Scoring and screening logic
│   ├── 📄 resume_parser.py         – Extracts text, cleans and tokenizes
│   ├── 📄 skills_keywords.py       – Keywords used for matching
│   └── 📄 fetch_resumes_email.py   – Extracts PDFs from Gmail
├── 📁 app/                         – (Optional) Streamlit app files
├── 📄 README.md                    – Project overview and instructions
├── 📄 sample.env.json              – Sample configuration file
└── 📄 requirements.txt             – Python dependencies
 ``` </pre>

## 📈 Results & Screenshots
[🎥 Demo Video 1](outputs/Demo%20Video/Resume%20Keyword%20Extractor%20-%20Google%20Chrome%202025-07-17%2013-24-58.mp4)  
[🎥 Demo Video 2](outputs/Demo%20Video/main.py%20-%20resume-keyword-extractor%20-%20Visual%20Studio%20Code%202025-07-17%2013-10-28%20(online-video-cutter.com).mp4)



## 🗒️ Learnings
- Learned how to connect and authenticate Gmail using the `imaplib` and `email` libraries securely via `.env` and `st.secrets`.  
- Gained hands-on experience in parsing PDF resumes using **PyMuPDF** to extract clean and accurate text content.  
- Implemented **keyword-based matching logic** to filter resumes based on required tech skills.  
- Explored **Streamlit** to create an interactive UI with preview buttons, file download options, and a user-friendly layout.  
- Understood the importance of handling **secure credentials**, practicing **git hygiene** with `.gitignore`, and **separating config from logic**.

## 📦 How to Run
```bash
# Step 1: Clone the repo
git clone https://github.com/careerbytecode/ai-ml-3-month-internship.git

# Step 2: Navigate to this project folder
cd ProjectXX-Your-Project-Title

# Step 3: Create virtual environment & activate
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Step 4: Install dependencies
pip install -r requirements.txt

# Step 5: Run your script or notebook
python src/model.py

---
🧑‍💻 _Project done as part of CareerByteCode's AI/ML Internship Program_ 🔥
