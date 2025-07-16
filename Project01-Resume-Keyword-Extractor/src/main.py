import os
import pandas as pd
import streamlit as st

from resume_parser import extract_text_from_file, extract_keywords
from skills_keywords import skill_keywords
from fetch_resumes_email import fetch_resumes

# Securely load Gmail credentials
if "EMAIL" in st.secrets:
    EMAIL = st.secrets["EMAIL"]
    APP_PASSWORD = st.secrets["APP_PASSWORD"]
else:
    from dotenv import load_dotenv
    load_dotenv()
    EMAIL = os.getenv("EMAIL")
    APP_PASSWORD = os.getenv("APP_PASSWORD")

# Step 1: Fetch resumes from Gmail
print("📥 Fetching resumes from email...")
fetch_resumes(EMAIL, APP_PASSWORD)  # pass credentials to fetch_resumes()

# Step 2: Define resume folder
data_folder = os.path.join(os.getcwd(), "data")
results = []

if not os.path.exists(data_folder):
    print("📂 'data' folder not found. No resumes to process.")
    exit()

# Step 3: Parse resumes and score
pdf_files = [file for file in os.listdir(data_folder) if file.endswith(".pdf")]

if not pdf_files:
    print("📭 No PDF resumes found in 'data/' folder.")
    exit()

for file in pdf_files:
    filepath = os.path.join(data_folder, file)
    text = extract_text_from_file(filepath)
    if not text:
        print(f"⚠️ Skipped empty or unreadable file: {file}")
        continue

    matched_keywords = extract_keywords(text, skill_keywords)
    score = len(matched_keywords)

    results.append({
        "Resume": file,
        "Matched Keywords": ", ".join(matched_keywords),
        "Score": score
    })

# Step 4: Sort and save results
results = sorted(results, key=lambda x: x["Score"], reverse=True)
df = pd.DataFrame(results)
df.to_csv("ranked_candidates.csv", index=False)

# Step 5: Display results
for rank, res in enumerate(results, start=1):
    print(f"🏅 Rank {rank}: {res['Resume']}")
    print(f"   ✅ Matched Skills: {res['Matched Keywords']}")
    print(f"   📊 Score: {res['Score']}\n")

print("📁 Results saved to ranked_candidates.csv")
