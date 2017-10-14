#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#1获取股票数据，修改最下面的i表示从哪里开始
#需要用到文件夹中stodata.xlsx中的股票代码
#如果trade为360，那么文件大小小于16k的删除
#如果trade为720，那么文件大小小于23k的删除
#如果trade为900，那么文件大小小于27k的删除
import numpy as np 
import pandas as pd
import statsmodels.tsa.stattools as ts
import tushare as tsh
from pandas import Series,DataFrame
import os,re

r = re.compile('\d+')
ns = len(list(pd.read_excel(r'G:\程序代码\PY文件\小任务\自己\量化\代码\stodata.xlsx')[0]))

def get_st_data(st):
    
    stolist = list(pd.read_excel(r'G:\程序代码\PY文件\小任务\自己\量化\代码\stodata.xlsx')[0])
    stolist = [str(s) for s in stolist]

    for s in range((st-1),len(stolist)):
        print(s+1)
        if len(stolist[s]) < 6:
            di = 6 - len(stolist[s])
            stolist[s] = '0'*di+stolist[s]
        x = tsh.get_k_data(stolist[s],start='2013-01-01',end='2017-10-10',pause=3)
        xcl = x[['date','close']]
        xcl.to_excel(r'G:\程序代码\PY文件\小任务\自己\量化\结果\stock\\'+str(s+1)+'  '+stolist[s]+'.xlsx')
        

if __name__ == '__main__':
    l = None
    flag = 0
    i = None
    try:
        os.listdir(r'G:\程序代码\PY文件\小任务\自己\量化\结果\stock')
    except:
        os.mkdir(r'G:\程序代码\PY文件\小任务\自己\量化\结果\stock')
    while i != ns:
        l = os.listdir(r'G:\程序代码\PY文件\小任务\自己\量化\结果\stock')
        l = [i for i in l if i.endswith('.xlsx')]
        if l:
            i = max([int(r.match(i).group()) for i in l])
        else:
            i = 1
        try:
            get_st_data(i)
        except KeyError:
            print('KeyError:',i)
        except :
            print('except:',i)
