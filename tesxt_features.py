#NLP feature engineering
from sklearn.feature_extraction.text import TfidfVectorizer

def build_features(texts):

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1,3),
        min_df=2
    )

    X = vectorizer.fit_transform(texts)

    return X, vectorizer
