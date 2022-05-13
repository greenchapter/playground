# 👨‍✈️ Kubernetes 



https://kubernetes.io/docs/reference/kubectl/cheatsheet/

### Debugging

Get the documentation of the resource and its fields
```bash
kubectl explain pods
```

Get the documentation of a specific field of a resource
```bash
kubectl explain pods.spec.containers
```

Describe a pod
```bash
kubectl describe pods/nginx
```

Return snapshot logs from pod nginx with only one container
```bash
kubectl logs nginx
```

List all pods in ps output format with more information (such as node name)
```bash
kubectl get pods -o wide
```

Get output from running 'date' command pod mypod, using the first container by default
```bash
kubectl exec my-pod -- date
```

Get output from running 'date' command in ruby-container from my-pod
```bash
kubectl exec my-pod -c ruby-container -- date
```

Switch to raw terminal mode, sends stdin to 'bash' in ruby-container from pod my-pod # and sends stdout/stderr from 'bash' back to the client
```bash
kubectl exec my-pod -c ruby-container -i -t -
```

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
