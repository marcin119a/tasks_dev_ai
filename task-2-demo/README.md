# Zadanie: API Predykcji Cen Mieszkań z FastAPI i Machine Learning

## Opis projektu
Celem zadania jest stworzenie API do predykcji cen mieszkań w Łodzi z wykorzystaniem FastAPI, SQLAlchemy, i modelu uczenia maszynowego. Projekt obejmuje bazę danych, endpoints RESTful, oraz integrację z modelem ML.

## Wymagania wstępne
- Python 3.8+
- Podstawowa znajomość FastAPI
- Podstawowa znajomość SQL i SQLAlchemy
- Podstawowa znajomość sklearn

## Krok 1: Przygotowanie środowiska

### 1.1 Utworzenie struktury projektu

### 1.2 Utworzenie wirtualnego środowiska

### 1.3 Utworzenie pliku requirements.txt


### 1.4 Instalacja zależności pip install -r requirements.txt
 
## Krok 2: Konfiguracja bazy danych

### 2.1 Utworzenie pliku db/database.py

### 2.2 Utworzenie modeli danych (db/models.py)


## Krok 3: Implementacja modelu ML

### 3.1 Przygotowanie danych (data/adresowo_lodz_all.csv)

## Krok 4: Implementacja API
* Predykcja modelu liniowego dla cech zdefiniowanych:

## Krok 5: Uruchomienie aplikacji

### 6.1 Uruchomienie serwera deweloperskiego
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 6.2 Dostęp do dokumentacji API
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Krok 7: Testowanie API

Przygotuj testy API z użyciem  http://localhost:8000/docs

## Krok 8: Rozszerzenia

### 8.1 Dodatkowe endpointy
- `POST /model/retrain` - ponowne trenowanie modelu
- `GET /model/info` - informacje o modelu ML

