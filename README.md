# skyes-hello-infra

python3.11 -m venv
source env/bin/activate
pip install fastapi uvicorn

uvicorn main:app --reload

http://localhost:8000/hello or http://127.0.0.1:8000/schedule/<input_data string>

http://localhost:8000/docs

docker-compose build

Upload to gcr

Install Minikube

minikube start
minikube kubectl -- get po -A
minikube kubectl -- apply -f deployment.yaml
minikube kubectl -- apply -f service.yaml
minikube kubectl -- port-forward service/skyes-rest-api 8080:8080
minikube kubectl -- delete deployment skyes-rest-api

kubectl get pods -A
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl port-forward service/skyes-rest-api 8080:8080
kubectl delete deployment skyes-rest-api