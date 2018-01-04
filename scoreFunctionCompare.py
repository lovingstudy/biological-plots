import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score

'''
glideScoreFile = '../testset150831_docking.csv'
BRD4ScoreFile = '../addData/testsetPred150829.txt'
#glideData = [l.split('\",\"')[1:3] for l in open(glideScoreFile)][1:]
glideData = [l.strip().split(',')[-2:] for l in open(glideScoreFile)][1:]
glideData = [(float(b),int(a)) for a,b in glideData]
BRD4Data = [l.strip().split('\t') for l in open(BRD4ScoreFile)][1:]
BRD4Data = [(-float(a),int(c)) for a,b,c in BRD4Data]
score_act = {'BRD4LGR':BRD4Data, 'Glide':glideData}
'''

glideScoreFile = '../version3/BRD4LGRv2_glideScore_testset.csv'
BRD4ScoreFile = '../version3/BRD4LGRv3-1_bScore_testset.csv'
#glideData = [l.split('\",\"')[1:3] for l in open(glideScoreFile)][1:]
glideData = [l.strip().split(',')[-2:] for l in open(glideScoreFile)][1:]
glideData = sorted([(float(a),int(b)) for a,b in glideData])
BRD4Data = [l.strip().split(',')[-2:] for l in open(BRD4ScoreFile)][1:]
BRD4Data = sorted([(float(a),int(b)) for a,b in BRD4Data],reverse=True)
score_act = {'BRD4LGR':BRD4Data, 'Glide':glideData}


def enrichCmpre(score_act):
    num = len(score_act.items()[0][1])
    actNum = len([m for m in score_act.items()[0][1] if m[1]==1])
    dvdline = actNum
    ticks = range(0, 2*len(score_act), 2)

    fig = plt.figure(figsize=(9,8))
    plt.xlim(-2,2*len(score_act))
    plt.xticks(ticks, score_act.keys(), fontsize=20)
    for k,tick in zip(score_act.keys(),ticks):
        for i,(score,t) in enumerate(sorted(score_act[k])):
            if t==1: col = 'royalblue'
            else: col = 'red'
            plt.plot([tick-0.5,tick+0.5],[num-i,num-i],color=col,lw=2.7)
        ky, kscore = [y[1] for y in score_act[k]], [-y[0] for y in score_act[k]]
        #k_auc = roc_auc_score(ky, kscore)
        #plt.text(tick-0.25, num+2, '%.3f'%k_auc, fontsize=18)
    plt.plot([-2,2*len(score_act)],[dvdline,dvdline], '-.k', lw=1)
    #plt.text(-1.9, dvdline+4, 'Active', fontsize=16, color='navy')
    #plt.text(-1.9, dvdline-10, 'Inactive', fontsize=16, color='orangered')
    plt.ylabel('Score Rank', fontsize=20)
    plt.yticks(fontsize=15)
    #plt.title('Strip of Glide v.s. BRD4LGR',fontsize=30)
    plt.show()
    fig.savefig('scoreCompare.png',dpi=300)
        


enrichCmpre(score_act)
