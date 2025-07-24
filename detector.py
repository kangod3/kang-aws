# ml_detector.py
import joblib
from sklearn.ensemble import IsolationForest

# 훈련 예제 (한 번만 하면 됨)
def train_model(command_list):
    from sklearn.feature_extraction.text import TfidfVectorizer
    vec = TfidfVectorizer()
    X = vec.fit_transform(command_list)
    model = IsolationForest()
    model.fit(X)
    joblib.dump((vec, model), "model.pkl")

# 예측
def predict(command):
    vec, model = joblib.load("model.pkl")
    X = vec.transform([command])
    pred = model.predict(X)
    return pred[0] == -1  # -1: 이상, 1: 정상
