#!/bin/bash

cd latest
export DATA_SOURCE_NAME="postgresql://postgres:123456@localhost:5432/deepdata_v6"
./postgres_exporter
