import streamlit as st
import sys, os, pandas as pd

# 📁 Ensure folder structure exists
for folder in ["data/raw", "data/processed", "outputs/graphs"]:
    os.makedirs(folder, exist_ok=True)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_loader import fetch_transcript
from src.utils import clean_text
from src.model import summarize_text

# 🌐 App UI
st.set_page_config(page_title="YouTube Transcript Summarizer", page_icon="🎥")
st.title("📺 YouTube Transcript Summarizer")
st.markdown("Paste a YouTube video link or ID to get an instant summary of the transcript!")

# 🎯 Input
video_input = st.text_input("🔗 Enter YouTube Video URL or ID:")
summary_length = st.radio("📏 Choose summary length", ["short", "medium", "long"], index=1)

# 🔍 Extract video ID
def extract_video_id(url_or_id: str) -> str:
    if "watch?v=" in url_or_id:
        return url_or_id.split("watch?v=")[-1][:11]
    if "youtu.be/" in url_or_id:
        return url_or_id.split("youtu.be/")[-1][:11]
    return url_or_id.strip()[:11]

# 🎬 Process
if video_input:
    video_id = extract_video_id(video_input)
    transcript_path = fetch_transcript(video_id)

    if transcript_path and os.path.exists(transcript_path):
        with open(transcript_path, encoding="utf-8") as f:
            raw_text = f.read()

        cleaned = clean_text(raw_text)
        summary = summarize_text(cleaned, length=summary_length)

        st.subheader("📝 Summary")
        st.success(summary)

        # Save result
        csv_path = "outputs/results.csv"
        row_df = pd.DataFrame([[video_id, summary]], columns=["video_id", "summary"])
        row_df.to_csv(csv_path, mode='a', header=not os.path.exists(csv_path), index=False)

        st.download_button("⬇️ Download Summary", data=summary, file_name=f"{video_id}_summary.txt", mime="text/plain")
    else:
        st.error("❌ Transcript not available or failed to fetch.")
