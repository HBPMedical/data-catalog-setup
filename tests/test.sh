#!/usr/bin/env bash

echo "Starting a Postgres container..."
postgres_container=$(docker run -d -p 5432:5432 postgres)
sleep 5

# Get gateway IP
echo "Searching for gateway IP..."
GATEWAY_IP=$(ip addr | grep docker | grep inet | grep -Eo '[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*')

echo "Running a migration..."
docker run --rm -e "DB_URL=postgresql://postgres:postgres@$GATEWAY_IP:5432/postgres" hbpmip/data-catalog-setup upgrade head
ret=$?

if [ -z "$CIRCLECI" ] || [ "$CIRCLECI" = false ] ; then
    echo "Removing the Postgres container..."
    docker rm -f ${postgres_container}
fi

exit $ret
