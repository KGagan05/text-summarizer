import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

def summarize_text(text):

    sentences = sent_tokenize(text)

    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))

    word_freq = {}

    for word in words:
        if word.isalnum() and word not in stop_words:
            word_freq[word] = word_freq.get(word, 0) + 1

    sentence_scores = {}

    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_freq:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_freq[word]

    # Pick top 3 sentences
    summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:3]

    return " ".join(summary)
