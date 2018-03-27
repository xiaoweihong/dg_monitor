#!/bin/bash

IP=$(hostname -I | cut -f1 -d' ')
cd latest
#sed -r -i.bak "s/\<(1?([0-1,3-9][0-9])|12[0-6,8-9]|2[0-6,8-9][0-9]?|[1-6,8-9]|27|7)(\.[0-9]+){3}/$IP/g" prometheus.yml 

[ ! -d /data/monitor/prometheus ] && mkdir -p /data/monitor/prometheus
./prometheus --web.listen-address="0.0.0.0:9090" --storage.tsdb.path="/home/admin/data/monitor/prometheus/"
