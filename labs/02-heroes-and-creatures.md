# Лаб 02. Призываем первого героя

## Цель

Создать и изучить одиночный `Pod`.

## Команды

```bash
kubectl apply -f manifests/01-pod/quest-scroll-pod.yaml
kubectl get pods -n adventure
kubectl describe pod quest-scroll -n adventure
kubectl logs quest-scroll -n adventure
kubectl delete -f manifests/01-pod/quest-scroll-pod.yaml
```

## Что заметить

- `Pod` легко создать и удалить;
- его жизненный цикл виден через `describe`;
- логи можно смотреть напрямую.

