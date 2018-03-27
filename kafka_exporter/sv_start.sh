#!/bin/bash
IP=$(hostname -I | cut -f1 -d' ')

cd latest
#./kafka_exporter --kafka.server=192.168.2.158:9092 --kafka.server=192.168.2.158:9093 
./kafka_exporter --kafka.server=$IP:9092 
