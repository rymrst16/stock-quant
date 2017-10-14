#3 分类，分别为1%，5%和10%下平稳的股票存在文件夹adf下
import pandas as pd
from pandas import Series,DataFrame
import os,re
import statsmodels.tsa.stattools as ts
import salo


def runcal():
    onep = -4.9386902332361515;fivep = -3.4775828571428571;tenp = -2.8438679591836733
    stoadf = salo.load(r'G:\程序代码\PY文件\小任务\自己\量化\结果\stoadf')['stoadf']

    one = [] ; five = [] ; ten = [] ; oth = []

    for st in stoadf:
        adf = stoadf[st]
        if abs(adf) > abs(onep):
            one.append(st)
        elif abs(adf) > abs(fivep):
            five.append(st)
        elif abs(adf) > abs(tenp):
            ten.append(st)
        else:
            oth.append(st)

    one = Series(one);five = Series(five);ten = Series(ten);oth = Series(oth)
    one.to_excel(r'G:\程序代码\PY文件\小任务\自己\量化\结果\adf\one.xlsx',index=False,header=False)
    five.to_excel(r'G:\程序代码\PY文件\小任务\自己\量化\结果\adf\five.xlsx',index=False,header=False)
    ten.to_excel(r'G:\程序代码\PY文件\小任务\自己\量化\结果\adf\ten.xlsx',index=False,header=False)
    oth.to_excel(r'G:\程序代码\PY文件\小任务\自己\量化\结果\adf\oth.xlsx',index=False,header=False)

if __name__ == '__main__':
    runcal()

