from transformers import pipeline

# Load the summarization model only once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, length="medium"):
    if not text or len(text.split()) < 20:
        return text

    length_map = {
        "short": (30, 60),   # min, max tokens
        "medium": (60, 120),
        "long": (120, 200)
    }

    min_len, max_len = length_map.get(length, (60, 120))

    # Limit input to max 1024 tokens (model limit)
    if len(text) > 3500:
        text = text[:3500]

    summary = summarizer(text, min_length=min_len, max_length=max_len, do_sample=False)[0]['summary_text']
    return summary
