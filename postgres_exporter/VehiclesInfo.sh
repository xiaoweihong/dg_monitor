#!/bin/bash

date_now=$(date +%F)
date_tomorrow=$(date -d tomorrow +%F)
vehicles_temp=`su - postgres -c"psql -d deepdata_v6 << eof
select count(*) from vehicles where uts > '$date_now' and uts < '$date_tomorrow';
eof"`
vehicles_count_1=`echo $vehicles_temp|awk '{print $3}'`
echo $vehicles_count_1
