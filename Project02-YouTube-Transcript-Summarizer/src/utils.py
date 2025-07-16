import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Download once
nltk.download('punkt')
nltk.download('stopwords')

def clean_text(text):
    # Lowercase
    text = text.lower()

    # Remove timestamps/special characters
    text = re.sub(r'\[.*?\]|\(.*?\)', '', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Remove stopwords
    words = word_tokenize(text)
    filtered_words = [w for w in words if w not in stopwords.words('english')]

    return ' '.join(filtered_words)
