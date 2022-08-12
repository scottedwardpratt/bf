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

#corrections because type2 BF denominator not corrected for annihiltation
dfactor_noregen=8.8756/7.18748
dfactor_withregen=8.8756/7.53014

filename_type1='bfdata/type1/bf_qinv.txt'

data1=np.loadtxt(filename_type1,skiprows=0,unpack=True)
x1=data1[0]
bf1=data1[1]
x1=x1*0.001

filename_type2='bfdata/type2/bf_noregeneration_qinv.txt'
data2=np.loadtxt(filename_type2,skiprows=0,unpack=True)
x2=data2[0]/1000
bf_noregeneration=data2[1]
bfsum_noregeneration=bf1*dfactor_noregen+bf_noregeneration

filename_type2='bfdata/type2/bf_withregeneration_qinv.txt'
data2=np.loadtxt(filename_type2,skiprows=0,unpack=True)
x2=data2[0]/1000
bf_withregeneration=data2[1]
bfsum_withregeneration=bf1*dfactor_withregen+bf_withregeneration


filename_type2='bfdata/type2/bf_noannihilation_qinv.txt'
data2=np.loadtxt(filename_type2,skiprows=0,unpack=True)
x2=data2[0]/1000
bf_noannihilation=data2[1]
bfsum_noannihilation=bf1+bf_noannihilation

bbff1=[None]*100
bbff_withregeneration=[None]*100
bbff_noregeneration=[None]*100
bbffsum_withregeneration=[None]*100
bbffsum_noregeneration=[None]*100
xx1=[None]*100
xx2=[None]*100
bbff1=[None]*100
for i in range(0,100):
  bbff1[i]=(bf1[3*i]+bf1[3*i+1]+bf1[3*i+2])/3.0
  bbff_withregeneration[i]=(bf_withregeneration[3*i]+bf_withregeneration[3*i+1]+bf_withregeneration[3*i+2])/3.0
  bbff_noregeneration[i]=(bf_noregeneration[3*i]+bf_noregeneration[3*i+1]+bf_noregeneration[3*i+2])/3.0
  bbffsum_withregeneration[i]=bbff_withregeneration[i]+bbff1[i]*dfactor_withregen
  bbffsum_noregeneration[i]=bbff_noregeneration[i]+bbff1[i]*dfactor_noregen
  xx1[i]=x1[3*i+1]
  xx2[i]=x2[3*i+1]


#x2=np.delete(x2,range(30,50,1))
#y2=np.delete(y2,range(30,50,1))

#y=1.13*y1+y2

xx0=0.18
width=0.96-xx0
yy0=0.11
height=0.985-yy0
ax = fig.add_axes([xx0,yy0,width,height])

plt.plot([0,5],[0,0],linestyle='dashed',color='grey')

ymin=-0.1
ymax=0.65
plt.plot(xx1,bbff1,linestyle='-',linewidth=3,color='r',markersize=8, marker='o',markerfacecolor='r',label='no annihilations')
#plt.plot(x1,bfsum_noannihilation,linestyle='-',linewidth=3,color='r',markersize=6, marker='o',markerfacecolor='r',label='No annihilations')
#plt.plot(x2,bfsum_noregeneration,linestyle='-',linewidth=3,color='g',markersize=6, marker='o',markerfacecolor='g',label='with annihilations')
#plt.plot(x2,bfsum_withregeneration,linestyle='-',linewidth=3,color='k',markersize=6, marker='o',markerfacecolor='k',label='with regeneration')
#plt.plot(x1,y,linestyle='-',linewidth=3,color='k',markersize=6, marker='o',markerfacecolor='none',label='Sum')

plt.plot(xx2,bbffsum_noregeneration,linestyle='-',linewidth=3,color='g',markersize=8, marker='^',markerfacecolor='g',label='with annihilations')

plt.plot(xx2,bbffsum_withregeneration,linestyle='-',linewidth=3,color='k',markersize=8, marker='s',markerfacecolor='k',label='plus regeneration')

legend(loc=(0.05,0.8),fontsize=18)

ax.set_xticks(np.arange(0,2,0.5), minor=False)
ax.set_xticks(np.arange(0,2,0.1), minor=True)
ax.set_xticklabels(np.arange(0,2,0.5),minor=False,size=18, family='serif')
ax.set_yticks(np.arange(-1,1,0.2), minor=False)
ax.set_yticklabels(np.arange(-1,1,0.2), minor=False, family='serif', size=18)
ax.set_yticks(np.arange(-1,1,0.1), minor=True)

xlim(0,1.5)
ylim(ymin,ymax)

plt.xlabel('$q_{\\rm inv}$ [GeV$/c$]',fontsize=24, family='serif',labelpad=0)
plt.ylabel('$B(q_{\\rm inv})$ [(GeV/$c$)$^{-1}$]',fontsize=24,family='serif',labelpad=1)
    
ax.xaxis.set_major_formatter(sformatter)
ax.yaxis.set_major_formatter(sformatter)

text(1.45,0.8,'(c)',fontsize=22,ha='right')

filename='bfvsqinv.pdf'
plt.savefig(filename,format='pdf')
os.system('open -a Preview '+filename)
#plt.show()

quit()
