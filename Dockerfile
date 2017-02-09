FROM postgres:9.6.1

MAINTAINER mirco.nasuti@chuv.ch


COPY data_catalog_schema.py /
COPY alembic.ini /
COPY db_migrations/ /db_migrations/
COPY migrate.sh /docker-entrypoint-initdb.d/

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        'python3=3.4.2-2' \
        'python3-dev=3.4.2-2' \
        'python3-pip=1.5.6-5' \
        'build-essential=11.7' \
        'postgresql-server-dev-9.6=9.6.2-1.pgdg80+1' \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install 'alembic==0.8.10' 'psycopg2==2.6.2'
