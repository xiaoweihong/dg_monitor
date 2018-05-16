#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/16 下午2:21
# @Author : xiaowei
# @Site : 
# @File : DeepDataPgInfo.py
# @Software: PyCharm
import psycopg2

class DeepVideoPostgresTool:
    def __init__(self,database,host):
        self.database=database
        self.user='postgres'
        self.password='123456'
        self.host=host
        self.port="5432"

    def getConnect(self):
        conn=psycopg2.connect(database=self.database,user=self.user,password=self.password,host=self.host,port=self.port)
        return conn

    def getVehicle(self):
        conn=self.getConnect()
        cur=conn.cursor()
        cur.execute("SELECT COUNT(*) FROM VEHICLES")
        vehicles=cur.fetchall()
        conn.close()
        return vehicles

    def getNonmontor(self):
        conn=self.getConnect()
        cur=conn.cursor()
        cur.execute("SELECT COUNT(*) FROM NONMOTORS")
        nonmotors=cur.fetchall()
        conn.close()
        return nonmotors

    def getPedestrians(self):
        conn=self.getConnect()
        cur=conn.cursor()
        cur.execute("SELECT COUNT(*) FROM PEDESTRIANS")
        pedestrians=cur.fetchall()
        conn.close()
        return pedestrians

    def getDeepDataInfo(self):
        deepdata = {"vehicles": None, "nonmotors": None, "pedestrians": None}
        deepdata["vehicles"]=self.getVehicle()[0][0]
        deepdata["nonmotors"]=self.getNonmontor()[0][0]
        deepdata["pedestrians"]=self.getPedestrians()[0][0]
        return deepdata

if __name__=='__main__':
    pg=DeepVideoPostgresTool(database='deepdata_v6',host="192.168.2.158")
    print(pg.getVehicle()[0][0])
    print(pg.getNonmontor())
    print(pg.getPedestrians())
    print(pg.getDeepDataInfo())
