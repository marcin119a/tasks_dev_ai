# **Zadanie: Analiza sentymentu + generowanie audio z użyciem Celery, Redis i SunoModel**

W tym zadaniu wykorzystasz **Celery** oraz **Redis** do uruchamiania asynchronicznych zadań, takich jak:

* **Analiza sentymentu z użyciem BERT-a**
* **Prosta klasyfikacja tekstów Adresowo (bez BERT-a)**
* **Generowanie audio z tekstu przy użyciu `suno/bark-small`**

---

## **Krok 1. Przygotowanie projektu**

Masz już gotowy projekt z **Celery** i **Redis**.

---

## **Krok 2. Zmodyfikuj kod `tasks.py`**

Twoim zadaniem jest zastąpienie dotychczasowego tłumaczenia **trzema nowymi taskami**:

1. **Analiza sentymentu (BERT)**
2. **Prosta klasyfikacja Adresowo (bez BERT-a)**
3. **Generowanie audio (Suno/Bark)**

---

## **1. Generowanie audio – Suno/Bark-Small**

Model do generowania audio z tekstu:
🔗 **Google Colab:**
[https://colab.research.google.com/drive/1I8BhvJE7XZf4F6WMxZ2dK0KHTX8IuzLl?usp=sharing](https://colab.research.google.com/drive/1I8BhvJE7XZf4F6WMxZ2dK0KHTX8IuzLl?usp=sharing)

---

## **Krok 3. Uruchom środowisko**

### **1. Zbuduj kontenery:**

```bash
docker compose build
```

### **2. Uruchom projekt:**

```bash
docker compose up
```

### **3. Sprawdź logi workera Celery:**

```bash
docker compose logs worker
```

---

## **Krok 4. Przetestuj zadania**

### **1. Generowanie audio z tekstu (`suno/bark-small`)**

```bash
curl -X POST localhost:8000/audio \
  -H "Content-Type: application/json" \
  -d '{"text": "Cześć, to jest test syntezy mowy."}'
```

### **Oczekiwany wynik:**

```json
{"audio_file": "audio_1234abcd5678ef.wav"}
```

Plik WAV zapisuje się w katalogu:

```
/data/audio
```

---

