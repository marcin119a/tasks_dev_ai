
---

## 1. Zbuduj nowy image w oparciu o stary kod z tego folderu

Na swojej maszynie (w katalogu z `Dockerfile`): 

```bash
docker build -t your-dockerhub-user/offers-api:v2 .
docker push your-dockerhub-user/offers-api:v2
```


---

## 2. Przygotowanie Yaml's 


---

## 3. Deployment na nowym obrazie

`deployment.yaml`:

---

## 4. Service (NodePort żeby minikube działał)

`service.yaml`:
---

## 5. Apply

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

---

## 6. Sprawdź dostęp

```bash
minikube service offers-api-service
```

albo bezpośrednio:

```
http://$(minikube ip):30080
```

---

Dodatkowe rozszerzenie: 

🧑‍💻 Zadanie: Job do trenowania modelu + FastAPI API
Cel

* Job jednorazowo trenuje model ML i zapisuje model.pkl w PersistentVolumeClaim (PVC),
* FastAPI serwis montuje ten sam PVC i używa modelu do predykcji.