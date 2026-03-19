# Лаб 00. Поднимаем локальное королевство

## Цель

Создать кластер `kind`, namespace `adventure` и, при желании, ingress-controller для следующих глав.

## Шаги

### 1. Создайте кластер

```bash
kind create cluster --config cluster/kind-config.yaml --name k8s-dnd
```

### 2. Проверьте состояние

```bash
kubectl cluster-info
kubectl get nodes
```

### 3. Создайте namespace кампании

```bash
kubectl apply -f manifests/00-namespace.yaml
```

### 4. Установите ingress-nginx для локального кластера

В официальном гайде `kind` рекомендуется кластер с `extraPortMappings` и отдельная установка ingress-controller. Для локального обучения подойдет manifest провайдера `kind` из ingress-nginx:

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
kubectl wait --namespace ingress-nginx \
  --for=condition=ready pod \
  --selector=app.kubernetes.io/component=controller \
  --timeout=90s
```

## Проверка

```bash
kubectl get ns
kubectl get pods -n ingress-nginx
```

## Что должно получиться

- кластер `k8s-dnd` поднят;
- есть namespace `adventure`;
- ingress-controller готов к работе.
