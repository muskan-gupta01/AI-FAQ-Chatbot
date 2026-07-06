import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

# Download stopwords only once
nltk.download("stopwords", quiet=True)

# English stopwords
stop_words = set(stopwords.words("english"))

# Tokenizer
tokenizer = RegexpTokenizer(r"\w+")


def preprocess(text):
    """
    Clean and preprocess text
    """

    text = str(text).lower()

    words = tokenizer.tokenize(text)

    words = [
        word
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)