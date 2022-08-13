import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import os
import sys
import codecs
sys.getdefaultencoding()
from pylab import *
from matplotlib import ticker
from matplotlib.ticker import ScalarFormatter
sformatter=ScalarFormatter(useOffset=True,useMathText=True)
sformatter.set_scientific(True)
sformatter.set_powerlimits((-3,3))

acceptance='alice'

font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 12}
plt.rc('font', **font)
plt.rc('text', usetex=False)
linestyles = [
  '_', '-', '--', ':'
]
mstyle = [u'*',u'o']
colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k')

plt.figure(figsize=(6,7))
fig = plt.figure(1)

filename_type1='bfdata/type1/bf_y.txt'
filename_type2='bfdata/type2/bf_noregeneration_y.txt'
filename_type3='bfdata/type2/bf_withregeneration_y.txt'

data1=np.loadtxt(filename_type1,skiprows=0,unpack=True)
x1=data1[0]
y1=data1[1]
data2=np.loadtxt(filename_type2,skiprows=0,unpack=True)
x2=data2[0]
y2=data2[1]
data3=np.loadtxt(filename_type3,skiprows=0,unpack=True)
x3=data3[0]
y3=data3[1]


dfactor_noregen=8.8756/7.18748
dfactor_withregen=8.8756/7.53014

y2=y1*dfactor_noregen+y2
y3=y1*dfactor_withregen+y3

xx0=0.18
width=0.96-xx0
yy0=0.09
height=0.98-yy0
ax = fig.add_axes([xx0,yy0,width,height])

plt.plot([0,5],[0,0],linestyle='dashed',color='grey')

ymin=0
ymax=0.20
plt.plot(x1,y1,linestyle='-',linewidth=3,color='r',markersize=8, marker='o',markerfacecolor='r',label='no annihilations')
plt.plot(x2,y2,linestyle='-',linewidth=3,color='g',markersize=8, marker='^',markerfacecolor='g',label='with annihilations')
plt.plot(x3,y3,linestyle='-',linewidth=3,color='k',markersize=8, marker='s',markerfacecolor='k',label='plus regeneration')

legend(loc=(0.01,0.02),fontsize=18)

ax.set_xticks(np.arange(0,4,0.5), minor=False)
ax.set_xticks(np.arange(0,4,0.1), minor=True)
ax.set_xticklabels(np.arange(0,4,0.5),minor=False,size=18, family='serif')
ax.set_yticks(np.arange(-1,1,0.1), minor=False)
ax.set_yticklabels(np.arange(-1,1,0.1), minor=False, family='serif', size=18)
ax.set_yticks(np.arange(-1,1,0.05), minor=True)

xlim(0,1.3)
ylim(ymin,ymax)

plt.xlabel('$\\Delta y$',fontsize=24, family='serif',labelpad=-6)
plt.ylabel('$B(\\Delta y)$',fontsize=24,family='serif',labelpad=0)
    
ax.xaxis.set_major_formatter(sformatter)
ax.yaxis.set_major_formatter(sformatter)

text(1.28,0.47,'(a)',fontsize=22,ha='right')

filename='bfvsy.pdf'
plt.savefig(filename,format='pdf')
os.system('open -a Preview '+filename)
#plt.show()

quit()
