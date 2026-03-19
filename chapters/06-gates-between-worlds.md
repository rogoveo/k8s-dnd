# 06. Врата между мирами

## Сюжет

Путешественники из внешнего мира не знают внутренние дороги вашего королевства. Им нужен портал с понятным маршрутом.

## Что это в мире D&D

Магические ворота, ведущие к нужной гильдии или таверне, - это `Ingress`.

## Что это в Kubernetes

`Ingress` описывает HTTP-маршруты до сервисов внутри кластера. Сам по себе объект `Ingress` ничего не делает, пока в кластере нет ingress-controller.

В этой кампании предполагается `ingress-nginx`, установленный в `kind`.

## Что вы делаете руками

- убеждаетесь, что ingress-controller установлен;
- создаете `Ingress` для `quest-board`;
- обращаетесь к приложению через `localhost`.

## Минимальные команды

```bash
kubectl get pods -n ingress-nginx
kubectl apply -f manifests/05-ingress/quest-board-ingress.yaml
kubectl get ingress -n adventure
curl http://localhost/
```

## Что должно получиться

- `Ingress` существует и указывает на сервис `quest-board`;
- `curl http://localhost/` возвращает HTML учебного приложения.

## Итог квеста

Теперь у вашего королевства есть единая внешняя точка входа.

Следующий шаг: [07. Подземелья хранения](./07-dungeons-of-storage.md) и [лаб 06](../labs/06-gates-between-worlds.md).

