`docker-compose build`

`docker-compose up`

`docker tag greenchapter/webserver:latest greenchapter/webserver:1.0.0`

`docker push greenchapter/webserver:latest`

`docker pull greenchapter/webserver:latest`

`docker run --name website -d -p 80:80 greenchapter/webserver`


Create your own image
`docker build -t my-nginx-image .`
