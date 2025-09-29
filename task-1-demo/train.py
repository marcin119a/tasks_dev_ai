import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import mlflow
import pickle

def load_data(src):
    df = pd.read_csv(src)

    # Czyszczenie ceny
    df['price_total_zl'] = df['price_total_zl'].astype(str).str.replace(' ', '').str.replace(',', '')
    df['price_total_zl'] = pd.to_numeric(df['price_total_zl'], errors='coerce')

    # Usuwanie braków
    df_clean = df.dropna(subset=['rooms', 'area_m2', 'price_total_zl'])

    # Filtry sanityzujące
    df_clean = df_clean[
        (df_clean['area_m2'] > 10) &
        (df_clean['area_m2'] < 500) &
        (df_clean['price_total_zl'] > 100000) &
        (df_clean['price_total_zl'] < 5000000) &
        (df_clean['rooms'] > 0) &
        (df_clean['rooms'] <= 10)
    ]

    return df_clean

def encode_features(df):
    df_encoded = df.copy()

    # Wybór kolumn kategorycznych do zakodowania
    categorical_cols = ['locality', 'street', 'property_type', 'city']
    encoder = LabelEncoder()

    for col in categorical_cols:
        if col in df_encoded.columns:
            df_encoded[col] = encoder.fit_transform(df_encoded[col].astype(str))

    return df_encoded

def train_model(X, y):
    with mlflow.start_run():
        model = RandomForestRegressor(random_state=42)
        model.fit(X, y)

        score = model.score(X, y)
        print(f"Train R²: {score}")

        mlflow.log_param("model", "RandomForestRegressor")
        mlflow.log_metric("score", score)

        mlflow.sklearn.log_model(model, "model")
        with open("model.pkl", "wb") as f:
            pickle.dump(model, f)
    return model 

def test_model(model, X, y):
    score = model.score(X, y)
    print(f"Test R²: {score}")
    return score

if __name__ == "__main__":
    df = load_data('data/adresowo_warszawa_wroclaw.csv')
    df_encoded = encode_features(df)

    # Wybór featurów
    features = ['rooms', 'area_m2', 'photos', 'locality', 'street',
                'property_type', 'city']
    X = df_encoded[features]
    y = df_encoded['price_total_zl']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = train_model(X_train, y_train)
    test_model(model, X_test, y_test)
