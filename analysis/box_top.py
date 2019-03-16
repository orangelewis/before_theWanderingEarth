# -*- coding: utf-8 -*-
__author__ = 'CL'
__date__ = '2019/2/15 12:59 AM'
from pyecharts import Bar
import pandas as pd
import numpy as np
import pymysql
import xlrd

total_sum = {}
yi = 100000000
wan = 10000
total_sum['2011'] = 131*yi
total_sum['2012'] = 171*yi
total_sum['2013'] = 218*yi
total_sum['2014'] = 296*yi
total_sum['2015'] = 441*yi
total_sum['2016'] = 454*yi
total_sum['2017'] = 558*yi
total_sum['2018'] = 606*yi
total_sum['2019'] = 115*yi


def excel_reader(file_name,sheet_num = 0):
    import xlrd

    book = xlrd.open_workbook(file_name, formatting_info=False)
    table = book.sheet_by_index(sheet_num)

    dict2 = {}

    colsNum = table.ncols
    rowsNum = table.nrows

    a = table.row_values(0)
    b = table.row_values(1)
    ab = dict(zip(a,b))

    for i in range(1 , rowsNum):
        c = table.row_values(i,0,colsNum)
        dict1 = dict(zip(ab,c))
        dict2[i] = dict1

    return dict2

if __name__ == '__main__':
    file_name = "movie.xls"
    sheet_num = 1
    data = excel_reader(file_name,sheet_num)


    data_list = []

    for item in data.items():
        pass
        data_1 = {}

        data_1['name'] = item[1]['name']
        # print(data_1['name'])

        total_box = item[1]['total_china_box']


        if isinstance(total_box,float) :
            continue

        if total_box[-1] == "万":
            data_1['sum_score'] = (float(item[1]['total_china_box'][0:-1])*wan)/(total_sum[item[1]['year']])
        if total_box[-1] == "亿":
            year_total = total_sum[item[1]['year']]
            data_1['sum_score'] = (float(item[1]['total_china_box'][0:-1])*yi)/year_total
        else:
            continue
        data_list.append(data_1)
    data_list = sorted(data_list , key=lambda item:item["sum_score"] ,reverse=True)


    list1 = []
    list2 = []
    for item in data_list:


        s = item['name']

        import re


        list1.append(s)
        list2.append('%.2f' %(item['sum_score']*1000))

    attr = np.array(list1[0:10])
    v1 = np.array(list2[0:10])

    bar = Bar("2011-2018年科幻电影票房占比TOP10(‰)", title_pos='center', title_top='18', width=1400, height=400)
    bar.add("", attr, v1, is_convert=True, xaxis_min=10, yaxis_label_textsize=12, is_yaxis_boundarygap=True,
            yaxis_interval=0, is_label_show=True, is_legend_show=False, label_pos='right', is_yaxis_inverse=True,
            is_splitline_show=False)
    bar.render("2011-2018年科幻电影票房占比TOP10.html")

    pass





