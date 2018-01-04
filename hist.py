import os
import matplotlib.pyplot as plt

trainfile = '../version3/dscrptorValueLEScaled_train.txt'
testfile = '../version3/dscrptorValueLEScaled_test.txt'
raw = [i.strip().split('\t') for i in open(trainfile)]
title = raw[0]
raw = raw[1:]

def get_dataTable(filename):
    titles = open(filename).readline().strip().split('\t')
    dataTable = dict([(t,None) for t in titles])
    raw = [l.strip().split('\t') for l in open(filename)][1:]
    for i,t in enumerate(titles): dataTable[t] = [r[i] for r in raw]
    return dataTable


def getValue(des):
    i = title.index(des)
    active = [float(m[i]) for m in raw if m[1]=='1']
    inact = [float(m[i]) for m in raw if m[1]=='0']
    return active, inact

'''
des = '140_np'
Fig = plt.figure(figsize=(10,10))
#plt.hist([active140,inact140], bins=5, color=['green','red'])
#plt.hist([activeW,inactW], color=['green','red'], label=['active','inactive'])
a = plt.hist(getValue(des), color=['green','red'], \
         label=['Active','Inactive'])
plt.legend(['Active','Inactive'], 'upper left', fontsize=18)
#xlist = [(a[1][i]+a[1][i+1])/2 for i in range(len(a[1])-1)]
#plt.plot(xlist,a[0][0], 'k-.')
#plt.plot(xlist,a[0][1], 'y-')
plt.title(des+' Energy (Trainset)', fontsize=25)
plt.xticks(fontsize=15)
plt.xlim(-3.0,-0.3)
plt.ylim(0,40)
plt.yticks(fontsize=15)
plt.show()
'''
'''
DES = sorted(['140_np', '140_polar', '81_np', '81_polar', '83_np', '85_np', \
              '87_np', '87_polar', '92_np', '92_polar', '94_polar', '97_np', \
              '97_polar', 'electro', 'w_hb']*2)
'''
DES = sorted(['140_polar', '146_np', '81_np', '81_polar', '82_np', '82_polar', \
              '83_np', '83_polar', '85_np', '85_polar', '87_np', '87_polar', \
              '92_np', '92_polar', '94_polar', '97_np', '97_polar', 'w_hb']*2)
bs = [i/2.0 for i in range(-6,7)]
fig, axes = plt.subplots(nrows=6, ncols=6, figsize=(21,12))
fig.subplots_adjust(top=0.97, bottom=0.03, left=0.03, right=0.97, hspace=0.3)
for i,des in enumerate(DES):
    x, y = i/6, i%6
    if i==len(DES): break
    if y%2==0: t, dataTable = '(Trainset)', get_dataTable(trainfile)
    else: t, dataTable = '(Testset)', get_dataTable(testfile)
    actives = [float(v) for i,v in enumerate(dataTable[des]) if \
               dataTable['Active'][i]=='1']
    inactives = [float(v) for i,v in enumerate(dataTable[des]) if \
                 dataTable['Active'][i]=='0']
    axes[x,y].hist([actives, inactives], label=['Positive','Negative'],\
                   bins=bs, color=['cornflowerblue','tomato'])
    axes[x,y].legend(loc='upper left',fontsize=8)
    axes[x,y].set_title(des+' Scores '+t, fontsize=13)
    axes[x,y].set_xlim(-3,3)
    
plt.show()
fig.savefig('Energy_distribution.png',dpi=300)
