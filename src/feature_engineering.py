from sklearn.feature_extraction.text import TfidfVectorizer


def build_features(texts):

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=5000,
        ngram_range=(1,2)
    )

    X = vectorizer.fit_transform(texts)

    return X, vectorizer
