#!/bin/bash

IP=`hostname -I|cut -f1 -d ' '`
cd latest

./redis_exporter -redis.addr $IP:6379 -log-format json
