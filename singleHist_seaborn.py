import os
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import seaborn as sns

trainfile = '../version3/dscrptorValueLEScaled_train.txt'
testfile = '../version3/dscrptorValueLEScaled_test.txt'
raw = [i.strip().split('\t') for i in open(trainfile)]
title = raw[0]
raw = raw[1:]

def get_dataTable(filenames):
    titles = open(filenames[0]).readline().strip().split('\t')
    dataTable = dict([(t,[]) for t in titles])
    for n in filenames:
        raw = [l.strip().split('\t') for l in open(n)][1:]
        for i,t in enumerate(titles):
            dataTable[t] += [r[i] for r in raw]
    return dataTable


def getValue(des):
    i = title.index(des)
    active = [float(m[i]) for m in raw if m[1]=='1']
    inact = [float(m[i]) for m in raw if m[1]=='0']
    return active, inact

des = '92_polar'
dataTable = get_dataTable([trainfile, testfile])
actives = [float(v) for i,v in enumerate(dataTable[des]) if \
           dataTable['Active'][i] == '1']
inactives = [float(v) for i,v in enumerate(dataTable[des]) if \
           dataTable['Active'][i] == '0']

#-------- para ----------------------------------------------------------
if des == '92_polar':
    bs = [i/2.5 for i in range(-6,6)]
    bs = [-2.4]
    for i in range(16): bs.append(bs[-1]+0.3)
    bsm = [i/10.0 for i in range(-25,25)]
    mu1, mu2, sig1, sig2, n1, n2 = 0.2, -0.2, 0.6, 0.8, 170, 220
    yl = 0.85

elif des == '97_polar':
    #bs = [i/2.5 for i in range(-8,8)]
    bs = [-3.0]
    for i in range(15): bs.append(bs[-1]+0.4)
    #bsm = [i/10.0 for i in range(-30,30)]
    #mu1, mu2, sig1, sig2, n1, n2 = -0.3, 0.3, 1, 0.6, 330, 200
    yl = 0.7
#-------------------------------------------------------------------------

sns.set(style="white", palette="muted", color_codes=True)
Fig = plt.figure(figsize=(8,7))
ax1 = Fig.add_subplot(111)
sns.distplot(inactives, kde=True, bins=bs, hist=True, color='red', \
             label='Negative', ax=ax1)
sns.distplot(actives, kde=True, bins=bs, hist=True, color='slateblue', \
             label='Positive', ax=ax1)

ax1.legend(fontsize=15)
ax1.set_xticks(bs)
ax1.set_xlim(bs[0],bs[-1])
ax1.set_ylim(0,yl)
ax1.set_title(des+' Scores', fontsize=20)
ax1.set_ylabel('Density', fontsize=15)

plt.show()
Fig.savefig(des+'_score_distribution160831.png', dpi=600)

