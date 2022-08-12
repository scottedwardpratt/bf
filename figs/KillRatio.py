import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import os
from pylab import *
from matplotlib import ticker
#from matplotlib.ticker import ScalarFormatter
#sformatter=ScalarFormatter(useOffset=True,useMathText=True)
#sformatter.set_scientific(True)
#sformatter.set_powerlimits((-2,3))

species=["$N$","$\\Sigma$","$\\Xi$","$\\Lambda$","$\\Delta$","$\\Sigma^*$","$\\Xi^*$","$\\Omega$"]
antispecies=["$\\bar{N}$","$\\bar{\\Sigma}$","$\\bar{\\Xi}$","$\\bar{\\Lambda}$","$\\bar{\\Delta}$","$\\bar{\\Sigma}^*$","$\\bar{\\Xi}^*$","$\\bar{\\Omega}$"]

names=['N','Sigma','Xi','Lambda','Delta','Sigmastar','Xistar','Omega']

Nstrange=[0,1,2,1,0,1,2,3]

plt.figure(figsize=(15,6))
fig=plt.figure(1)

btype1=0
#btype1=int(input('Enter btype1: '))
btype2=0
#btype2=int(input('Enter btype2: '))

NS=Nstrange[btype1]+Nstrange[btype2]
if NS==6:
	NS=1
NPI=5-NS

bottom=0.17
height=(0.98-bottom)
width=0.3
x0=0.085

################## Panel 1 #####################
ax = fig.add_axes([x0,bottom,width,height])
tau=12
filename='data/muTvsR_pi_tau'+str(tau)+'.txt'
print('filename=',filename)
pidata = np.loadtxt(filename,skiprows=0,unpack=True)
filename='data/muTvsR_K_tau'+str(tau)+'.txt'
print('filename=',filename)
Kdata = np.loadtxt(filename,skiprows=0,unpack=True)
filename='data/muTvsR_B'+str(btype1)+'_tau'+str(tau)+'.txt'
print('filename=',filename)
B1data = np.loadtxt(filename,skiprows=0,unpack=True)
filename='data/muTvsR_B'+str(btype2)+'_tau'+str(tau)+'.txt'
print('filename=',filename)
B2data = np.loadtxt(filename,skiprows=0,unpack=True)

rpi=pidata[0]
Npi=pidata[1]
Tpi=pidata[2]
Upi=pidata[3]
mupi=pidata[4]
rhopi=float(tau)*pidata[5]

rK=Kdata[0]
NK=Kdata[1]
TK=Kdata[2]
UK=Kdata[3]
muK=Kdata[4]
rhoK=float(tau)*Kdata[5]

rB1=B1data[0]
NB1=B1data[1]
TB1=B1data[2]
UB1=B1data[3]
muB1=B1data[4]
rhoB1=float(tau)*B1data[5]

rB2=B2data[0]
NB2=B2data[1]
TB2=B2data[2]
UB2=B2data[3]
muB2=B2data[4]
rhoB2=float(tau)*B2data[5]

x=np.array([],dtype=float)
y=np.array([],dtype=float)
s=np.prod(Npi.shape)
z=np.array([],dtype=float)
for i in range(0,s):
	if Npi[i]>4 and NK[i]>4 and NB1[i]>4 and NB2[i]>4 :
		DelMu0=-muB1[i]-muB2[i]+NPI*mupi[i]+NS*muK[i]
		X=exp(DelMu0)
		DelBeta=-(1.0/Tpi[i])+(0.5/TB1[i])+(0.5/TB2[i])
		#Ebar=2.0+1.5*TB1[i]+1.5*TB2[i]  # typical energy of a baryon of mass 1.0 GeV
		Ebar=2.0
		XX=exp(DelBeta*Ebar)
		print(i,': X=',X,' DelMu0=',DelMu0,' XX=',XX,' DelBeta=',DelBeta)
		x=np.append(x,rpi[i])
		y=np.append(y,X)
		z=np.append(z,XX)

yz=1.0-y*z
y=1.0-y
z=1.0-z


plt.plot(x,y,linestyle='--',color='g',markersize=6,marker='o',markerfacecolor='g',label='$1-e^{-2\\mu_N+5\\mu_\\pi}$')
#plt.plot(x,z,linestyle='-',color='r',markersize=6,marker='o',markerfacecolor='r')
plt.plot(x,yz,linestyle='-',color='k',markersize=6,marker='s',markerfacecolor='k',label='add correction for $\\Delta T$')
#plt.plot(rpi,X1,linestyle='-',color='g',markersize=6,marker='o',markerfacecolor='g')
#plt.plot(rpi,X2,linestyle='-',color='b',markersize=6,marker='o',markerfacecolor='b')
#plt.plot(rpi,X3,linestyle='-',color='c',markersize=6,marker='o',markerfacecolor='c')

ax.tick_params(axis='both', which='major', labelsize=14)

ax.set_xticks(np.arange(0,31,10), minor=False)
ax.set_xticklabels(np.arange(0,31,10), minor=False, family='sans',fontsize=18)
ax.set_xticks(np.arange(0,31,5), minor=True)
#ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0f'))
plt.xlim(0,25)

ax.set_yticks(np.arange(-2,2,0.5), minor=False)
ax.set_yticklabels(np.arange(-2,2,0.5), minor=False, family='sans',fontsize=18)
ax.set_yticks(np.arange(-2,2.0,0.1), minor=True)
plt.ylim(-0.1,1.1)
#ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1e'))
#ax.yaxis.set_major_formatter(sformatter)

plt.xlabel(None)
plt.ylabel('$R_{\\rm ann.}/R_0$',fontsize=26)

text(24,0.0,'a) $\\tau=$'+str(tau)+' fm/$c$',fontsize=26,ha='right')
#species=species[btype1]+','+species[btype2]
if NS==0:
	species_descrip=species[btype1]+'+'+antispecies[btype2]+'$\\leftrightarrow$'+str(NPI)+'$\\pi$'
else:
	species_descrip=species[btype1]+'+'+antispecies[btype2]+'$\\leftrightarrow$'+str(NPI)+'$\\pi$'+'+'+str(NS)+'$K$'
text(24,0.125,species_descrip,fontsize=26,ha='right')

########## Panel 2 ##################
ax = fig.add_axes([x0+width,bottom,width,height])
tau=15
filename='data/muTvsR_pi_tau'+str(tau)+'.txt'
print('filename=',filename)
pidata = np.loadtxt(filename,skiprows=0,unpack=True)
filename='data/muTvsR_K_tau'+str(tau)+'.txt'
print('filename=',filename)
Kdata = np.loadtxt(filename,skiprows=0,unpack=True)
filename='data/muTvsR_B'+str(btype1)+'_tau'+str(tau)+'.txt'
print('filename=',filename)
B1data = np.loadtxt(filename,skiprows=0,unpack=True)
filename='data/muTvsR_B'+str(btype2)+'_tau'+str(tau)+'.txt'
print('filename=',filename)
B2data = np.loadtxt(filename,skiprows=0,unpack=True)

rpi=pidata[0]
Npi=pidata[1]
Tpi=pidata[2]
Upi=pidata[3]
mupi=pidata[4]
rhopi=float(tau)*pidata[5]

rK=Kdata[0]
NK=Kdata[1]
TK=Kdata[2]
UK=Kdata[3]
muK=Kdata[4]
rhoK=float(tau)*Kdata[5]

rB1=B1data[0]
NB1=B1data[1]
TB1=B1data[2]
UB1=B1data[3]
muB1=B1data[4]
rhoB1=float(tau)*B1data[5]

rB2=B2data[0]
NB2=B2data[1]
TB2=B2data[2]
UB2=B2data[3]
muB2=B2data[4]
rhoB2=float(tau)*B2data[5]

x=np.array([],dtype=float)
y=np.array([],dtype=float)
s=np.prod(Npi.shape)
z=np.array([],dtype=float)
for i in range(0,s):
	if Npi[i]>4 and NK[i]>4 and NB1[i]>4 and NB2[i]>4 :
		DelMu0=-muB1[i]-muB2[i]+NPI*mupi[i]+NS*muK[i]
		X=exp(DelMu0)
		DelBeta=-(1.0/Tpi[i])+(0.5/TB1[i])+(0.5/TB2[i])
		#Ebar=2.0+1.5*TB1[i]+1.5*TB2[i]  # typical energy of a baryon of mass 1.0 GeV
		Ebar=2.0
		XX=exp(DelBeta*Ebar)
		print(i,': X=',X,' DelMu0=',DelMu0,' XX=',XX,' DelBeta=',DelBeta)
		x=np.append(x,rpi[i])
		y=np.append(y,X)
		z=np.append(z,XX)

yz=1.0-y*z
y=1.0-y
z=1.0-z

plt.plot(x,y,linestyle='--',color='g',markersize=6,marker='o',markerfacecolor='g',label='$S_\\mu(\\vec{\\mu},\\vec{T})$')
#plt.plot(x,z,linestyle='-',color='r',markersize=6,marker='o',markerfacecolor='r')
plt.plot(x,yz,linestyle='-',color='k',markersize=6,marker='s',markerfacecolor='k',label='$S_\\mu(\\vec{\\mu},\\vec{T})S_T(\\vec{\\mu},\\vec{T})$')
#plt.plot(rpi,X1,linestyle='-',color='g',markersize=6,marker='o',markerfacecolor='g')
#plt.plot(rpi,X2,linestyle='-',color='b',markersize=6,marker='o',markerfacecolor='b')
#plt.plot(rpi,X3,linestyle='-',color='c',markersize=6,marker='o',markerfacecolor='c')
#legend(loc=(0.01,0.25),fontsize=18)

ax.tick_params(axis='both', which='major', labelsize=14)

ax.set_xticks(np.arange(0,31,10), minor=False)
ax.set_xticklabels(np.arange(0,31,10), minor=False, family='sans',fontsize=18)
ax.set_xticks(np.arange(0,31,5), minor=True)
#ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0f'))
plt.xlim(0,25)

ax.set_yticks(np.arange(-2,2,0.5), minor=False)
ax.set_yticklabels([])
ax.set_yticks(np.arange(-2,2.0,0.1), minor=True)
plt.ylim(-0.1,1.1)
#ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1e'))
#ax.yaxis.set_major_formatter(sformatter)

plt.xlabel('$r$ [fm]', fontsize=26, weight='normal')
plt.ylabel(None)


text(24,0.0,'b) $\\tau=$'+str(tau)+' fm/$c$',fontsize=26,ha='right')

############# Panel 3 ###############
tau=18
ax = fig.add_axes([x0+2*width,bottom,width,height])

filename='data/muTvsR_pi_tau'+str(tau)+'.txt'
print('filename=',filename)
pidata = np.loadtxt(filename,skiprows=0,unpack=True)
filename='data/muTvsR_K_tau'+str(tau)+'.txt'
print('filename=',filename)
Kdata = np.loadtxt(filename,skiprows=0,unpack=True)
filename='data/muTvsR_B'+str(btype1)+'_tau'+str(tau)+'.txt'
print('filename=',filename)
B1data = np.loadtxt(filename,skiprows=0,unpack=True)
filename='data/muTvsR_B'+str(btype2)+'_tau'+str(tau)+'.txt'
print('filename=',filename)
B2data = np.loadtxt(filename,skiprows=0,unpack=True)

rpi=pidata[0]
Npi=pidata[1]
Tpi=pidata[2]
Upi=pidata[3]
mupi=pidata[4]
rhopi=float(tau)*pidata[5]

rK=Kdata[0]
NK=Kdata[1]
TK=Kdata[2]
UK=Kdata[3]
muK=Kdata[4]
rhoK=float(tau)*Kdata[5]

rB1=B1data[0]
NB1=B1data[1]
TB1=B1data[2]
UB1=B1data[3]
muB1=B1data[4]
rhoB1=float(tau)*B1data[5]

rB2=B2data[0]
NB2=B2data[1]
TB2=B2data[2]
UB2=B2data[3]
muB2=B2data[4]
rhoB2=float(tau)*B2data[5]

x=np.array([],dtype=float)
y=np.array([],dtype=float)
s=np.prod(Npi.shape)
z=np.array([],dtype=float)
for i in range(0,s):
	if Npi[i]>4 and NK[i]>4 and NB1[i]>4 and NB2[i]>4 :
		DelMu0=-muB1[i]-muB2[i]+NPI*mupi[i]+NS*muK[i]
		X=exp(DelMu0)
		DelBeta=-(1.0/Tpi[i])+(0.5/TB1[i])+(0.5/TB2[i])
		#Ebar=2.0+1.5*TB1[i]+1.5*TB2[i]  # typical energy of a baryon of mass 1.0 GeV
		Ebar=2.0
		XX=exp(DelBeta*Ebar)
		print(i,': X=',X,' DelMu0=',DelMu0,' XX=',XX,' DelBeta=',DelBeta)
		x=np.append(x,rpi[i])
		y=np.append(y,X)
		z=np.append(z,XX)

yz=1.0-y*z
y=1.0-y
z=1.0-z


plt.plot(x,y,linestyle='--',color='g',markersize=6,marker='o',markerfacecolor='g',label='$S_\\mu(\\vec{\\mu},\\vec{T})$')
#plt.plot(x,z,linestyle='-',color='r',markersize=6,marker='o',markerfacecolor='r')
plt.plot(x,yz,linestyle='-',color='k',markersize=6,marker='s',markerfacecolor='k',label='$S_\\mu(\\vec{\\mu},\\vec{T})S_T(\\vec{\\mu},\\vec{T})$')
#plt.plot(rpi,X1,linestyle='-',color='g',markersize=6,marker='o',markerfacecolor='g')
#plt.plot(rpi,X2,linestyle='-',color='b',markersize=6,marker='o',markerfacecolor='b')
#plt.plot(rpi,X3,linestyle='-',color='c',markersize=6,marker='o',markerfacecolor='c')

legend(loc=(0.04,0.55),fontsize=21)

ax.tick_params(axis='both', which='major', labelsize=14)

ax.set_xticks(np.arange(0,31,10), minor=False)
ax.set_xticklabels(np.arange(0,31,10), minor=False, family='sans',fontsize=18)
ax.set_xticks(np.arange(0,31,5), minor=True)
#ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0f'))
plt.xlim(0,25)

ax.set_yticks(np.arange(-2,2,0.5), minor=False)
ax.set_yticklabels([])
ax.set_yticks(np.arange(-2,2.0,0.1), minor=True)
plt.ylim(-0.1,1.1)
#ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1e'))
#ax.yaxis.set_major_formatter(sformatter)

plt.xlabel(None)
plt.ylabel(None)
text(24,0.0,'c) $\\tau=$'+str(tau)+' fm/$c$',fontsize=26,ha='right')

###############

filename='KillRatio_'+names[btype1]+'_'+names[btype2]+'.pdf'

plt.savefig(filename)
os.system('open -a Preview '+filename)
#plt.show()
quit()
