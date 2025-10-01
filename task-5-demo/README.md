
# 📝 Zadanie: Postawienie drugiego Gradio z mniejszym Whisperem

Masz już usługę `whisper-gradio` z modelem **Whisper Small**.
Dodaj teraz **drugą usługę** w `docker-compose.yml`, która uruchamia **Whisper Tiny**.

---

## 1. Zmodyfikuj `app.py`

Dodaj nowy plik np. `app_tiny.py` z pipeline dla mniejszego modelu:

Uwaga: ustaw port na **7861**, żeby nie kolidował z 7860.

---

## 2. Uaktualnij `docker-compose.yml`

Dodaj nową usługę ```whisper-gradio-tiny```:
---

## 3. Uruchom serwisy

```bash
docker compose up --build
```

---

##  4. Przetestuj w przeglądarce prez https://sages.link/guacamole/#/

* Whisper Small [http://localhost:7860](http://localhost:7860)
* Whisper Tiny [http://localhost:7861](http://localhost:7861)

---

## 5. Test

1. Wgraj ten sam plik audio do obu interfejsów.

   * zmierz czas transkrypcji,
   * porównaj dokładność wyników.

2. Otwórz w terminalu:

   ```bash
   docker stats
   ```

   * zobacz, ile CPU/RAM zużywa Whisper Small,
   * a ile Whisper Tiny.

---