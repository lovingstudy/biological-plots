import numpy as np
import matplotlib.pyplot as plt
from math import log10

def loadData(filename):
    raw = [l.strip().split('\t') for l in open(filename)]
    xlab = raw[0][1:]
    ylab = [i[0] for i in raw[1:]]
    dataList = [i[1:] for i in raw[1:]]
    dataTrans = []
    for l in dataList:
        dataTrans.append([])
        for i in l:
            if i=='N': dataTrans[-1].append(-log10(100.0*10**(-6)))
            else: dataTrans[-1].append(-log10(float(i)*10**(-9)))
    data = np.array(dataTrans)
    return xlab, ylab, data

xlab, ylab, data = loadData('Kinase_selectivity_spectrum.txt')


fig = plt.figure(figsize=(17,5.5))
ax = plt.subplot()

heatmap = ax.pcolor(data, cmap=plt.cm.Reds)
ax.set_xticks(np.arange(len(xlab))+0.5)
ax.set_yticks(np.arange(len(ylab))+0.5)
ax.set_ylim(0,11)
ax.set_xticklabels(xlab, rotation=90)
ax.set_yticklabels(ylab)
cbar = plt.colorbar(heatmap)
cbar.set_label('pIC50')

plt.show()
fig.savefig('kinaseSpectrum1.png', dpi=300)
