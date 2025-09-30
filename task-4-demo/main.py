from pathlib import Path
import pickle

model_path = Path("artifacts/model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

print(model)