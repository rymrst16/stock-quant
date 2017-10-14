#4计算现价与股票的均值的差（天数为adf.py中设置的天数）
#getdif_now_mean将运算结果存入文件夹res方便以后进行查看
import pandas as pd
from pandas import Series,DataFrame
import os,re
import salo
import tushare as ts 
import numpy as np

#level参数可以写'one'、'five'、'ten'，分别处理1%、5%和10%的股票,adftrade是算adf时的交易时长，即等于adf.py中函数的参数,chocur为选择的需要和adftrade比较的时间（可以是一周，或者一个月等）
#返回字典中存的是列表，第一个数是adftrade时期的均值，第二个为chocur时期的均值
def choose(level,adftrade=None,chocur=None):
    allst = os.listdir(r'G:\程序代码\PY文件\小任务\自己\量化\结果\stock')
    stlist = pd.read_excel(r'G:\程序代码\PY文件\小任务\自己\量化\结果\adf\\'+level+'.xlsx',header=None,dtype=str)
    stlist = list(stlist[0])
    primea = {}
    for st in stlist:
        for sest in allst:
            if (st+'.xlsx') in sest.split():
                thisst = sest
                break;
        c = pd.read_excel(r'G:\程序代码\PY文件\小任务\自己\量化\结果\stock\\'+thisst)
        if adftrade is not None:
            cadftrade = c.close[-adftrade:]
            cchocur = c.close[-chocur:]
        else:
            cadftrade = c.close
            cchocur = c.close[-chocur:]
        meancadftrade = np.average(Series(cadftrade))
        meanchocur = np.average(Series(cchocur))
        primea[st] = [meancadftrade,meanchocur]
    return primea

#函数的返回值是一个字典，存着一个五个元素的列表，值分别为trade的均值，chocur的均值，trade的均值和chocur的均值的差值，现价和trade的差值，现价和chocur的差值，然后存在res文件夹中
def getdif_now_mean(level,trade,chocur):
    curpri = ts.get_today_all()
    curpri = curpri[['code','trade']]
    curpri.index = curpri.code
    curpri = curpri.trade
    primea = choose(level,trade,chocur) #第一个值为所有时期的均值，第二个值为level时期的均值
    pridif = {}
    print(primea)
    for st in primea:
        print(st,pridif)
        stcurpri = curpri[st]
        fidi = primea[st][1] - primea[st][0]
        sedi = stcurpri - primea[st][0]
        seth = stcurpri - primea[st][1]
        if fidi<0 and sedi<0 and seth<0:
            pridif[st] = [primea[st][0],primea[st][1],fidi,sedi,seth]
    dataframe = DataFrame(pridif).T
    dataframe.columns = ['adfmean','chocurmean','chocur-trade','current-trade','current-chocur']
    dataframe.to_excel(r'G:\程序代码\PY文件\小任务\自己\量化\结果\res\\'+'res.xlsx')
    return pridif

if __name__ == '__main__':
    print(getdif_now_mean('five',365,30))
