#!/usr/bin/env bash

echo "Copying alembic.ini to parent folder..."
cp ./tests/alembic.ini .
echo "Running alembic migration..."
alembic upgrade head
