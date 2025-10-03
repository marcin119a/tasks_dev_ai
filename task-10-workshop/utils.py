import pickle
from train import encode_features
import pandas as pd
from train import FEATURES

def load_model():
    model_path = "model.pkl"
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model


def predict_price(area_m2: float, rooms:int, photos:int, locality:str, street:str, property_type:str, city:str):
    """Predykcja ceny mieszkania na podstawie jego powierzchni i liczby pokoi"""

    df = pd.DataFrame([[rooms, area_m2, photos, locality, street, property_type, city]], columns=FEATURES)
    model = load_model()
    encoded_data = encode_features(df)


    return model.predict(encoded_data)[0]

    