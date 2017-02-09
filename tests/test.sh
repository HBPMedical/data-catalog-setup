#!/usr/bin/env bash

if [ -z "$CIRCLECI" ] || [ "$CIRCLECI" = false ] ; then

    # Start DB container
    echo "Starting container..."
    db_docker_id=$(docker run -d hbpmip/data-catalog-db)

    # Query database
    echo "Waiting for the DB to be ready..."
    sleep 5
    out=$(docker exec -ti ${db_docker_id} bash -c "psql -U postgres -c \"\dt\" | grep alembic_version")
    ret=${#out}

    # Remove DB container
    echo "Removing DB container..."
    docker kill ${db_docker_id}
    docker rm -f ${db_docker_id}

    # Exit
    if [ $ret -eq 48 ]
    then
      exit 0
    else
      exit 1
    fi

else

    # Do not use Docker on CircleCI because it uses LXC driver
    echo "Changing directory..."
    cd ..
    echo "Running alembic migration..."
    alembic upgrade head
    exit $?
fi
