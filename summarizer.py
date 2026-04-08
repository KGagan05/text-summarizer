from transformers import pipeline

# Load model once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):

    # Limit input length (important)
    text = text[:1000]

    summary = summarizer(
        text,
        max_length=120,
        min_length=30,
        do_sample=False
    )

    return summary[0]['summary_text']