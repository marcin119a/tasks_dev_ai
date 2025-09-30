## Zadanie: Trening i monitorowanie modelu regresji liniowej w MLflow

**Cel:**
Nauczyć się trenować prosty model ML (regresja liniowa), logować parametry i metryki w **MLflow**, a następnie testować działanie modelu na przykładowych danych.

---

### Przygotowanie środowiska venv

1. Upewnij się, że masz zainstalowane biblioteki:

   ```bash
   pip install mlflow scikit-learn pandas
   ```
2. Uruchom lokalnie MLflow Tracking Server:

   ```bash
   mlflow ui
   ```

   Następnie wejdź w przeglądarce na `http://127.0.0.1:5000`.

---

### Zadania do wykonania

#### Część A: Trening modelu

* Użyj danych wejściowych `area_m2` oraz `rooms` do przewidywania ceny mieszkania (`price_total_zl`).
* Wytrenuj model regresji liniowej (`LinearRegression`).
* Zaloguj do MLflow:

  * parametry (np. użyte cechy, liczba próbek),
  * metryki (`r2`, współczynniki regresji, wyraz wolny),
  * sam model.

#### Część B: Zapis i wczytanie modelu

* Zapisz model zarówno lokalnie w pliku `model.pkl`, jak i do MLflow (`mlflow.sklearn.log_model`).
* Napisz funkcję `load_model()`, która:

  * sprawdza, czy model istnieje lokalnie,
  * jeśli nie, trenuje go od nowa.

#### Część C: Predykcje

* Napisz funkcję `predict_price(area_m2, rooms)`, która przewiduje cenę na podstawie trenowanego modelu.
* Sprawdź model na przykładowych danych:

  * 50 m², 2 pokoje
  * 70 m², 3 pokoje
  * 30 m², 1 pokój
  * 100 m², 4 pokoje

#### Część D: Analiza wyników

* Uruchom MLflow UI i sprawdź:

  * jakie wartości miały współczynniki modelu,
  * jak zmieniały się metryki,
  * czy zapisany model da się pobrać i użyć ponownie.

---

### Rozszerzenie (dla chętnych)

* Dodaj dodatkowe cechy do modelu (np. lokalizacja mieszkania).
* Zmień model na `RandomForestRegressor` i porównaj wyniki.
* Uruchom **eksperymenty z różnymi hiperparametrami** (np. liczba epok, batch_size) i porównaj je w MLflow.

---

**Efekt końcowy**:
Masz model regresji liniowej, którego wyniki są **reprodukowalne i śledzone w MLflow**, z możliwością przewidywania cen mieszkań na podstawie powierzchni i liczby pokoi.