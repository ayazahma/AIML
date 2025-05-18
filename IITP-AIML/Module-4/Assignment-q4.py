from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# List of social media posts
posts = [
    "I love this product! It works great and exceeded my expectations.",
    "Worst experience ever. Totally disappointed and angry.",
    "It's okay, nothing special. Just average.",
    "Absolutely fantastic! Highly recommend it to everyone.",
    "I hate it. Complete waste of money."
]

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def classify_sentiment(compound_score):
    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Analyze each post
for idx, post in enumerate(posts, 1):
    scores = analyzer.polarity_scores(post)
    sentiment = classify_sentiment(scores['compound'])
    print(f"Post {idx}: {post}")
    print(f"Scores: Positive={scores['pos']}, Negative={scores['neg']}, Neutral={scores['neu']}, Compound={scores['compound']}")
    print(f"Overall Sentiment: {sentiment}\n")