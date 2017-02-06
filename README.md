[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](https://github.com/LREN-CHUV/data-catalog-db/blob/master/LICENSE) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/9adcf4cbd730472386d0e71ab27b9b6b)](https://www.codacy.com/app/mirco-nasuti/data-catalog-db?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LREN-CHUV/data-catalog-db&amp;utm_campaign=Badge_Grade) [![CircleCI](https://circleci.com/gh/LREN-CHUV/data-catalog-db.svg?style=svg)](https://circleci.com/gh/LREN-CHUV/data-catalog-db)

# Data Catalog DB

This project contains the model and migration scripts needed to deploy the data-catalog-db. 
This database is used to store metadata mostly extracted from DICOM files in the Data Factory.

## Prerequisites

* Alembic

## Usage

Run `alembic upgrade head`.

## Tests

Open the tests directory and run `./test.sh`.

NOTE: This will launch a Docker container with a Postgres instance on the port 5432. On CircleCI,
it does not launch a Docker container but connects to a local Postgres instance. If you don't want to
use Docker, you can define this environment variable: `CIRCLE_CI=True`
