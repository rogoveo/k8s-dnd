# Лаб 04. Строим дороги

## Цель

Подключиться к приложению через `Service`.

## Команды

```bash
kubectl apply -f manifests/03-service/quest-board-service.yaml
kubectl get svc,endpoints -n adventure
kubectl port-forward svc/quest-board 8080:80 -n adventure
```

Во втором терминале:

```bash
curl http://localhost:8080/
```

## Что заметить

- у сервиса есть стабильное имя `quest-board`;
- реальные `Pod` могут меняться, сервис остается.
