[![CHUV](https://img.shields.io/badge/CHUV-LREN-AF4C64.svg)](https://www.unil.ch/lren/en/home.html) [![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](https://github.com/LREN-CHUV/data-catalog-setup/blob/master/LICENSE) [![DockerHub](https://img.shields.io/badge/docker-hbpmip%2Fdata--catalog--setup-008bb8.svg)](https://hub.docker.com/r/hbpmip/data-catalog-setup/) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/b999388f1d5f4f99a3eb692bb71ae556)](https://www.codacy.com/app/hbp-mip/data-catalog-setup?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LREN-CHUV/data-catalog-setup&amp;utm_campaign=Badge_Grade) [![CircleCI](https://circleci.com/gh/LREN-CHUV/data-catalog-setup.svg?style=svg)](https://circleci.com/gh/LREN-CHUV/data-catalog-setup)

# Data Catalog Setup

Migration scripts for the Data Catalog database used to capture provenance information on all files managed by the Data Factory.

## Introduction

The goal of this project is to provide a Docker container including Alembic and a Python model of the Data Catalog schema.

## Usage

Example:

`docker run --rm -e "DB_URL=postgresql://postgres:postgres@localhost:5432/postgres" hbpmip/data-catalog-setup:1.6.0 upgrade
head`

## Build

Run: `./build.sh`

## Test

Run: `cd tests && ./test.sh`

## Publish on Docker Hub

Run: `./publish.sh`

## License

Copyright (C) 2017 [LREN CHUV](https://www.unil.ch/lren/en/home.html)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
