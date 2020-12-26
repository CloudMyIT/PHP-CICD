# Example

This directory contains an example of how to use this repository

## Quickstart
`docker-compose --env-file ./.env up`

## Services

### Workspace
This container should be where you connect your IDE to during development.

### Nginx
This container will allow you to locally host and test your application as if it were live

### PHP-FPM
This container allows Nginx to process PHP files

### Database Servers
The following servers are launched in both a "database" and "database-dev" mode.

- MySQL
- PostgreSQL

## Environment File
If you are using laravel, you will need to add these to your existing `.env` file.
```
CODE_PATH=./
VERSION_WORKSPACE_PHP=latest
VERSION_PHP=latest
VERSION_MYSQL=latest
VERSION_POSTGRESQL=latest
```

### CODE_PATH
This variable should be the root of your project.

> This should be the directory containing the `public` folder

### VERSION_WORKSPACE_PHP
This variable should be the version of PHP that you want to use in the command line while developing

### VERSION_PHP
This variable should be the version of PHP that you want to be used when running in Nginx during development

### VERSION_MYSQL
This variable should be the version of MySQL that you want to be used during development

### VERSION_POSTGRESQL
This variable should be the version of PostgreSQL that you want to be used during development.