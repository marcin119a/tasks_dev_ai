# Zadanie: Wdrożenie i testowanie serwisu predykcyjnego (ml-predictor)

### Kontekst

Masz już skonfigurowane środowisko w `docker-compose.yml`, które zawiera:

* **mlflow** – serwer MLflow do monitorowania eksperymentów,
* **ml-trainer** – komponent trenujący model i zapisujący go jako `model.pkl`.

Twoim zadaniem jest **uruchomić i przetestować kontener `ml-predictor`**, który korzysta z wytrenowanego modelu i umożliwia wykonywanie predykcji.

---

### Krok 1. Analiza konfiguracji `ml-predictor`


* Montuje lokalny model `model.pkl` do kontenera,
* Uruchamia plik `main.py`,
* Jest podłączony do tej samej sieci co inne usługi.

---

### Krok 2. Implementacja `main.py`

1. W pliku `main.py` przygotuj prostą aplikację (**FastAPI**), która:

   * ładuje model z `model.pkl`,
   * wystawia endpoint `/predict`,
   * przyjmuje dane w formacie JSON i zwraca przewidywaną etykietę.


---

### Krok 3. Uruchomienie kontenera

Uruchom tylko profil `prediction`:

```bash
docker compose --profile prediction up --build
```

---

### Krok 4. Testowanie API

1. Sprawdź, czy API działa:

---

### Podsumowanie

1. Zaimplementuj plik `main.py` tak, aby poprawnie ładował model i wystawiał API.
2. Uruchom `ml-predictor` i przetestuj predykcje lokalnie.
3. (Dla chętnych) Dodaj obsługę logowania wyników predykcji do **MLflow**, aby śledzić, jakie dane i predykcje zostały wykonane.

---

