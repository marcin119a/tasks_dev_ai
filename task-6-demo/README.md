# Zadanie: Analiza sentymentu z użyciem BERT-a, Celery i Redis

W tym zadaniu wykorzystasz **kolejkę zadań Celery** oraz **brokera Redis**, aby uruchomić asynchroniczną analizę sentymentu na tekście.
Zamiast tłumaczenia (pipeline `"translation_en_to_de"`), będziesz używać **pipeline `"sentiment-analysis"`** z modelu BERT.

---

## Krok 1. Przygotowanie projektu

Masz już gotowy projekt z Celery i Redis.
---

## Krok 2. Zmodyfikuj kod `tasks.py`

Twoim zadaniem jest zastąpienie obecnego tłumaczenia tekstu nową funkcją, która wykonuje **analizę sentymentu** przy użyciu BERT-a.

Zaimplementuj nową funkcję.

---

## Krok 3. Uruchom środowisko

1. Zbuduj obrazy:

   ```bash
   docker compose build
   ```

2. Uruchom wszystkie usługi:

   ```bash
   docker compose up
   ```

3. Sprawdź logi workera:

   ```bash
   docker compose logs worker
   ```

Powinieneś zobaczyć, że worker Celery wystartował i czeka na zadania.

---

## Krok 4. Przetestuj zadanie

Uruchom odpowiedni curl do przetestowania zadania. 

Oczekiwany wynik:

```json
{"label": "POSITIVE", "score": 0.9992}
```

---

## Zadanie dodatkowe: 
Twoim zadaniem jest wykorzystanie modelu z W&B, która wykonuje **klasyfikacje tekstu dla adresowo.pl** przy użyciu BERT-a.

* Uruchom berta z naszego W&B fine-tuningowego na tekstach z adresowo.pl. 