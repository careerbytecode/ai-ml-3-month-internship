from youtube_transcript_api import YouTubeTranscriptApi
import os

def fetch_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([entry['text'] for entry in transcript])

        # Save raw transcript
        os.makedirs("data/raw", exist_ok=True)
        path = f"data/raw/{video_id}.txt"
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        return path
    except Exception as e:
        print(f"[Error] Could not fetch transcript: {e}")
        return None
