# Using Environment During Development

(This can be packaged for your individual needs)

1) Create the following `docker-compose.yml` at the root of your project
```yaml
version: "3.1"

services:
  ###
  # Workspace -> This is where you develop in
  ###
  workspace:
    image: "cloudmyit/php-cicd:php-${VERSION_WORKSPACE_PHP}"
    volumes:
      - ${CODE_PATH}:/opt
  
  ###
  # Serve a website if needed
  ###
  nginx:
    image: nginx:stable-alpine
    volumes:
      - ${CODE_PATH}/.dev/nginx/:/etc/nginx/conf.d
      - ${CODE_PATH}:/opt
    ports:
      - "80:80"
    depends_on:
      - php-fpm
  # PHP-FPM so NGINX can host PHP
  php-fpm:
    image: "cloudmyit/php-cicd:php-${VERSION_PHP}"
    ports:
      - "9000:9000"
    volumes:
      - ${CODE_PATH}:/opt

  ###
  # Databases
  #
  # Each database has a "database" and "database-dev" server
  # The "database" server should be used with nginx
  #   Its data is stored in the codepath
  # The "database-dev" server should be used when running tests
  ###

  # MySQL
  mysql:
    image: "cloudmyit/php-cicd:mysql-${VERSION_MYSQL}"
    volumes:
      - ${CODE_PATH}/.dev/mysql:/var/lib/mysql
  mysql-dev:
    image: "cloudmyit/php-cicd:mysql-${VERSION_MYSQL}"

  # PostgreSQL
  postgresql:
    image: "cloudmyit/php-cicd:postgresql-${VERSION_POSTGRESQL}"
    volumes:
      - ${CODE_PATH}/.dev/postgresql:/var/lib/postgresql/data
  postgresql-dev:
    image: "cloudmyit/php-cicd:postgresql-${VERSION_POSTGRESQL}"
```

2) Add the following variables to your `.env` file.
```
CODE_PATH=./
VERSION_WORKSPACE_PHP=latest
VERSION_PHP=latest
VERSION_MYSQL=latest
VERSION_POSTGRESQL=latest
```

3) Create the following directories
  - `.dev`
  - `.dev/mysql`
  - `.dev/nginx`
  - `.dev/postgres`

4) Create the default nginx config `.dev/nginx/default.conf`
```nginx
server {
    listen  80;

    root /opt/public;

    location / {
        try_files $uri /index.php$is_args$args;
    }

    location ~ ^/.+\.php(/|$) {
        fastcgi_pass php-fpm:9000;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    }
}
```

> Additional Hosts and VHosts can be created by creating additional config files in this same directory

5) Update PHPUnit to use the "database-dev" servers. `phpunit.xml`
```xml
<phpunit>
<!-- ... -->
    <php>
        <!-- ... -->
        <server name="DB_HOST" value="mysql-dev">
        <!-- ... -->
    </php>
</phpunit>
```
> Note: This is an overly simple example.

6) Configure your IDE to connect to the "workspace" instance and put you into the /opt directory