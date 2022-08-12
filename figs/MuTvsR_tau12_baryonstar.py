import sys
import os
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from pylab import *
from matplotlib import ticker
#from matplotlib.ticker import ScalarFormatter
#sformatter=ScalarFormatter(us0eOffset=True,useMathText=True)
#sformatter.set_scientific(True)
#sformatter.set_powerlimits((-2,3))


tau=12
#tau=int(input('Enter tau: '))
plt.figure(figsize=(5,11))
fig=plt.figure(1)

filename='data/muTvsR_B4_tau'+str(tau)+'.txt'
B0data = np.loadtxt(filename,skiprows=0,unpack=True)
rB0=B0data[0]
NB0=B0data[1]
TB0=B0data[2]
UB0=B0data[3]
muB0=B0data[4]
rhoB0=tau*B0data[5]
UB0_alt=B0data[7]
filename='data/muTvsR_B5_tau'+str(tau)+'.txt'
B1data = np.loadtxt(filename,skiprows=0,unpack=True)
rB1=B1data[0]
NB1=B1data[1]
TB1=B1data[2]
UB1=B1data[3]
muB1=B1data[4]
rhoB1=tau*B1data[5]
UB1_alt=B1data[7]
filename='data/muTvsR_B6_tau'+str(tau)+'.txt'
B2data = np.loadtxt(filename,skiprows=0,unpack=True)
rB2=B2data[0]
NB2=B2data[1]
TB2=B2data[2]
UB2=B2data[3]
muB2=B2data[4]
rhoB2=tau*B2data[5]
UB2_alt=B2data[7]
filename='data/muTvsR_B7_tau'+str(tau)+'.txt'
B3data = np.loadtxt(filename,skiprows=0,unpack=True)
rB3=B3data[0]
NB3=B3data[1]
TB3=B3data[2]
UB3=B3data[3]
muB3=B3data[4]
rhoB3=tau*B3data[5]
UB3_alt=B3data[7]

#######################################

ax = fig.add_axes([0.19,0.06,0.8,0.23])

plt.plot(rB0,1000*TB0,linestyle='-',color='r',markersize=6,marker='o',markerfacecolor='r')
plt.plot(rB1,1000*TB1,linestyle='-',color='g',markersize=6,marker='s',markerfacecolor='g')
plt.plot(rB2,1000*TB2,linestyle='-',color='b',markersize=6,marker='^',markerfacecolor='b')
plt.plot(rB3,1000*TB3,linestyle='-',color='k',markersize=6,marker='v',markerfacecolor='k')

ax.tick_params(axis='both', which='major', labelsize=14)

ax.set_xticks(np.arange(0,31,10), minor=False)
ax.set_xticklabels(np.arange(0,31,10), minor=False, family='sans', fontsize=16)
ax.set_xticks(np.arange(0,31,5), minor=True)
#ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0f'))
plt.xlim(0,25)

ax.set_yticks(np.arange(0,200,40), minor=False)
ax.set_yticklabels(np.arange(0,200,40), minor=False, family='sans', fontsize=16)
ax.set_yticks(np.arange(0,200,20), minor=True)
plt.ylim(20,170)
#ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1e'))
#ax.yaxis.set_major_formatter(sformatter)

plt.xlabel('$r$ [fm]', fontsize=22, weight='normal')
plt.ylabel('$T$ [MeV]',fontsize=22, weight='normal')
text(25,26.0,"(l)",fontsize=20,ha='right')

#######################################

ax = fig.add_axes([0.19,0.29,0.8,0.23])

plt.plot(rB0,rhoB0,linestyle='-',color='r',markersize=6,marker='o',markerfacecolor='r',label='$\\Delta$')
plt.plot(rB1,rhoB1,linestyle='-',color='g',markersize=6,marker='s',markerfacecolor='g',label='$\\Sigma^*$')
plt.plot(rB2,rhoB2,linestyle='-',color='b',markersize=6,marker='^',markerfacecolor='b',label='$\\Xi^*$')
plt.plot(rB3,rhoB3,linestyle='-',color='k',markersize=6,marker='v',markerfacecolor='k',label='$\\Omega$')

legend(loc=(0.68,0.35),fontsize=18)

ax.tick_params(axis='both', which='major', labelsize=14)

ax.set_xticks(np.arange(0,31,10), minor=False)
ax.set_xticklabels([])
ax.set_xticks(np.arange(0,31,5), minor=True)
#ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0f'))
plt.xlim(0,25)

ax.set_yticks(np.arange(0,0.5,0.04), minor=False)
ax.set_yticklabels(np.arange(0,0.5,0.04), minor=False, family='sans', fontsize=16)
ax.set_yticks(np.arange(0,0.5,0.02), minor=True)
plt.ylim(0,0.15)
#ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1e'))
#ax.yaxis.set_major_formatter(sformatter)

plt.xlabel(None)
plt.ylabel('$\\rho\\tau~$ [fm$^{-2}$]',fontsize=22,labelpad=-1)
text(25,0.01,"(k)",fontsize=20,ha='right')

#######################################

ax = fig.add_axes([0.19,0.52,0.8,0.23])

x=np.array([],dtype=float)
y=np.array([],dtype=float)
s=np.prod(NB0.shape)
for i in range(0,s):
	if NB0[i]>4 :
		x=np.append(x,rB0[i])
		y=np.append(y,UB0[i])
plt.plot(x,y,linestyle='-',color='r',markersize=6,marker='o',markerfacecolor='r')

x=np.array([],dtype=float)
y=np.array([],dtype=float)
s=np.prod(NB1.shape)
for i in range(0,s):
	if NB1[i]>4 :
		x=np.append(x,rB1[i])
		y=np.append(y,UB1[i])
plt.plot(x,y,linestyle='-',color='g',markersize=6,marker='s',markerfacecolor='g')


x=np.array([],dtype=float)
y=np.array([],dtype=float)
s=np.prod(NB2.shape)
for i in range(0,s):
	if NB2[i]>4 :
		x=np.append(x,rB2[i])
		y=np.append(y,UB2[i])
plt.plot(x,y,linestyle='-',color='b',markersize=6,marker='^',markerfacecolor='b')


x=np.array([],dtype=float)
y=np.array([],dtype=float)
s=np.prod(NB3.shape)
for i in range(0,s):
	if NB3[i]>4 :
		x=np.append(x,rB3[i])
		y=np.append(y,UB3[i])
plt.plot(x,y,linestyle='-',color='k',markersize=6,marker='v',markerfacecolor='k')
#plt.plot(x,z,linestyle='-',color='b',markersize=6,marker='s',markerfacecolor='b')

ax.tick_params(axis='both', which='major', labelsize=14)

ax.set_xticks(np.arange(0,31,10), minor=False)
#ax.set_xticklabels(np.arange(0,31,10), minor=False, family='sans')
ax.set_xticklabels([])
ax.set_xticks(np.arange(0,31,5), minor=True)
#ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0f'))
plt.xlim(0,25)

ax.set_yticks(np.arange(0,6,1.0), minor=False)
ax.set_yticklabels(np.arange(0,6,1.0), minor=False, family='sans', fontsize=16)
ax.set_yticks(np.arange(0,6,0.2), minor=True)
plt.ylim(0,2.5)
#ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1e'))
#ax.yaxis.set_major_formatter(sformatter)

plt.xlabel(None)
plt.ylabel('$u_r$ ',fontsize=22)
text(25,0.2,"(j)",fontsize=20,ha='right')

#######################################

ax = fig.add_axes([0.19,0.75,0.80,0.23])

x=np.array([],dtype=float)
y=np.array([],dtype=float)
s=np.prod(NB0.shape)
for i in range(0,s):
	if NB0[i]>100 :
		x=np.append(x,rB0[i])
		y=np.append(y,muB0[i])
plt.plot(x,y,linestyle='-',color='r',markersize=6,marker='o',markerfacecolor='r')

x=np.array([],dtype=float)
y=np.array([],dtype=float)
s=np.prod(NB0.shape)
for i in range(0,s):
	if NB1[i]>10 :
		x=np.append(x,rB1[i])
		y=np.append(y,muB1[i])
plt.plot(x,y,linestyle='-',color='g',markersize=6,marker='s',markerfacecolor='g')

x=np.array([],dtype=float)
y=np.array([],dtype=float)
s=np.prod(NB2.shape)
for i in range(0,s):
	if NB2[i]>10 :
		x=np.append(x,rB2[i])
		y=np.append(y,muB2[i])
plt.plot(x,y,linestyle='-',color='b',markersize=6,marker='^',markerfacecolor='b')

x=np.array([],dtype=float)
y=np.array([],dtype=float)
s=np.prod(NB3.shape)
for i in range(0,s):
	if NB3[i]>10 :
		x=np.append(x,rB3[i])
		y=np.append(y,muB3[i])
plt.plot(x,y,linestyle='-',color='k',markersize=6,marker='v',markerfacecolor='k')

ax.tick_params(axis='both', which='major', labelsize=14)

ax.set_xticks(np.arange(0,31,10), minor=False)
#ax.set_xticklabels(np.arange(0,31,10), minor=False, family='sans')
ax.set_xticklabels([])
ax.set_xticks(np.arange(0,31,5), minor=True)
#ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0f'))
plt.xlim(0,25)

ax.set_yticks(np.arange(-5,40,5), minor=False)
ax.set_yticklabels(np.arange(-5,40,5), minor=False, family='sans', fontsize=16)
ax.set_yticks(np.arange(-5,40,1), minor=True)
#plt.ylim(-25,1250)
#plt.ylim(-2,10.0)
plt.ylim(-1.5,20)
#ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1e'))
#ax.yaxis.set_major_formatter(sformatter)

plt.xlabel(None)
plt.ylabel('$\\mu/T$',fontsize=22)

text(1.0,17,"$\\tau=$"+str(tau)+" fm/$c$",fontsize=22,ha='left')
text(25,-1.0,"(i)",fontsize=20,ha='right')

#######################################

filename='MuTvsR_tau'+str(tau)+"_baryonstar.pdf"

plt.savefig(filename)
os.system('open -a Preview '+filename)
#plt.show()
quit()
