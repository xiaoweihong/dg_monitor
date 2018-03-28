#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/3/27 下午10:51
# @Author : xiaowei
# @Site : 
# @File : title.py
# @Software: PyCharm
import json
DiskInfo='{"status":"success","data":{"resultType":"vector","result":[{"metric":{"__name__":"HostInfo:Disk_usage","device":"/dev/dm-0","fstype":"ext4","instance":"192.168.2.158:9100","job":"node_exporter","mountpoint":"/"},"value":[1521007847.944,"74.12545845818191"]},{"metric":{"__name__":"HostInfo:Disk_usage","device":"/dev/sda1","fstype":"ext4","instance":"192.168.2.231:9100","job":"node_exporter","mountpoint":"/"},"value":[1521007847.944,"64.65177613459359"]},{"metric":{"__name__":"HostInfo:Disk_usage","device":"/dev/sda1","fstype":"ext4","instance":"192.168.2.232:9100","job":"node_exporter","mountpoint":"/"},"value":[1521007847.944,"69.3177449292346"]},{"metric":{"__name__":"HostInfo:Disk_usage","device":"/dev/sdb1","fstype":"ext4","instance":"192.168.2.158:9100","job":"node_exporter","mountpoint":"/data"},"value":[1521007847.944,"65.67301959228942"]},{"metric":{"__name__":"HostInfo:Disk_usage","device":"/dev/sdb1","fstype":"ext4","instance":"192.168.2.231:9100","job":"node_exporter","mountpoint":"/data"},"value":[1521007847.944,"16.19557882091729"]},{"metric":{"__name__":"HostInfo:Disk_usage","device":"/dev/sdb1","fstype":"ext4","instance":"192.168.2.232:9100","job":"node_exporter","mountpoint":"/data"},"value":[1521007847.944,"6.450719295737471"]}]}}'

temp=json.loads(DiskInfo)
s=temp['data']['result'][0]['metric']
print(s)
title=[]
for i in s:
    title.append(i)

print(title)


