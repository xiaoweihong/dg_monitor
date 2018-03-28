#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/3/26 上午10:47
# @Author : xiaowei
# @Site : 
# @File : HostInfo.py
# @Software: PyCharm
import requests

prometheusIp = 'http://192.168.2.158:9090'

DiskInfoUrl = prometheusIp + '/api/v1/query?query=HostInfo:Disk_usage'
MemInfoUrl = prometheusIp + '/api/v1/query?query=HostInfo:Mem_used'
GpuInfoUrl = prometheusIp + '/api/v1/query?query=HostInfo:GPU_utilization_pct'
GpuMemUrl = prometheusIp + '/api/v1/query?query=HostInfo:GPU_mem_used'
Net_receive_Url = prometheusIp + '/api/v1/query?query=HostInfo:node_network_receive'
Net_transmit_Url = prometheusIp + '/api/v1/query?query=HostInfo:node_network_transmit'

class GetInfos:



    def getDiskInfo(self):
        DiskInfo=requests.get(DiskInfoUrl)
        return DiskInfo.json()

    def getMemInfo(self):
        MemInfo=requests.get(MemInfoUrl)
        return MemInfo.json()

    def getGpuUtil(self):
        GpuInfo=requests.get(GpuInfoUrl)
        return GpuInfo.json()


    def getGpuMemInfo(self):
        GpuMemInfo=requests.get(GpuMemUrl)
        return GpuMemInfo.json()


    def getNetworkReceive(self):
        Network_receiveInfo=requests.get(Net_receive_Url)
        return Network_receiveInfo.json()

    def getNetworkTransmit(self):
        Network_transmitInfo=requests.get(Net_transmit_Url)
        return Network_transmitInfo.json()

    def getTitle(self,titleInfo):
        title_temp = titleInfo[0]['metric']
        title_content=[]
        for title in title_temp:
            title_content.append(title)
        title_content.append('value')
        return title_content

