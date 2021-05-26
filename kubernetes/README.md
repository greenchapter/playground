# 👨‍✈️ Kubernetes 

https://kubernetes.io/docs/reference/kubectl/cheatsheet/

### MiniKube

https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/

`minikube start`

`minikube kubectl -- get pods -A` 

`kubectl apply -f echo-server.yaml`

`minikube service echoserver-service --url` 

`kubectl scale --replicas=3 deploy/echoserver` 

`minikube stop`

`minikube delete`


### k9s

https://k9scli.io/topics/commands/

`brew install k9s`

### k3s

`curl -sfL https://get.k3s.io | sh -`
