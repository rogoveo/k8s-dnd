# 03. Отряды и роли

## Сюжет

Один герой может пасть в бою. Настоящая экспедиция требует резервных бойцов и командира, который следит, чтобы численность отряда сохранялась.

## Что это в мире D&D

- отряд приключенцев - это `Deployment`;
- список бойцов, которых нужно поддерживать, - это `ReplicaSet`.

## Что это в Kubernetes

`Deployment` описывает желаемое состояние группы одинаковых `Pod`.

Он отвечает за:

- количество реплик;
- шаблон `Pod`;
- rollout при обновлении;
- восстановление отряда, если один из бойцов исчез.

`ReplicaSet` обычно не создают вручную. Его порождает `Deployment`.

## Что вы делаете руками

- запускаете `Deployment` `quest-board`;
- масштабируете число реплик;
- смотрите, как Kubernetes поддерживает нужный размер партии.

## Команды проверки

```bash
kubectl apply -f manifests/02-deployment/quest-board-deployment.yaml
kubectl get deployments -n adventure
kubectl get replicasets -n adventure
kubectl get pods -n adventure -l app=quest-board
kubectl scale deployment quest-board --replicas=3 -n adventure
```

## Что должно получиться

- `Deployment` в состоянии `Available`;
- после масштабирования появляется три одинаковых `Pod`;
- если удалить один `Pod`, `Deployment` создаст новый.

## Итог квеста

Вы перестали мыслить одиночными `Pod` и начали описывать желаемое состояние системы.

Следующий шаг: [04. Города и маршруты](./04-cities-and-routes.md) и [лаб 03](../labs/03-parties-and-roles.md).

