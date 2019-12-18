`docker ps --all`

attach to docker conteiner logs
`docker logs --follow <container name>`

`docker restart <container name>`

`docker save <image name> > <archive name>.tar`

`docker load --input <archive name>.tar`

`docker exec -it <container id> /bin/bash`

`docker-compose up -d --force-recreate --build`

`docker system prune`

`docker system prune -a`

`docker-compose pull && docker-compose up -d --force-recreate --no-deps --build` 
