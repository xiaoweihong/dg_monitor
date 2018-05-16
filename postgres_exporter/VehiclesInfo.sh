#!/bin/bash

date_now=$(date +%F)
date_tomorrow=$(date -d tomorrow +%F)
function getVehicles(){
    vehicles_temp2=`su - postgres -c"psql -d deepdata_v6 << eof
explain analyze select count(*) from vehicles where uts > '$date_now' and uts < '$date_tomorrow';
eof"`

    vehicles_count_2=`echo $vehicles_temp2|awk -F 'actual time' '{print $3}'|awk '{print $2}'|awk -F '=' '{print $2}'`

}
#vehicles_temp1=`su - postgres -c"psql -d deepdata_v6 << eof
#select count(*) from vehicles where uts > '$date_now' and uts < '$date_tomorrow';
#eof"`
#vehicles_count_1=`echo $vehicles_temp1|awk '{print $3}'`
#echo $vehicles_count_1

function getPedestrians(){
    pedestrians_temp2=`su - postgres -c"psql -d deepdata_v6 << eof
explain analyze select count(*) from pedestrians where uts > '$date_now' and uts < '$date_tomorrow';
eof"`

    pedestrians_count_2=`echo $pedestrians_temp2|awk -F 'actual time' '{print $3}'|awk '{print $2}'|awk -F '=' '{print $2}'`
}

function getNonmotors(){
    nonmotors_temp2=`su - postgres -c"psql -d deepdata_v6 << eof
explain analyze select count(*) from nonmotors where uts > '$date_now' and uts < '$date_tomorrow';
eof"`

    nonmotors_count_2=`echo $nonmotors_temp2|awk -F 'actual time' '{print $3}'|awk '{print $2}'|awk -F '=' '{print $2}'`
}

getVehicles
getPedestrians
getNonmotors
echo $vehicles_count_2
echo $nonmotors_count_2
echo $pedestrians_count_2