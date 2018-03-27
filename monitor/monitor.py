#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/3/15 下午10:38
# @Author : xiaowei
# @Site : 
# @File : monitor.py
# @Software: PyCharm
import json
import xlwt
#from monitor.GetHostInfo import GetInfos
from HostInfo import GetInfos
import time
localTime = time.localtime(time.time())
#strTime = time.strftime("%Y%m%d%H%M%S", localTime)
strTime = time.strftime("%Y%m%d", localTime)
filename=strTime+'.xls'
book=xlwt.Workbook(encoding='utf-8',style_compression=0)

sheet1=book.add_sheet('主机信息',cell_overwrite_ok=True)
sheet2=book.add_sheet('内存信息',cell_overwrite_ok=True)
sheet3=book.add_sheet('GPU使用率',cell_overwrite_ok=True)
sheet4=book.add_sheet('GPU显存使用',cell_overwrite_ok=True)
sheet5=book.add_sheet('网络流量接收',cell_overwrite_ok=True)
sheet6=book.add_sheet('网络流量流出',cell_overwrite_ok=True)

#DiskInfo='{"status":"success","data":{"resultType":"vector","result":[{"metric":{"__name__":"HostInfo:Disk_usage","device":"/dev/dm-0","fstype":"ext4","instance":"192.168.2.158:9100","job":"node_exporter","mountpoint":"/"},"value":[1521007847.944,"74.12545845818191"]},{"metric":{"__name__":"HostInfo:Disk_usage","device":"/dev/sda1","fstype":"ext4","instance":"192.168.2.231:9100","job":"node_exporter","mountpoint":"/"},"value":[1521007847.944,"64.65177613459359"]},{"metric":{"__name__":"HostInfo:Disk_usage","device":"/dev/sda1","fstype":"ext4","instance":"192.168.2.232:9100","job":"node_exporter","mountpoint":"/"},"value":[1521007847.944,"69.3177449292346"]},{"metric":{"__name__":"HostInfo:Disk_usage","device":"/dev/sdb1","fstype":"ext4","instance":"192.168.2.158:9100","job":"node_exporter","mountpoint":"/data"},"value":[1521007847.944,"65.67301959228942"]},{"metric":{"__name__":"HostInfo:Disk_usage","device":"/dev/sdb1","fstype":"ext4","instance":"192.168.2.231:9100","job":"node_exporter","mountpoint":"/data"},"value":[1521007847.944,"16.19557882091729"]},{"metric":{"__name__":"HostInfo:Disk_usage","device":"/dev/sdb1","fstype":"ext4","instance":"192.168.2.232:9100","job":"node_exporter","mountpoint":"/data"},"value":[1521007847.944,"6.450719295737471"]}]}}'
#MemInfo='{"status":"success","data":{"resultType":"vector","result":[{"metric":{"__name__":"HostInfo:Memory_used","instance":"192.168.2.158:9100","job":"node_exporter"},"value":[1521184227.019,"34.096729572050386"]},{"metric":{"__name__":"HostInfo:Memory_used","instance":"192.168.2.231:9100","job":"node_exporter"},"value":[1521184227.019,"34.330911564956445"]},{"metric":{"__name__":"HostInfo:Memory_used","instance":"192.168.2.232:9100","job":"node_exporter"},"value":[1521184227.019,"20.812912318215503"]}]}}'
#GpuInfo='{"status":"success","data":{"resultType":"vector","result":[{"metric":{"__name__":"HostInfo:GPU_utilization_pct","device":"0","instance":"192.168.2.158:9101","job":"nvidia_exporter"},"value":[1521184853.724,"0.01"]},{"metric":{"__name__":"HostInfo:GPU_utilization_pct","device":"0","instance":"192.168.2.231:9101","job":"nvidia_exporter"},"value":[1521184853.724,"0.05"]},{"metric":{"__name__":"HostInfo:GPU_utilization_pct","device":"0","instance":"192.168.2.232:9101","job":"nvidia_exporter"},"value":[1521184853.724,"0"]},{"metric":{"__name__":"HostInfo:GPU_utilization_pct","device":"1","instance":"192.168.2.231:9101","job":"nvidia_exporter"},"value":[1521184853.724,"0"]},{"metric":{"__name__":"HostInfo:GPU_utilization_pct","device":"1","instance":"192.168.2.232:9101","job":"nvidia_exporter"},"value":[1521184853.724,"0"]}]}}'
#GpuMem='{"status":"success","data":{"resultType":"vector","result":[{"metric":{"__name__":"HostInfo:GPU_mem_used","device":"0","instance":"192.168.2.158:9101","job":"nvidia_exporter"},"value":[1521186265.431,"62.882011110257785"]},{"metric":{"__name__":"HostInfo:GPU_mem_used","device":"0","instance":"192.168.2.231:9101","job":"nvidia_exporter"},"value":[1521186265.431,"54.70748162320008"]},{"metric":{"__name__":"HostInfo:GPU_mem_used","device":"0","instance":"192.168.2.232:9101","job":"nvidia_exporter"},"value":[1521186265.431,"35.775741505275285"]},{"metric":{"__name__":"HostInfo:GPU_mem_used","device":"1","instance":"192.168.2.231:9101","job":"nvidia_exporter"},"value":[1521186265.431,"18.912719990154287"]},{"metric":{"__name__":"HostInfo:GPU_mem_used","device":"1","instance":"192.168.2.232:9101","job":"nvidia_exporter"},"value":[1521186265.431,"35.73993891182493"]}]}}'
#Network_receive='{"status":"success","data":{"resultType":"vector","result":[{"metric":{"__name__":"HostInfo:node_network_recive","device":"em1","instance":"192.168.2.158:9100","job":"node_exporter"},"value":[1521186704.442,"3243.828498573974"]},{"metric":{"__name__":"HostInfo:node_network_recive","device":"em1","instance":"192.168.2.231:9100","job":"node_exporter"},"value":[1521186704.442,"1891.5233882497996"]},{"metric":{"__name__":"HostInfo:node_network_recive","device":"em1","instance":"192.168.2.232:9100","job":"node_exporter"},"value":[1521186704.442,"598.6574372723699"]},{"metric":{"__name__":"HostInfo:node_network_recive","device":"em2","instance":"192.168.2.158:9100","job":"node_exporter"},"value":[1521186704.442,"0"]},{"metric":{"__name__":"HostInfo:node_network_recive","device":"em2","instance":"192.168.2.231:9100","job":"node_exporter"},"value":[1521186704.442,"0"]},{"metric":{"__name__":"HostInfo:node_network_recive","device":"em2","instance":"192.168.2.232:9100","job":"node_exporter"},"value":[1521186704.442,"0"]},{"metric":{"__name__":"HostInfo:node_network_recive","device":"em3","instance":"192.168.2.158:9100","job":"node_exporter"},"value":[1521186704.442,"0"]},{"metric":{"__name__":"HostInfo:node_network_recive","device":"em4","instance":"192.168.2.158:9100","job":"node_exporter"},"value":[1521186704.442,"0"]}]}}'
#Network_transmit='{"status":"success","data":{"resultType":"vector","result":[{"metric":{"__name__":"HostInfo:node_network_transmit","device":"em1","instance":"192.168.2.158:9100","job":"node_exporter"},"value":[1521187479.327,"230.86361560132354"]},{"metric":{"__name__":"HostInfo:node_network_transmit","device":"em1","instance":"192.168.2.231:9100","job":"node_exporter"},"value":[1521187479.327,"102.58978739287704"]},{"metric":{"__name__":"HostInfo:node_network_transmit","device":"em1","instance":"192.168.2.232:9100","job":"node_exporter"},"value":[1521187479.327,"19.87841784209013"]},{"metric":{"__name__":"HostInfo:node_network_transmit","device":"em2","instance":"192.168.2.158:9100","job":"node_exporter"},"value":[1521187479.327,"0"]},{"metric":{"__name__":"HostInfo:node_network_transmit","device":"em2","instance":"192.168.2.231:9100","job":"node_exporter"},"value":[1521187479.327,"0"]},{"metric":{"__name__":"HostInfo:node_network_transmit","device":"em2","instance":"192.168.2.232:9100","job":"node_exporter"},"value":[1521187479.327,"0"]},{"metric":{"__name__":"HostInfo:node_network_transmit","device":"em3","instance":"192.168.2.158:9100","job":"node_exporter"},"value":[1521187479.327,"0"]},{"metric":{"__name__":"HostInfo:node_network_transmit","device":"em4","instance":"192.168.2.158:9100","job":"node_exporter"},"value":[1521187479.327,"0"]}]}}'

disk_content=[]
mem_content=[]
gpu_content=[]
gpu_mem_content=[]
network_receive_content=[]
network_transmit_content=[]

disk_table_title=['__name__', 'device', 'fstype', 'instance', 'job', 'mountpoint','value']
mem_table_title=['__name__', 'instance', 'job', 'value']
gpu_table_title=['__name__','device', 'instance', 'job', 'value']
gpu_mem_table_title=['__name__','device', 'instance', 'job', 'value']
network_receive_table_title=['__name__','device', 'instance', 'job', 'value']
network_transmit_table_title=['__name__','device', 'instance', 'job', 'value']

#json_disk_info=json.loads(DiskInfo)
#print(type(json_disk_info))
#json_mem_info=json.loads(MemInfo)
#json_gpu_info=json.loads(GpuInfo)
#json_gpu_mem_info=json.loads(GpuMem)
#json_network_receive_info=json.loads(Network_receive)
#json_network_transmit_info=json.loads(Network_transmit)

json_disk_info=GetInfos().getDiskInfo()
disk_infos=json_disk_info['data']['result']

json_mem_info=GetInfos().getMemInfo()
mem_infos=json_mem_info['data']['result']

json_gpu_info=GetInfos().getGpuUtil()
gpu_infos=json_gpu_info['data']['result']

json_gpu_mem_info=GetInfos().getGpuMemInfo()
gpu_mem_infos=json_gpu_mem_info['data']['result']

json_network_receive_info=GetInfos().getNetworkReceive()
network_receive_infos=json_network_receive_info['data']['result']

json_network_transmit_info=GetInfos().getNetworkTransmit()
network_transmit_infos=json_network_transmit_info['data']['result']


for i in range(len(disk_table_title)):
    sheet1.write(0,i,disk_table_title[i])
for i in range(len(mem_table_title)):
    sheet2.write(0,i,mem_table_title[i])
for i in range(len(gpu_table_title)):
    sheet3.write(0,i,gpu_table_title[i])
for i in range(len(gpu_mem_table_title)):
    sheet4.write(0,i,gpu_mem_table_title[i])
for i in range(len(network_receive_table_title)):
    sheet5.write(0,i,network_receive_table_title[i])
for i in range(len(network_transmit_table_title)):
    sheet6.write(0,i,network_transmit_table_title[i])

for info in disk_infos:
    hostInfo = info['metric']
    value=info['value']
    hostInfo['value']=value[1]
    disk_content.append(list(hostInfo.values()))
#print(disk_content)

for info in mem_infos:
    hostInfo = info['metric']
    value=info['value']
    hostInfo['value']=value[1]
    mem_content.append(list(hostInfo.values()))
#print(mem_content)

for info in gpu_infos:
    hostInfo = info['metric']
    value=info['value']
    hostInfo['value']=value[1]
    gpu_content.append(list(hostInfo.values()))
#print(gpu_content)
for info in gpu_mem_infos:
    hostInfo = info['metric']
    value=info['value']
    hostInfo['value']=value[1]
    gpu_mem_content.append(list(hostInfo.values()))
#print(gpu_mem_content)

for info in network_receive_infos:
    hostInfo = info['metric']
    value=info['value']
    hostInfo['value']=value[1]
    network_receive_content.append(list(hostInfo.values()))
#print(gpu_mem_content)

for info in network_transmit_infos:
    hostInfo = info['metric']
    value=info['value']
    hostInfo['value']=value[1]
    network_transmit_content.append(list(hostInfo.values()))
#print(network_transmit_content)

print("正在导出disk信息....")
for row in range(len(disk_content)):
    for col in range(0,len(disk_content[row])):
        sheet1.write(row+1,col,list(disk_content[row][col]))

print("正在导出memory信息....")
for row in range(len(mem_content)):
    for col in range(0,len(mem_content[row])):
        sheet2.write(row+1,col,list(mem_content[row][col]))

print("正在导出GPU使用率信息....")
for row in range(len(gpu_content)):
    for col in range(0,len(gpu_content[row])):
        sheet3.write(row+1,col,list(gpu_content[row][col]))

print("正在导出显存使用信息....")
for row in range(len(gpu_mem_content)):
    for col in range(0,len(gpu_mem_content[row])):
        sheet4.write(row+1,col,list(gpu_mem_content[row][col]))

print("正在导出网卡接收数据信息....")
for row in range(len(network_receive_content)):
    for col in range(0,len(network_receive_content[row])):
        sheet5.write(row+1,col,list(network_receive_content[row][col]))

print("正在导出网卡发送数据信息....")
for row in range(len(network_transmit_content)):
    for col in range(0,len(network_transmit_content[row])):
        sheet6.write(row+1,col,list(network_transmit_content[row][col]))

book.save('../'+filename)