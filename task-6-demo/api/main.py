from fastapi import FastAPI
from pydantic import BaseModel
from celery import Celery

app = FastAPI()

# Celery z Redisem
celery = Celery(
    "tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

class TextIn(BaseModel):
    text: str

@app.post("/translate")
def translate(req: TextIn):
    task = celery.send_task("tasks.translate_text", args=[req.text])
    return {"task_id": task.id, "status": "processing"}


@app.get("/result/{task_id}")
def get_result(task_id: str):
    task = celery.AsyncResult(task_id)
    if task.state == "PENDING":
        return {"status": "pending"}
    elif task.state == "SUCCESS":
        return {"status": "done", "result": task.result}
    else:
        return {"status": task.state}