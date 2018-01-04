#-------------------------------------------------------------------------------
# Name: testsetPredPlot.py
# Author: Yolanda
# Instructions: For two-class prediction testset, plot histogram of right and
#     wrong prediction. Data input from textfile containing score, predict-class
#     and true-class.
#-------------------------------------------------------------------------------

raw = sorted([l.strip().split('\t') for l in \
              open('../version3/BRD4LGRv2_pred_testset.txt')][1:])
raw = [(float(prob),int(pred),int(true)) for prob,pred,true in raw]
#right = [(prob,pred,true) for (prob,pred,true) in raw if pred==true]
#wrong = [(prob,pred,true) for (prob,pred,true) in raw if pred!=true]
right = [(prob,pred,true) for (prob,pred,true) in raw \
         if (true==1 and prob>=0.4) or (true==0 and prob<=0.5)]
wrong = [(prob,pred,true) for (prob,pred,true) in raw \
         if (true==1 and prob<0.4) or (true==0 and prob>0.5)]

rightProb = [a for a,b,c in right]
wrongProb = [a for a,b,c in wrong]

import matplotlib.pyplot as plt
#ti = [i/10.0 for i in range(1,11)]
xplus, yplus = 0.06, 0.8
ti = [0,0.2,0.4,0.6,0.8,1]
plt.figure(figsize=(12,10))
a = plt.hist([rightProb,wrongProb], bins=ti, color=['cornflowerblue','tomato'],\
             stacked=True, cumulative=False, label=['Right','Wrong'], lw=0)
plt.legend(fontsize=15, loc='upperleft')

cr,total = a[0]
pos = a[1]
for x,y,t in zip(pos, total, cr):
    rate = float(t)/y*100
    if rate>90: plt.text(x+xplus, y+yplus, str(rate)[:4]+'%', color='red',\
                          fontsize=15)
    else: plt.text(x+xplus, y+yplus, str(rate)[:4]+'%', fontsize=13)

plt.xlabel('Probability', fontsize=15)
plt.ylim(0,70)
plt.show()


