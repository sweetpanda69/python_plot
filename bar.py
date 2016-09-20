# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 16:01:10 2016

@author: dataminer
"""
import pylab as pl
pl.mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
pl.mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('ggplot')
iptv = pd.read_csv('.\\tele')

#Index([u'income', u'month_fee', u'connect', u'conduct_age', u'high_broad_connect'], dtype='object')
#[iptv_boot, iptv_consu_fee]
#Index([u'out_circle', u'in_circle', u'income', u'call', u'month_fee'], dtype='object')
#Index([u'income', u'call', u'flow', u'month_fee'], dtype='object')
def preproccess(data,maxnum):
    data = data.replace(0,np.nan)
    data = data[data < maxnum].dropna()
    return len(data),data
maxnum =200
minnum = 0
zd = 'month_fee'
raw_data = iptv[zd]    
length , data = preproccess(raw_data,maxnum)
plt.figure(figsize = (15,6))
#plt.hist(data,maxnum/5, alpha=0.7)
plt.hist(raw_data, range = [minnum,maxnum] , bins = (maxnum-minnum)/5, alpha=0.7)
plt.ylabel(u'人 数', fontproperties='SimHei',fontsize=14)
plt.xlabel(u'固话 - 套餐月费（元）', fontproperties='SimHei',fontsize=14)

plt.savefig('tele_'+str(zd))
plt.show()


tele = pd.DataFrame()
tele['bfw'] = range(0,101)
data = []
for j in range(0,101):
    data.append(np.nanpercentile(iptv[zd], j))

tele[zd] = data


#percentile = [0,0,46,82]
#plt.plot([46,46], [0,60000],'--')
#################plot the histogram of the data####################
#n, bins, patches = plt.hist(data['income']., 100, normed=True, facecolor='b', alpha=0.7)

#plt.axis([-10, 500,0 ,0.1])
#plt.grid(True)

#x_31 = np.percentile(data['income'], 33.33)
#x_32 = np.percentile(data['income'], 66.66)
#
##plt.annotate(int(x_31), xy = (x_31, 1000), xytext=(x_31-10, 1000+5),arrowprops=dict(facecolor='r', shrink=0.05))
##plt.annotate(int(x_32), xy = (x_32, 1000), xytext=(x_32-10, 1000+5),arrowprops=dict(facecolor='r', shrink=0.05))
#plt.xticks([40,60,80,int(x_31),100,int(x_32),120,140,160])



################get_percentile###########################

#iptv_bfw = pd.DataFrame(columns = iptv.columns)
#tele['bfw'] = range(5,101,5)
#for node in iptv.columns:
#    data = []
#    for j in range(5,100,5):
#        data.append(np.nanpercentile(iptv[node], j))
#    data.append(np.nanpercentile(iptv[node], 99))
#    iptv_bfw[node] = data
#iptv_bfw.to_csv('.\\iptv_bfw.csv')

#######################plot bar##############################
#percentile = pd.read_csv('.\\bfw.csv')
#plt.figure(figsize=(10,6))
###axe1 = plt.subplot(221)
#cols = percentile.columns
#zd = cols[6]
#rect = plt.bar(range(5,101,5), map(int, map(round,percentile[zd])), width = 3, facecolor='y', alpha=0.8, align="center")
#ax1 = plt.gca()
##ax1.set_xticks(1.2+2*5)
#maxn = 250
#plt.xticks(range(5,101,5))
#plt.plot([95,95],[0,maxn],'y--')
#plt.plot([80,80],[0,maxn],'y--')
#plt.plot([50,50],[0,maxn],'y--')
#plt.plot([30,30],[0,maxn],'y--')
#plt.xlim(0,105)

#解决中文显示乱码fontproperties='SimHei'
#plt.ylabel(u'宽带-全源收入（元）', fontproperties='SimHei')
#plt.xlabel(u'百分位数', fontproperties='SimHei')
#
#def autolabel(rects):
#    for rect in rects:
#        height = rect.get_height()
#        plt.text(rect.get_x()+rect.get_width()/2.-3/2., 1.05*height, '%s' % int(round(height)))
#autolabel(rect)
#
#plt.text(10,maxn-50,'$mean={0},  median={1}$'.format(round(percentile[zd].mean()),round(percentile[zd].median())), fontproperties = 'SimHei',fontsize = 15)      
#
##

