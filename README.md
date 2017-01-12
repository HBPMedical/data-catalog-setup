[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](https://github.com/LREN-CHUV/mri-meta-db/blob/master/LICENSE) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/9adcf4cbd730472386d0e71ab27b9b6b)](https://www.codacy.com/app/mirco-nasuti/mri-meta-db?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LREN-CHUV/mri-meta-db&amp;utm_campaign=Badge_Grade) [![CircleCI](https://circleci.com/gh/LREN-CHUV/mri-meta-db.svg?style=svg)](https://circleci.com/gh/LREN-CHUV/mri-meta-db)

# MRI Meta DB

This project contains the model and migration scripts needed to deploy the mri-meta-db. This database is used to store metadata extracted mainly from DICOM files in the Data Factory.

## Prerequisites

* Alembic

## Usage

Write a configuration file called `alembic.ini` based on `alembic.ini.sample`, `cd` db_migrations folder and run `alembic upgrade head`. 
