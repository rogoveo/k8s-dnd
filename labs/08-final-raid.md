# Лаб 08. Финальный рейд

## Цель

Собрать собственное приложение и полностью развернуть его в `kind`.

## Команды

```bash
docker build -t quest-board:local ./demo-app
kind load docker-image quest-board:local --name k8s-dnd
kubectl apply -f manifests/04-config/quest-board-configmap.yaml
kubectl apply -f manifests/04-config/quest-board-secret.yaml
kubectl apply -f manifests/06-storage/quest-board-pvc.yaml
kubectl apply -f manifests/07-final/
kubectl rollout status deployment/quest-board -n adventure
curl http://localhost/
```

## Финальная проверка

```bash
kubectl get all -n adventure
kubectl exec -n adventure deploy/quest-board -- sh -c 'ls -la /data && cat /data/party.log || true'
```

