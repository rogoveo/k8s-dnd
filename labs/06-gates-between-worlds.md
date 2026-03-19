# Лаб 06. Открываем портал

## Цель

Сделать приложение доступным через `Ingress`.

## Команды

```bash
kubectl apply -f manifests/05-ingress/quest-board-ingress.yaml
kubectl get ingress -n adventure
curl http://localhost/
```

## Что заметить

- `Ingress` маршрутизирует HTTP-запрос к сервису;
- внешний адрес теперь не требует `port-forward`.

