import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

data = pd.DataFrame({
    "rainfall": [20, 30, 45, 55, 70, 85, 100, 120, 140, 160],
    "slope": [5, 8, 12, 15, 18, 22, 25, 30, 35, 40],
    "risk": [
        "LOW", "LOW", "LOW",
        "MEDIUM", "MEDIUM", "MEDIUM",
        "HIGH", "HIGH", "HIGH", "HIGH"
    ]
})

X = data[["rainfall", "slope"]]
y = data["risk"]

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

joblib.dump(model, "landslide_model.pkl")

print("SlopeWatch ML model trained successfully!")
