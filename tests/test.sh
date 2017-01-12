#!/usr/bin/env bash

echo "Copying alembic.ini to parent folder..."
cp ./alembic.ini ../
echo "Changing directory..."
cd ..
echo "Running alembic migration..."
alembic upgrade head
