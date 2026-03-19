# 07. Подземелья хранения

## Сюжет

Отряд записывает трофеи и заметки о квестах. Если лагерь сгорит и будет пересобран, записи не должны исчезнуть.

## Что это в мире D&D

Сокровищница и архив под замком - это тома хранения.

## Что это в Kubernetes

- `emptyDir` живет только пока жив конкретный `Pod`;
- `PersistentVolumeClaim` просит устойчивое хранилище у кластера;
- контейнер получает это хранилище через `volumeMounts`.

В `kind` для локального обучения поведение storage class зависит от окружения, поэтому в репозитории мы показываем и простой `emptyDir`, и вариант с `PersistentVolumeClaim`.

## Что вы делаете руками

- создаете `PersistentVolumeClaim`;
- монтируете том в приложение по пути `/data`;
- пишете заметку партии и проверяете, что каталог смонтирован.

## Команды проверки

```bash
kubectl apply -f manifests/06-storage/quest-board-pvc.yaml
kubectl apply -f manifests/06-storage/quest-board-storage-deployment.yaml
kubectl get pvc -n adventure
kubectl exec -n adventure deploy/quest-board -- sh -c 'echo \"dragon defeated\" >> /data/party.log && cat /data/party.log'
```

## Что должно получиться

- PVC в состоянии `Bound` или понятное сообщение, если локальная storage class требует дополнительной настройки;
- файл `/data/party.log` существует и читается из контейнера.

## Итог квеста

Вы увидели разницу между временным лагерем и устойчивым хранилищем данных.

Следующий шаг: [08. Финальный рейд](./08-final-raid.md) и [лаб 07](../labs/07-dungeons-of-storage.md).

