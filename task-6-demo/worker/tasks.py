from celery import Celery
from transformers import pipeline

celery = Celery(
    "tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

# Ładowanie modelu tłumaczenia
translator = pipeline("translation_en_to_de")

@celery.task(name="tasks.translate_text")
def translate_text(text: str):
    result = translator(text)
    return result[0]["translation_text"]