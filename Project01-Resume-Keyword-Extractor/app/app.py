import streamlit as st
import pandas as pd
import os
import base64

# --- Page Config ---
st.set_page_config(page_title="Resume Keyword Extractor", layout="centered")
st.title("📄 Resume Keyword Extractor Results")

# --- Helper: PDF Preview Renderer ---
def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="500" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# --- Load and Prepare Data ---
try:
    df = pd.read_csv("ranked_candidates.csv")
except FileNotFoundError:
    st.error("❌ CSV file not found. Please ensure 'ranked_candidates.csv' is generated.")
    st.stop()

df['Resume'] = df['Resume'].apply(lambda path: os.path.basename(str(path)))
df = df.sort_values(by='Score', ascending=False).reset_index(drop=True)

# --- Full Table ---
with st.expander("📊 Show All Candidates and Scores"):
    st.dataframe(df)

# --- Top 5 Section ---
st.markdown("## 🏅 Top 5 Ranked Candidates")

top_5 = df.head(5)
for idx, row in top_5.iterrows():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"### {idx+1}. {row['Resume']}")
        st.markdown(f"**✅ Matched Skills:** {row['Matched Keywords']}")
        st.markdown(f"**📊 Score:** {row['Score']}")
    with col2:
        preview_button = st.button("👁 Show Preview", key=f"preview_{idx}")

    resume_path = os.path.join("data", row['Resume'])

    if preview_button:
        if os.path.exists(resume_path):
            st.markdown("#### 📝 Resume Preview")
            show_pdf(resume_path)

            with open(resume_path, "rb") as f:
                st.download_button("⬇️ Download Resume", f, file_name=row['Resume'], key=f"download_{idx}")
        else:
            st.warning("⚠️ Resume file not found.")
    
    st.markdown("---")
