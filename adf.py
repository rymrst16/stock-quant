#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2计算adf，参数为多少日adf
import pandas as pd
from pandas import Series,DataFrame
import os,re
import statsmodels.tsa.stattools as ts
import salo #在自己定义的文件中

r = re.compile(r'\d+\s+(\d+)')
dirlist = os.listdir(r'G:\程序代码\PY文件\小任务\自己\量化\结果\stock\\')
dirlist = [d for d in dirlist if r.match(d)]
#dirlist = [r.match(d).group(1) for d in dirlist if r.match(d)]

def adf(traday=None):
    stoadf = {}

    for sto in dirlist:
        print(sto)
        stoda = pd.read_excel(r'G:\程序代码\PY文件\小任务\自己\量化\结果\stock\\'+sto)
        if traday is not None:
            stoda = stoda.close[-traday:]
        else:
            stoda = stoda.close
        sto = r.match(sto).group(1)
        adf = ts.adfuller(stoda,1)[0]
        stoadf[sto] = adf
    return stoadf

if __name__ == '__main__':
    stoadf = adf(365)
    print(stoadf)
    salo.save(r'G:\程序代码\PY文件\小任务\自己\量化\结果\stoadf',stoadf=stoadf)