# Zadanie: API Predykcji Cen Mieszkań z FastAPI i Machine Learning

## Opis projektu
Celem zadania jest stworzenie API do predykcji cen mieszkań we Wrocławiu z wykorzystaniem FastAPI, SQLAlchemy, i modelu uczenia maszynowego (Linear Regression). Projekt obejmuje bazę danych, endpoints RESTful, oraz integrację z modelem ML.

## Wymagania wstępne
- Python 3.8+
- Podstawowa znajomość FastAPI
- Podstawowa znajomość SQL i SQLAlchemy
- Podstawowa znajomość sklearn

## Krok 1: Przygotowanie środowiska

### 1.1 Utworzenie struktury projektu

### 1.2 Utworzenie wirtualnego środowiska

### 1.3 Utworzenie pliku requirements.txt
```txt
pandas
numpy
scikit-learn
fastapi
uvicorn
sqlalchemy
pydantic
httpx
```

### 1.4 Instalacja zależności pip install -r requirements.txt
 

## Krok 2: Konfiguracja bazy danych

### 2.1 Utworzenie pliku database.py

### 2.2 Utworzenie modeli danych (models.py)


## Krok 3: Implementacja modelu ML

### 3.1 Przygotowanie danych (data/adresowo_wroclaw_all.csv)
Plik CSV powinien zawierać kolumny:
- `locality` - dzielnica
- `rooms` - liczba pokoi
- `area_m2` - powierzchnia w m²
- `price_total_zl` - cena całkowita w PLN

### 3.2 Utworzenie modułu ML (ml.py)

## Krok 4: Implementacja API
* Predykcja modelu liniowego dla cech:

```python
  offer.rooms, offer.area_m2, offer.photos, offer.locality, offer.street, offer.property_type, offer.city
```
### 4.1 Utworzenie głównego pliku aplikacji (main.py)

## Krok 5: Uruchomienie aplikacji

### 6.1 Uruchomienie serwera deweloperskiego
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 6.2 Dostęp do dokumentacji API
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Krok 7: Testowanie API

### 7.1 Przykładowe zapytania curl
```bash
# Predykcja ceny
curl -X POST "http://localhost:8000/predict/" \
     -H "Content-Type: application/json" \
     -d '{"area_m2": 50.0, "rooms": 2}'

# Dodanie oferty
curl -X POST "http://localhost:8000/offers/" \
     -H "Content-Type: application/json" \
     -d '{"locality": "Warszawa Centrum", "rooms": 2, "area_m2": 50.0, "description": "Ładne mieszkanie"}'

# Pobranie ofert
curl -X GET "http://localhost:8000/offers/"

# Statystyki
curl -X GET "http://localhost:8000/offers/stats/summary"
```

## Krok 8: Rozszerzenia (opcjonalne)

### 8.1 Dodatkowe endpointy
- `POST /offers/{offer_id}` - aktualizacja oferty
- `POST /offers/{offer_id}` - usuwanie oferty
- `GET /model/info` - informacje o modelu ML
- `POST /model/retrain` - ponowne trenowanie modelu

## Struktura finalnego projektu
```
FastAPIProject/
├── main.py              # Główna aplikacja FastAPI
├── models.py            # Modele danych
├── database.py          # Konfiguracja bazy danych
├── ml.py               # Moduł machine learning
├── test_main.py        # Testy
├── requirements.txt    # Zależności
├── data/
│   └── adresowo_wroclaw_all.csv  # Dane treningowe
├── offers.db          # Baza danych SQLite
├── model.pkl          # Wytrenowany model ML
└── ZADANIE.md         # Ten dokument
```
