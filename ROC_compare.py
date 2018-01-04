import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

graw = [l.strip().split(',') for l in open('BRD4LGRv2_glideScore_testset.csv')][1:]
gscore = [-float(i[1]) for i in graw]
gtrue = [int(i[2]) for i in graw]
gfp,gtp,thre = roc_curve(gtrue,gscore)
gauc = roc_auc_score(gtrue,gscore)
braw = [l.strip().split(',') for l in open('BRD4LGRv2_bScore_testset.csv')][1:]
bscore = [float(i[1]) for i in braw]
btrue = [int(i[2]) for i in braw]
bfp,btp,thre = roc_curve(btrue,bscore)
bauc = roc_auc_score(btrue,bscore)

fig = plt.figure(figsize=(9,8))
#plt.plot(gfp,gtp,'r',lw=3,label='Glide AUC='+str(gauc)[:5])
plt.plot(bfp,btp,'g',lw=3,label='BRD4LGR AUC='+str(bauc)[:5])
plt.legend(loc='upper left')
plt.xlabel('FP rate',fontsize=20)
plt.xticks(fontsize=15)
plt.ylabel('TP rate',fontsize=20)
plt.yticks(fontsize=15)
#plt.title('ROC of Glide v.s. BRD4LGR',fontsize=30)
plt.title('ROC',fontsize=30)
plt.show()
fig.savefig('ROC_BRD4LGR.png',dpi=300)

