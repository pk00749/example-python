import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# # plt.axis()
# l=[-1,1,-10,10]
# plt.axis(l)
# # plt.axhline()
# # plt.axvline()
# # plt.axhline(4)
# plt.show()

#
# N = 5
# menMeans = (20, 35, 30, 35, 27)
# menStd =   (2, 3, 4, 1, 2)
#
# ind = np.arange(N)  # the x locations for the groups
# width = 0.35       # the width of the bars
#
# fig, ax = plt.subplots()
# rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)
#
# womenMeans = (25, 32, 34, 20, 25)
# womenStd = (3, 5, 2, 3, 3)
# rects2 = ax.bar(ind+width, womenMeans, width, color='y', yerr=womenStd)

# add some
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.set_xticks(ind+width)
# ax.set_xticklabels( ('G1', 'G2', 'G3', 'G4', 'G5') )
#
# ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )
#
# def autolabel(rects):
#     # attach some text labels
#     for rect in rects:
#         height = rect.get_height()
#         ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
#                 ha='center', va='bottom')
#
# autolabel(rects1)
# autolabel(rects2)
#
# plt.show()
#
#
# import pandas  as pd
# import  numpy as np
# import matplotlib.pyplot  as plt
# ts=pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
# ts=ts.cumsum()
# ts.plot()
# plt.show()
#
#
#
# df=pd.DataFrame(np.random.randn(1000,4),index=ts.index,columns=list('ABCD'))
# df=df.cumsum()
# df.plot()
# plt.show()




#画柱状图
# df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
# print(np.random.rand(10, 4))
# df2.plot(kind='bar')   #分开并列线束
# df2.plot(kind='bar', stacked=True) #四个在同一个里面显示 百分比的形式
# df2.plot(kind='barh', stacked=True)#纵向显示
# plt.show()


# df4=pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':np.random.randn(1000)-1},columns=list('abc'))
# df4.plot(kind='hist', alpha=0.5)
# df4.plot(kind='hist', stacked=True, bins=20)
# df4['a'].plot(kind='hist', orientation='horizontal',cumulative=True) #cumulative是按顺序排序，加上这个
# plt.show()


# #Area Plot
# df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
# df.plot(kind='area')
# df.plot(kind='area',stacked=False)
# plt.show()


# #散点图
# df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
# df.plot(kind='scatter', x='a', y='b')
# df.plot(kind='scatter', x='a', y='b',color='DarkBlue', label='Group 1')
#
# #饼图
# df = pd.DataFrame(3 * np.random.rand(4, 2), index=['a', 'b', 'c', 'd'], columns=['x', 'y'])
# df.plot(kind='pie', subplots=True, figsize=(8, 4))
# df.plot(kind='pie', subplots=True,autopct='%.2f',figsize=(8, 4)) #显示百分比
# plt.show()
#
#
#
# #画矩阵散点图
# df = pd.DataFrame(np.random.randn(1000, 4), columns=['a', 'b', 'c', 'd'])
# pd.scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')
# plt.show()

import matplotlib.pyplot as plt
import numpy as np



# def f(t):
#     return np.exp(-t) * np.cos(2 * np.pi * t)
#
# if __name__ == '__main__' :
#     t1 = np.arange(0, 5, 0.1)
#     t2 = np.arange(0, 5, 0.02)
#
#     plt.figure(12)
#     plt.subplot(221)
#     plt.plot(t1, f(t1), 'bo', t2, f(t2), 'r--')
#
#     plt.subplot(222)
#     plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
#
#     plt.subplot(212)
#     plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
#
#     plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# plt.figure(1)#创建图表1
# plt.figure(2)#创建图表2
# ax1=plt.subplot(211)#在图表2中创建子图1
# ax2=plt.subplot(212)#在图表2中创建子图2
# x=np.linspace(0,3,100)
# for i in range(5):
#     plt.figure(1)
#     plt.plot(x,np.exp(i*x/3))
#     plt.sca(ax1)
#     plt.plot(x,np.sin(i*x))
#     plt.sca(ax2)
#     plt.plot(x,np.cos(i*x))
# plt.show()


#
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib as mpl
#
# mpl.rcParams['font.family'] = 'sans-serif'
# mpl.rcParams['font.sans-serif'] = [u'SimHei']
# mpl.rcParams['axes.unicode_minus'] = False
#
# data = np.random.randint(1, 5, [3, 4])
# index = np.arange(data.shape[1])
# color_index = ['r', 'g', 'b']
#
# fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize = (5, 12))
#
# for i in range(data.shape[0]):
#     ax1.bar(index + i*.25 + .1, data[i], width = .25, color = color_index[i],\
#     alpha = .5)
#
# for i in range(data.shape[0]):
#     ax2.bar(index + .25, data[i], width = .5, color = color_index[i],\
#     bottom = np.sum(data[:i], axis = 0), alpha = .7)
#
# ax3.barh(index, data[0], color = 'r', alpha = .5)
# ax3.barh(index, -data[1], color = 'b', alpha = .5)
#
# plt.show()
# plt.savefig('complex_bar_chart')

# """
# =============================================================
# Demo of the histogram (hist) function with multiple data sets
# =============================================================
#
# Plot histogram with multiple sample sets and demonstrate:
#
#     * Use of legend with multiple sample sets
#     * Stacked bars
#     * Step curve with no fill
#     * Data sets of different sample sizes
#
# Selecting different bin counts and sizes can significantly affect the
# shape of a histogram. The Astropy docs have a great section on how to
# select these parameters:
# http://docs.astropy.org/en/stable/visualization/histogram.html
# """
# import numpy as np
# import matplotlib.pyplot as plt
#
# np.random.seed(0)
#
# n_bins = 10
# x = np.random.randn(1000, 3)
#
# fig, axes = plt.subplots(nrows=2, ncols=2)
# ax0, ax1, ax2, ax3 = axes.flatten()
#
# colors = ['red', 'tan', 'lime']
# ax0.hist(x, n_bins, normed=1, histtype='bar', color=colors, label=colors)
# ax0.legend(prop={'size': 10})
# ax0.set_title('bars with legend')
#
# ax1.hist(x, n_bins, normed=1, histtype='bar', stacked=True)
# ax1.set_title('stacked bar')
#
# ax2.hist(x, n_bins, histtype='step', stacked=True, fill=False)
# ax2.set_title('stack step (unfilled)')
#
# # Make a multiple-histogram of data-sets with different length.
# x_multi = [np.random.randn(n) for n in [10000, 5000, 2000]]
# ax3.hist(x_multi, n_bins, histtype='bar')
# ax3.set_title('different sample sizes')
#
# fig.tight_layout()
# plt.show()



# """
# ========
# Barchart
# ========
#
# A bar plot with errorbars and height labels on individual bars
# """
# import numpy as np
# import matplotlib.pyplot as plt
#
# N = 5
# men_means = (20, 35, 30, 35, 27)
# men_std = (2, 3, 4, 1, 2)
#
# ind = np.arange(N)  # the x locations for the groups
# width = 0.35       # the width of the bars
#
# fig, ax = plt.subplots()
# rects1 = ax.bar(ind, men_means, width, color='r', yerr=men_std)
#
# women_means = (25, 32, 34, 20, 25)
# women_std = (3, 5, 2, 3, 3)
# # rects2 = ax.bar(ind + width, women_means, width, color='y', yerr=women_std)
#
# # add some text for labels, title and axes ticks
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.set_xticks(ind + width / 2)
# ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
#
# # ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))
#
#
# def autolabel(rects):
#     """
#     Attach a text label above each bar displaying its height
#     """
#     for rect in rects:
#         height = rect.get_height()
#         print(rect.get_x())
#         ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
#                 '%d' % int(height),
#                 ha='center', va='bottom')
#
# autolabel(rects1)
# # autolabel(rects2)
#
# plt.show()



import matplotlib.pyplot as plt
import numpy as np

# import matplotlib.cbook as cbook
#
# fname = cbook.get_sample_data('msft.csv', asfileobj=False)
# fname2 = cbook.get_sample_data('data_x_x2_x3.csv', asfileobj=False)

# test 1; use ints
# plt.plotfile(fname, (0, 5, 6))
#
# # test 2; use names
# plt.plotfile(fname, ('date', 'volume', 'adj_close'))
#
# # test 3; use semilogy for volume
# plt.plotfile(fname, ('date', 'volume', 'adj_close'),
#              plotfuncs={'volume': 'semilogy'})
#
# # test 4; use semilogy for volume
# plt.plotfile(fname, (0, 5, 6), plotfuncs={5: 'semilogy'})
#
# # test 5; single subplot
# plt.plotfile(fname, ('date', 'open', 'high', 'low', 'close'), subplots=False)
#
# # test 6; labeling, if no names in csv-file
# plt.plotfile(fname2, cols=(0, 1, 2), delimiter=' ',
#              names=['$x$', '$f(x)=x^2$', '$f(x)=x^3$'])
#
# # test 7; more than one file per figure--illustrated here with a single file
# plt.plotfile(fname2, cols=(0, 1), delimiter=' ')
# plt.plotfile(fname2, cols=(0, 2), newfig=False,
#              delimiter=' ')  # use current figure
# plt.xlabel(r'$x$')
# plt.ylabel(r'$f(x) = x^2, x^3$')

# test 8; use bar for volume
# plt.plotfile(fname, (0, 5, 6), plotfuncs={5: 'bar'})
#
# plt.show()


#
# import matplotlib as mpl
#
#
# mpl.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
#
# mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
#
# mpl.rc('xtick', labelsize=20) #设置坐标轴刻度显示大小
#
# mpl.rc('ytick', labelsize=20)
#
# font_size=30


from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

xmajorLocator   = MultipleLocator(10) #将x主刻度标签设置为20的倍数
xmajorFormatter = FormatStrFormatter('%1.1f') #设置x轴标签文本的格式
xminorLocator   = MultipleLocator(5) #将x轴次刻度标签设置为5的倍数

ymajorLocator   = MultipleLocator(0.5) #将y轴主刻度标签设置为0.5的倍数
ymajorFormatter = FormatStrFormatter('%1.1f') #设置y轴标签文本的格式
yminorLocator   = MultipleLocator(0.1) #将此y轴次刻度标签设置为0.1的倍数

t = arange(0.0, 100.0, 1)
s = sin(0.1*pi*t)*exp(-t*0.01)

ax = subplot(111) #注意:一般都在ax中设置,不再plot中设置
plot(t,s,'--b*')

#设置主刻度标签的位置,标签文本的格式
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)

ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)

#显示次刻度标签的位置,没有标签文本
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.grid(True, which='major') #x坐标轴的网格使用主刻度
ax.yaxis.grid(True, which='minor') #y坐标轴的网格使用次刻度

show()