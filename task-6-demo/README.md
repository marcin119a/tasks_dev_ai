Zadanie: Analiza sentymentu + generowanie audio z użyciem BERT-a, Celery, Redis i SunoModel

W tym zadaniu wykorzystasz Celery oraz Redis do uruchamiania asynchronicznych zadań, takich jak:

Analiza sentymentu z użyciem BERT-a

Prosta klasyfikacja tekstów Adresowo (bez BERT-a)

Generowanie audio z tekstu przy użyciu suno/bark-small

Krok 1. Przygotowanie projektu

Masz już gotowy projekt z Celery i Redis.

Krok 2. Zmodyfikuj kod tasks.py

Twoim zadaniem jest zastąpienie obecnego tłumaczenia trzema taskami:

analiza sentymentu (BERT)

prosta klasyfikacja Adresowo (bez BERT-a)

generowanie audio (Suno/Bark)





# -------------------------
# 1. GENEROWANIE AUDIO – SUNO/BARK-SMALL
# -------------------------

# ładowanie modelu bark-small: https://colab.research.google.com/drive/1I8BhvJE7XZf4F6WMxZ2dK0KHTX8IuzLl?usp=sharing

Krok 3. Uruchom środowisko

Zbuduj kontenery:

docker compose build


Uruchom projekt:

docker compose up


Sprawdź logi workera Celery:

docker compose logs worker

Krok 4. Przetestuj zadania

1. Generowanie audio z tekstu (suno/bark-small)
curl -X POST localhost:8000/audio \
  -H "Content-Type: application/json" \
  -d '{"text": "Cześć, to jest test syntezy mowy."}'


Oczekiwany wynik:

{"audio_file": "audio_1234abcd5678ef.wav"}


Plik WAV zapisuje się w /data/audio.

## Zadanie dodatkowe (rozszerzone)

Zaimplementuj endpoint, który:

przyjmuje tekst
generuje audio

