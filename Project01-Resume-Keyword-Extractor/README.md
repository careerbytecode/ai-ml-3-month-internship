# 🚀 Project Title: <PROJECT_TITLE>

## 📌 Problem Statement
Recruiters face challenges in manually screening large volumes of resumes.
Identifying relevant technical skills from unstructured PDF resumes is time-consuming.
There is a need for an automated tool to extract, filter, and rank resumes efficiently.
This project fetches resumes from Gmail, matches them with required skills, and ranks them.
An interactive Streamlit interface helps recruiters preview and shortlist top candidates.

## 🎯 Objectives
-Automate Resume Collection: Fetch resumes directly from Gmail inbox using email credentials.

-Skill Extraction: Extract text from PDF resumes and identify relevant technical skills.

-Candidate Ranking: Score and rank candidates based on the number of matched keywords.

-Interactive UI: Provide a Streamlit-based interface to view matches, scores, and resume previews.

-Enable Shortlisting: Help recruiters efficiently identify and preview top candidate resumes for further action.

## 🧠 Tech Stack / Tools Used
-Python 🐍
-Libraries: pandas, pdfplumber, dotenv, streamlit, imaplib, email, os, re
-IDE/Editor: VS Code 💻
-File Formats: .pdf, .csv, .env
-(Optional) Streamlit for app demo 🌐

## 📂 Project Structure
📁 resume-keyword-extractor/
│
├── 📁 data/
│   ├── 📁 raw/                # Raw dataset for database model
│   └── 📁 processed/          # Raw resumes (PDFs) downloaded from email Cleaned or parsed text versions
│
├── 📁 outputs/
│   └── 📄 ranked_candidates.csv         # Final ranked candidate results
│
├── 📁 src/                         # Source code files
│   ├── 📄 extract_keywords.py      # The extracted matching keywords from resume
│   ├── 📄 main.py                  # Scoring and screening logic 
|   └── 📄 resume_parser.py         # Extracts text from PDFs, cleans and tokenizes
|   ├── 📄 skills_keywords.py       # Keywords to find the matching resumes
|   ├── 📄 fetch_resumes_email.py   # Extracts pdfs from mail
|    
├── 📁 app/ (optional)         # Streamlit app
│
├── 📄 README.md               # Project overview and instructions
├── 📄 sample.env.json         # Sample config for contributors
├── 📄 requirements.txt        # Python dependencies


## 📈 Results & Screenshots


## 🗒️ Learnings
-Learned how to connect and authenticate Gmail using the imaplib and email libraries securely via .env and st.secrets.
-Gained hands-on experience in parsing PDF resumes using PyMuPDF to extract clean and accurate text content.
-Implemented keyword-based matching logic to filter resumes based on required tech skills.
-Explored Streamlit for creating an interactive UI with preview buttons, file download options, and user-friendly layout.
-Understood the importance of handling secure credentials, git hygiene with .gitignore, and separating config from logic.

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
