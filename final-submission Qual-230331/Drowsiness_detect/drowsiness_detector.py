from sklearn.ensemble import RandomForestClassifier
import numpy as np

class DrowsinessDetector:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.is_trained = False

    def train(self, X, y):
        self.model.fit(X, y)
        self.is_trained = True

    def predict(self, ear):
        if not self.is_trained:
            raise Exception("Model is not trained yet")
        return self.model.predict(np.array([ear]).reshape(1, -1))[0]