#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER postgresql_user;
    ALTER USER postgresql_user PASSWORD 'postgresql_user_password';
    CREATE DATABASE postgresql_database;
    GRANT ALL PRIVILAGES ON DATABASE postgresql_database TO postgresql_user;

    CREATE USER postgresql_admin_user;
    ALTER USER postgresql_admin_user PASSWORD 'postgresql_admin_user_password';
    ALTER USER postgresql_admin_user WITH SUPERUSER;
EOSQL