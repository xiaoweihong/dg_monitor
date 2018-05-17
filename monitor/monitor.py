#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/3/15 下午10:38
# @Author : xiaowei
# @Site : 
# @File : monitor.py
# @Software: PyCharm
import xlwt
from HostInfo import GetInfos
from ExcleStyle import Excle_tool
from DeepDataPgInfo import  DeepVideoPostgresTool
from collections import OrderedDict
import time
localTime = time.localtime(time.time())
database="deepdata_v6"
host="192.168.2.158"
#strTime = time.strftime("%Y%m%d%H%M%S", localTime)
strTime = time.strftime("%Y%m%d", localTime)
filename=strTime+'.xls'
book=xlwt.Workbook(encoding='utf-8',style_compression=0)

sheet0=book.add_sheet('数据统计',cell_overwrite_ok=True)
sheet1=book.add_sheet('主机信息',cell_overwrite_ok=True)
sheet2=book.add_sheet('内存信息',cell_overwrite_ok=True)
sheet3=book.add_sheet('GPU使用率',cell_overwrite_ok=True)
sheet4=book.add_sheet('GPU显存使用',cell_overwrite_ok=True)
sheet5=book.add_sheet('网络流量接收',cell_overwrite_ok=True)
sheet6=book.add_sheet('网络流量流出',cell_overwrite_ok=True)


disk_content=[]
mem_content=[]
gpu_content=[]
gpu_mem_content=[]
network_receive_content=[]
network_transmit_content=[]

data_table_info=DeepVideoPostgresTool(database=database,host=host).getDeepDataInfo()
data_table_title=["机动车","非机动车","行人"]
print(data_table_info)

json_disk_info=GetInfos().getDiskInfo()
disk_infos=json_disk_info['data']['result']
disk_table_title=GetInfos().getTitle(disk_infos)

json_mem_info=GetInfos().getMemInfo()
mem_infos=json_mem_info['data']['result']
mem_table_title=GetInfos().getTitle(mem_infos)

json_gpu_info=GetInfos().getGpuUtil()
gpu_infos=json_gpu_info['data']['result']
gpu_table_title=GetInfos().getTitle(gpu_infos)

json_gpu_mem_info=GetInfos().getGpuMemInfo()
gpu_mem_infos=json_gpu_mem_info['data']['result']
gpu_mem_table_title=GetInfos().getTitle(gpu_mem_infos)

json_network_receive_info=GetInfos().getNetworkReceive()
network_receive_infos=json_network_receive_info['data']['result']
network_receive_table_title=GetInfos().getTitle(network_receive_infos)

json_network_transmit_info=GetInfos().getNetworkTransmit()
network_transmit_infos=json_network_transmit_info['data']['result']
network_transmit_table_title=GetInfos().getTitle(network_transmit_infos)


for i in range(len(data_table_title)):
    sheet0.col(i).width=256*30
    sheet0.write(0,i,data_table_title[i],Excle_tool().def_style(320))

for i in range(len(disk_table_title)):
    sheet1.col(i).width=256*30
    sheet1.write(0,i,disk_table_title[i],Excle_tool().def_style(320))

for i in range(len(mem_table_title),):
    sheet2.col(i).width=256*30
    sheet2.write(0,i,mem_table_title[i],Excle_tool().def_style(320))

for i in range(len(gpu_table_title)):
    sheet3.col(i).width=256*30
    sheet3.write(0,i,gpu_table_title[i],Excle_tool().def_style(320))

for i in range(len(gpu_mem_table_title)):
    sheet4.col(i).width=256*30
    sheet4.write(0,i,gpu_mem_table_title[i],Excle_tool().def_style(320))

for i in range(len(network_receive_table_title)):
    sheet5.col(i).width=256*30
    sheet5.write(0,i,network_receive_table_title[i],Excle_tool().def_style(320))

for i in range(len(network_transmit_table_title)):
    sheet6.col(i).width=256*30
    sheet6.write(0,i,network_transmit_table_title[i],Excle_tool().def_style(320))

for info in disk_infos:
    hostInfo = info['metric']
    value=info['value']
    hostInfo = OrderedDict(hostInfo)
    hostInfo['value']=value[1]+"%"
    disk_content.append(list(hostInfo.values()))
print(disk_content)

for info in mem_infos:
    hostInfo = info['metric']
    value=info['value']
    hostInfo = OrderedDict(hostInfo)
    hostInfo['value']=value[1]+"%"
    mem_content.append(list(hostInfo.values()))

for info in gpu_infos:
    hostInfo = info['metric']
    value=info['value']
    hostInfo = OrderedDict(hostInfo)
    hostInfo['value']=value[1]
    gpu_content.append(list(hostInfo.values()))


for info in gpu_mem_infos:
    hostInfo = info['metric']
    value=info['value']
    hostInfo = OrderedDict(hostInfo)
    hostInfo['value']=value[1]
    gpu_mem_content.append(list(hostInfo.values()))

for info in network_receive_infos:
    hostInfo = info['metric']
    value=info['value']
    hostInfo = OrderedDict(hostInfo)
    hostInfo['value']=value[1]+"GB"
    network_receive_content.append(list(hostInfo.values()))

for info in network_transmit_infos:
    hostInfo = info['metric']
    value=info['value']
    hostInfo = OrderedDict(hostInfo)
    hostInfo['value']=value[1]+"GB"
    network_transmit_content.append(list(hostInfo.values()))

print("正在导出数据信息....")
print(list(data_table_info.values()))
for row in range(len(list(data_table_info.values()))):
    sheet0.write(1,row,list(data_table_info.values())[row],Excle_tool().def_style(320,False))

print("正在导出disk信息....")
for row in range(len(disk_content)):
    for col in range(0,len(disk_content[row])):
        sheet1.write(row+1,col,list(disk_content[row][col]),Excle_tool().def_style(320,False))

print("正在导出memory信息....")
for row in range(len(mem_content)):
    for col in range(0,len(mem_content[row])):
        sheet2.write(row+1,col,list(mem_content[row][col]),Excle_tool().def_style(320,False))

print("正在导出GPU使用率信息....")
for row in range(len(gpu_content)):
    for col in range(0,len(gpu_content[row])):
        sheet3.write(row+1,col,list(gpu_content[row][col]),Excle_tool().def_style(320,False))

print("正在导出显存使用信息....")
for row in range(len(gpu_mem_content)):
    for col in range(0,len(gpu_mem_content[row])):
        sheet4.write(row+1,col,list(gpu_mem_content[row][col]),Excle_tool().def_style(320,False))

print("正在导出网卡接收数据信息....")
for row in range(len(network_receive_content)):
    for col in range(0,len(network_receive_content[row])):
        sheet5.write(row+1,col,list(network_receive_content[row][col]),Excle_tool().def_style(320,False))

print("正在导出网卡发送数据信息....")
for row in range(len(network_transmit_content)):
    for col in range(0,len(network_transmit_content[row])):
        sheet6.write(row+1,col,list(network_transmit_content[row][col]),Excle_tool().def_style(320,False))

book.save('../'+filename)