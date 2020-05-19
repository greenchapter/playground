`docker-compose build`

`docker-compose up`

`docker run -p 3306:3306 --name some-database --volume=/storage/mariadb:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d greenchapter/database:latest`

`docker run -p 3306:3306 --name some-database --volume=/storage/mariadb:/var/lib/mysql -e MYSQL_RANDOM_ROOT_PASSWORD=yes -d greenchapter/database:latest`

`docker exec some-database /usr/bin/mysqldump -u root --password=my-secret-pw --all-databases > backup.sql`
