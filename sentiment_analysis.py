from transformers import pipeline

def sentiment_analysis(texts):
    classifier = pipeline('sentiment-analysis')
    return [classifier(text) for text in texts]

# Analyze sentiments of gathered articles...
