import pandas as pd
from sklearn.linear_model import LinearRegression
import mlflow
import pickle
from sklearn.model_selection import train_test_split

def load_data(src):
  df = pd.read_csv(src)

  df_clean = df.dropna(subset=['rooms', 'area_m2', 'price_total_zl'])
  df_clean['price_total_zl'] = df_clean['price_total_zl'].astype(str).str.replace(' ', '').str.replace(',', '')
  df_clean['price_total_zl'] = pd.to_numeric(df_clean['price_total_zl'], errors='coerce')
  df_clean = df_clean.dropna(subset=['price_total_zl'])

  df_clean = df_clean[
        (df_clean['area_m2'] > 10) &  # minimum 10 m²
        (df_clean['area_m2'] < 500) &  # maximum 500 m²
        (df_clean['price_total_zl'] > 100000) &  # minimum 100k PLN
        (df_clean['price_total_zl'] < 5000000) &  # maximum 5M PLN
        (df_clean['rooms'] > 0) &  # at least 1 room
        (df_clean['rooms'] <= 10)  # maximum 10 rooms
    ]

  return df_clean

def train_model(X, y):
    with mlflow.start_run():
        model = LinearRegression()
        model.fit(X, y)

        score = model.score(X, y)
        print(f"Model score: {score}")
        print(f"Model coefficients: {model.coef_}")
        print(f"Model intercept: {model.intercept_}")

        mlflow.log_param("model", "LinearRegression")
        mlflow.log_param("score", score)
        mlflow.log_param("coefficients", model.coef_)
        mlflow.log_param("intercept", model.intercept_)

        mlflow.sklearn.log_model(model, "model")
        with open("model.pkl", "wb") as f:
            pickle.dump(model, f)
    return model 

def test_model(model, X, y):
    score = model.score(X, y)
    print(f"Model score: {score}")
    print(f"Model coefficients: {model.coef_}")
    print(f"Model intercept: {model.intercept_}")
    return score

if __name__ == "__main__":
    df = load_data('data/adresowo_warszawa_wroclaw.csv')
    X_train, X_test, y_train, y_test = train_test_split(df[['rooms', 'area_m2']], df['price_total_zl'], test_size=0.2, random_state=42)
    model = train_model(X_train, y_train)
    test_model(model, X_test, y_test)