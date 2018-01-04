#-----------------------------------------------------------------------------
# Name: paraPlot.py
# Author: Yolanda
# Instruction: Plot model parameters in polar axis. Descriptors and parameters
#     are input from a model text file.
#-----------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Old #
'''
DESCRIPTOR = ['I146\nnp','W81\npolar','P82\nnp','F83\nnp','F83\npolar','Q85\nnp',\
              'L92\nnp','L92\npolar','L94\nnp','Electro','Water\nhb']
para = [0.07785, -0.96835, -0.62792, -0.07237, -0.55418, 0.14573, 0.20543, \
        0.87112, -0.18862, -0.59481, -0.52225]
'''
# Old #

trainfile = '../version3/dscrptorValueLEScaled_train.txt'
#modelfile = '../../official_version_beta2/model151029_scaled.txt'
modelfile = '../../official_version_beta3/model_160621.txt'
#modelfile = '../../official_version_4/model160125.txt'

def getParaDES(trainfile, modelfile, transform=False):
    rawPara = [float(l.strip().split()[1]) for l in open(modelfile)][:-1]
    rawDES = [l.strip().split()[0] for l in open(modelfile)][:-1]
    if not transform: return rawPara, rawDES
    f = open(trainfile)
    title = f.readline().strip().split('\t')
    trainDict = dict([(i,[0.0,0.0]) for i in title])
    for line in f:
        value = line.strip().split('\t')
        for t,v in zip(title,value):
            if t=='Name': continue
            trainDict[t] = [min([float(v),trainDict[t][0]]),\
                            max([float(v), trainDict[t][1]])]
    f.close()
    para = [rpara/(trainDict[t][1]-trainDict[t][0]) for rpara,t in \
            zip(rawPara, rawDES)]
    
    return para, rawDES

# New
para, DESCRIPTOR = getParaDES(trainfile, modelfile)

# Modify names of descriptors.
DESCRIPTOR = [des.replace('_','\n') for des in DESCRIPTOR]
DESCRIPTOR[DESCRIPTOR.index('w\nhb')] = 'Water\n H-bond'
#DESCRIPTOR[DESCRIPTOR.index('electro')] = 'Electro'   


theta = np.linspace(0.0, 2*np.pi, len(DESCRIPTOR), endpoint=False)
radii = np.array([abs(i) for i in para])
width = [2*np.pi/(len(DESCRIPTOR)+1)]*len(DESCRIPTOR)

fig = plt.figure(figsize=(9,8))
ax = plt.subplot(111, polar=True)
plt.xticks(theta+0.5*np.array(width),DESCRIPTOR, fontsize=15)
bars = ax.bar(theta, radii, width=width, bottom=0.0)
for i,bar in enumerate(bars):
    #if c[i] == 0: bar.set_facecolor('purple')
    #else: bar.set_facecolor('orange')
    if para[i]>0:
        bar.set_facecolor(cm.Reds(para[i]+0.25))
    else:
        bar.set_facecolor(cm.Blues(-para[i]))
    bar.set_alpha(0.9)
'''
an = ax.annotate('Water H-bond', xy=(theta[-1]+0.5*width[-1],radii[-1]),\
                 bbox=dict(boxstyle='round',fc='0.8'),\
                 arrowprops=dict(arrowstyle='->'))
an.draggable()
'''
plt.show()
fig.savefig('para160621.png',dpi=300)
