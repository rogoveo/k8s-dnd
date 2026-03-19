# Лаб 05. Загружаем свитки и секреты

## Цель

Отделить конфигурацию от кода приложения.

## Команды

```bash
kubectl apply -f manifests/04-config/quest-board-configmap.yaml
kubectl apply -f manifests/04-config/quest-board-secret.yaml
kubectl apply -f manifests/04-config/quest-board-configured-deployment.yaml
kubectl rollout status deployment/quest-board -n adventure
kubectl port-forward svc/quest-board 8080:80 -n adventure
```

Во втором терминале:

```bash
curl http://localhost:8080/
```

## Что заметить

- контент страницы меняется без пересборки образа;
- `Secret` не печатается как есть, приложение показывает только факт его наличия.

