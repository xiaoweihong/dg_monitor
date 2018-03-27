#!/bin/bash

#[ ! -d /data/monitor/grafana ] && mkdir -p /data/monitor/grafana
cd latest/bin
./grafana-server -config ../conf/defaults.ini
