# 📝 Zadanie: Budowanie indeksu ofert mieszkań z Wrocławia i dokeryzacja aplikacji

Twoim zadaniem jest przygotowanie aplikacji, która:

1. Pobierze i zapisze opisy mieszkań z portalu **Adresowo** (dla lokalizacji Wrocław).
2. Zbuduje **indeks wektorowy** na podstawie pobranych ofert.
3. Udostępni prostą **wyszukiwarkę RAG** w Gradio, działającą w kontenerze Dockera.

---

## 🔹 Krok 1. Scraping danych

Plik `scrape_adresowo.py` odpowiada za pobranie danych ofert i zapisanie ich do pliku CSV.
Twoim zadaniem jest:

* zmiana adresu bazowego na **Wrocław**:

  ```python
  BASE_LIST_URL = "https://adresowo.pl/mieszkania/wroclaw/_l{}"
  ```
* uruchomienie skryptu i wygenerowanie pliku `adresowo_offers_detail.csv`.

---

## 🔹 Krok 2. Budowanie plików tekstowych

Plik `build_files.py` tworzy pliki `.txt` z opisami mieszkań.

* uruchom go, aby zapisać dane do folderu `adresowo_descriptions/`.

---

## 🔹 Krok 3. Budowanie indeksu

Plik `build_vectorstore.py` wektoryzuje opisy przy użyciu **SentenceTransformers (MiniLM-L6-v2)** i zapisuje wektorową bazę do `./chroma_index`.

* uruchom skrypt i sprawdź w logach liczbę chunków i dokumentów.

---

## 🔹 Krok 4. Wyszukiwarka w Gradio

Plik `app.py` uruchamia prostą wyszukiwarkę ofert zbudowaną w oparciu o ChromaDB.

* interfejs Gradio działa na porcie `7860`,
* możesz wpisać zapytanie np. *„2 pokoje blisko centrum Wrocławia”* i zobaczyć dopasowania.

---

## 🔹 Krok 5. Dokeryzacja

Przygotuj `Dockerfile` dla aplikacji (np. dla `app.py`):

---

## 🔹 Krok 6. Orkiestracja w `docker-compose.yml`

Dodaj do istniejącego `docker-compose.yml` serwis aplikacji:



---

## 🔹 Krok 7. Zadania do wykonania

1. Zbuduj i uruchom serwis:
