from sklearn.ensemble import RandomForestClassifier


def train(X, y):

    model = RandomForestClassifier(
        n_estimators=500,
        random_state=42
    )

    model.fit(X, y)

    return model
