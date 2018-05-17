#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/3/14 下午2:09
# @Author : xiaowei
# @Site : 
# @File : test.py
# @Software: PyCharm
#import json
#import xlwt
#
#book=xlwt.Workbook(encoding='utf-8',style_compression=0)
#
#sheet=book.add_sheet('主机信息',cell_overwrite_ok=True)
#sheet2=book.add_sheet('主机信息2',cell_overwrite_ok=True)
#
#sheet.write(0,0,'IP')
#sheet.write(0,1,'设备')
#sheet.write(0,2,'挂载点')
#sheet.write(0,3,'使用率')
#sheet2.write(0,0,'IP')
#sheet2.write(0,1,'设备')
#sheet2.write(0,2,'挂载点')
#sheet2.write(0,3,'使用率')
#
#info='{"status":"success","data":{"resultType":"vector","result":[{"metric":{"__name__":"HostInfo:Disk_usage","device":"/dev/dm-0","fstype":"ext4","instance":"192.168.2.158:9100","job":"node_exporter","mountpoint":"/"},"value":[1521007847.944,"74.12545845818191"]},{"metric":{"__name__":"HostInfo:Disk_usage","device":"/dev/sda1","fstype":"ext4","instance":"192.168.2.231:9100","job":"node_exporter","mountpoint":"/"},"value":[1521007847.944,"64.65177613459359"]},{"metric":{"__name__":"HostInfo:Disk_usage","device":"/dev/sda1","fstype":"ext4","instance":"192.168.2.232:9100","job":"node_exporter","mountpoint":"/"},"value":[1521007847.944,"69.3177449292346"]},{"metric":{"__name__":"HostInfo:Disk_usage","device":"/dev/sdb1","fstype":"ext4","instance":"192.168.2.158:9100","job":"node_exporter","mountpoint":"/data"},"value":[1521007847.944,"65.67301959228942"]},{"metric":{"__name__":"HostInfo:Disk_usage","device":"/dev/sdb1","fstype":"ext4","instance":"192.168.2.231:9100","job":"node_exporter","mountpoint":"/data"},"value":[1521007847.944,"16.19557882091729"]},{"metric":{"__name__":"HostInfo:Disk_usage","device":"/dev/sdb1","fstype":"ext4","instance":"192.168.2.232:9100","job":"node_exporter","mountpoint":"/data"},"value":[1521007847.944,"6.450719295737471"]}]}}'
#
#json_info=json.loads(info)
#disk_infos=json_info['data']['result']
#print(disk_infos)
#
#i=0
#for info in disk_infos:
#    hostInfo=info['metric']
#    print(hostInfo['instance'],hostInfo['device'],hostInfo['mountpoint'],info['value'][1])
#    sheet.write(i+1,0,hostInfo['instance'])
#    sheet.write(i+1,1,hostInfo['device'])
#    sheet.write(i+1,2,hostInfo['mountpoint'])
#    temp=info['value'][1]
#    sheet.write(i+1,3,str(int(float(temp)))+'%')
#    i=i+1
#j=0
#for info in disk_infos:
#    hostInfo=info['metric']
#    print(hostInfo['instance'],hostInfo['device'],hostInfo['mountpoint'],info['value'][1])
#    sheet2.write(j+1,0,hostInfo['instance'])
#    sheet2.write(j+1,1,hostInfo['device'])
#    sheet2.write(j+1,2,hostInfo['mountpoint'])
#    temp=info['value'][1]
#    sheet2.write(j+1,3,str(int(float(temp)))+'%')
#    j=j+1
#book.save('hostinfo.xls')
