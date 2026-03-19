# Лаб 03. Собираем отряд

## Цель

Понять, как `Deployment` поддерживает желаемое число копий.

## Команды

```bash
kubectl apply -f manifests/02-deployment/quest-board-deployment.yaml
kubectl get deploy,rs,pods -n adventure
kubectl scale deployment quest-board --replicas=3 -n adventure
kubectl get pods -n adventure -l app=quest-board
kubectl delete pod -n adventure -l app=quest-board --field-selector=status.phase=Running --wait=false
```

## Что заметить

- `ReplicaSet` появляется автоматически;
- число `Pod` возвращается к нужному значению;
- вы описываете не экземпляры, а желаемое состояние.

