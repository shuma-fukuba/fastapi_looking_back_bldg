#!/bin/bash

echo "Waiting for mysql to start..."
until mysql -h"$MYSQL_HOST" -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" &> /dev/null
do
    sleep 1
done

cd /usr/src/app/db && alembic upgrade head
# cd /usr/src/app/db && python seed.py
