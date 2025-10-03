set -e

python train.py

docker build -t offers-api:latest .

kubectl apply -f k8s/pvc.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
#kubectl apply -f k8s/job-train-model.yamlml


