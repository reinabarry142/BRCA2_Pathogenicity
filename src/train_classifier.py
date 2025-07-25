def train_classifier(X_train, y_train):
    mlp = MLPClassifier(hidden_layer_sizes=(512, 128),
                        activation='relu',
                        solver='adam',
                        learning_rate_init=0.001,
                        max_iter=300,
                        batch_size=32,
                        random_state=42)
    mlp.fit(X_train, y_train)
    return mlp