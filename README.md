[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](https://github.com/LREN-CHUV/data-catalog-db/blob/master/LICENSE) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/9adcf4cbd730472386d0e71ab27b9b6b)](https://www.codacy.com/app/mirco-nasuti/data-catalog-db?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LREN-CHUV/data-catalog-db&amp;utm_campaign=Badge_Grade) [![CircleCI](https://circleci.com/gh/LREN-CHUV/data-catalog-db.svg?style=svg)](https://circleci.com/gh/LREN-CHUV/data-catalog-db)

# Data Catalog DB

This project contains the model and migration scripts needed to deploy the data-catalog-db. This database is used to store metadata extracted mainly from DICOM files in the Data Factory.

## Prerequisites

* Alembic

## Usage

Write a configuration file called `alembic.ini` based on `alembic.ini.sample`, `cd` db_migrations folder and run `alembic upgrade head`. 

## Tests

A test script is available in the tests directory. It is written for CircleCI but you can run it manually if needed.

Note that there are some prerequisites for that :
* A Postgres instance has to be running (following tests/alembic.ini.test configuration)
* Alembic and Psycopg2 have to be installed
