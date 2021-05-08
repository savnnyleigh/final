# Deployment Directions


## Flask

To deploy the flask service and deployment (found in /deploy/flask/) use the following commands
```
kubectl apply -f flask-service.yml
kubectl apply -f flask-deployment.yml
```

## Redis

To deploy the redis service and deployment (found in /deploy/redis/) use the following commands
```
kubectl apply -f redis-service.yml
kubectl apply -f redis-deployment.yml
kubectl apply -f redis-pvc.yml
```

## Worker
To deploy the worker deployment (found in /deploy/worker/) use the following commands
```
kubectl apply -f worker-deployment.yml
```
