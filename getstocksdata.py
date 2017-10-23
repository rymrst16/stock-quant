#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#1获取股票数据，修改最下面的i表示从哪里开始
#需要用到文件夹中stodata.xlsx中的股票代码
#如果trade为360，那么文件大小小于16k的删除
#如果trade为720，那么文件大小小于23k的删除
#如果trade为900，那么文件大小小于27k的删除
import time
import os
import re
from threading import Thread
import statsmodels.tsa.stattools as ts
import numpy as np 
import pandas as pd
from pandas import Series,DataFrame
import tushare as tsh

r = re.compile('\d+')
r1 = re.compile('\s+')
ns = len(list(pd.read_excel(r'G:\程序代码\PY文件\小任务\自己\量化\代码\stodata.xlsx')[0]))

def get_st_data(st_info):
        print(st_info[0])
        if len(str(st_info[1])) < 6:
            di = 6 - len(st_info[1])
            st_info[1] = '0'*di + str(st_info[1])
        x = tsh.get_k_data(str(st_info[1]),start='2010-01-01',end='2017-10-23',pause=10)
        xcl = x[['date','close']]
        xcl.to_excel(r'G:\程序代码\PY文件\小任务\自己\量化\结果\stock\\'+str(st_info[0])+'  '+str(st_info[1])+'.xlsx')

if __name__ == '__main__':
    s_time = time.time()
    try:
        l = os.listdir(r'G:\程序代码\PY文件\小任务\自己\量化\结果\stock')
    except:
        os.mkdir(r'G:\程序代码\PY文件\小任务\自己\量化\结果\stock')
        l = os.listdir(r'G:\程序代码\PY文件\小任务\自己\量化\结果\stock')
        l = [i for i in l if i.endswith('.xlsx')]
    stolist = [s for s in enumerate(list(pd.read_excel(r'G:\程序代码\PY文件\小任务\自己\量化\代码\stodata.xlsx')[0]),1) if s[1] not in [int(r1.split(i)[1].split('.')[0]) for i in l ]]    #将股票文件中的股票列表和他们的编号列出来,注意，代码是数值型，因此前面的0会去掉
    stolist = stolist[::-1]
        
    def get_stock_data(stolist):
        while stolist:
            st_info = stolist.pop() #即stolist的元素，前面为编号，后面为股票数值代码
            try:
                get_st_data(st_info)
            except:
                stolist.append(st_info)
                print('%d fail' % (st_info[0],))
                time.sleep(600)

    all_thread = {}
    for i in range(100):   #线程数量自己设定
        t = Thread(target=get_stock_data,args=(stolist,))
        all_thread[i] = t
        t.start()
    for i in range(100):  #线程数量自己设定
        all_thread[i].join()
    e_time = time.time()
    print('run %ds' % ((e_time-s_time),))


