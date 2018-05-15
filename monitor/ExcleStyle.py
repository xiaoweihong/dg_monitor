#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/7 上午10:47
# @Author : xiaowei
# @Site : 
# @File : ExcleStyle.py
# @Software: PyCharm

import xlwt
class Excle_tool:
    def def_style(self,textSize,bold=True):
        borders = xlwt.Borders()
        borders.left = 1
        borders.right = 1
        borders.top = 1
        borders.bottom = 1
        borders.bottom_colour = 0x3A
        style = xlwt.XFStyle()

##########这部分设置字体#########
        font = xlwt.Font()
        font.name = 'Times New Roman'  # 或者换成外面传进来的参数，这样可以使一个函数定义所有style
        font.bold = bold
        font.height = textSize
        #font.size = 16
        #font.colour_index('...')
        style.font = font
        style.borders=borders

########这部分设置居中格式#######
        alignment = xlwt.Alignment()
        alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平居中
        alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直居中
        style.alignment = alignment

#########还可以添加几个设置颜色，边框的部分##########

        return style