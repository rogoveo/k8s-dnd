# 08. Финальный рейд

## Сюжет

Теперь вы не просто ученик, а мастер экспедиции. Ваша задача - собрать собственный артефакт, перенести его в королевство и открыть таверну приключенцев для всех жителей.

## Что это в мире D&D

Это финальный штурм цитадели, где все освоенные механики работают вместе.

## Что это в Kubernetes

Вы соединяете:

- Docker-образ;
- `Deployment`;
- `Service`;
- `ConfigMap`;
- `Secret`;
- `Ingress`;
- `PersistentVolumeClaim`.

## Что вы делаете руками

1. Собираете локальный образ `quest-board:local`.
2. Загружаете его в `kind`.
3. Применяете финальные манифесты.
4. Проверяете приложение через `Ingress`.

## Команды проверки

```bash
docker build -t quest-board:local ./demo-app
kind load docker-image quest-board:local --name k8s-dnd
kubectl apply -f manifests/04-config/quest-board-configmap.yaml
kubectl apply -f manifests/04-config/quest-board-secret.yaml
kubectl apply -f manifests/06-storage/quest-board-pvc.yaml
kubectl apply -f manifests/07-final/
kubectl get all -n adventure
curl http://localhost/
```

## Что должно получиться

- собственный образ загружен в локальный кластер;
- приложение доступно через `Ingress`;
- конфигурация читается;
- каталог `/data` смонтирован.

## Итог кампании

Вы прошли полный путь от устройства кластера до выкладки простого приложения. Это еще не production, но это уже реальная рабочая модель Kubernetes, собранная своими руками.

Возвращайтесь к [README](../README.md), если хотите пройти главы заново или использовать репозиторий как учебное пособие для команды.

