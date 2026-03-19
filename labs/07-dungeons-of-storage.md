# Лаб 07. Сокровищница данных

## Цель

Подключить хранилище к приложению.

## Команды

```bash
kubectl apply -f manifests/06-storage/quest-board-pvc.yaml
kubectl apply -f manifests/06-storage/quest-board-storage-deployment.yaml
kubectl rollout status deployment/quest-board -n adventure
kubectl exec -n adventure deploy/quest-board -- sh -c 'echo \"session one\" >> /data/party.log && cat /data/party.log'
```

## Что заметить

- приложение видит каталог `/data`;
- заметки живут вне файловой системы контейнера.

