import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(chat_history, top_n = 5):
    messages = [dt['message'] for dt in chat_history]

    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(messages)

    feature_names = vectorizer.get_feature_names_out()
    sums = vectors.sum(axis=0)

    tfidf_scores = [(feature_names[i], sums[0, i]) for i in range(len(feature_names))]
    sorted_scores = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)

    return [kw for kw, score in sorted_scores[:top_n]]

