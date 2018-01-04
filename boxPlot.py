testfile = '../addData/addData150829_value_test.txt'
trainfile = '../addData/addData150829_value_train.txt'

def get_dataTable(filename):
    titles = open(filename).readline().strip().split('\t')
    dataTable = dict([(t,None) for t in titles])
    raw = [l.strip().split('\t') for l in open(filename)][1:]
    for i,t in enumerate(titles): dataTable[t] = [r[i] for r in raw]
    return dataTable


import matplotlib.pyplot as plt
DES = sorted(['81_polar','82_np','83_polar','85_np','85_polar','92_polar','97_np',\
       '140_np','140_polar','w_hb']*2)
'''
des = '97_np'
actives = [float(v) for i,v in enumerate(dataTable[des]) if \
           dataTable['Active'][i]=='1']
inactives = [float(v) for i,v in enumerate(dataTable[des]) if \
             dataTable['Active'][i]=='0']

plt.figure(figsize=(10,10))
plt.boxplot([actives, inactives], widths=0.6)
plt.xticks([1,2],['Active','Inactive'], fontsize=20)
plt.title(des + ' Energys', fontsize=30)
plt.yticks(fontsize=15)
plt.ylim(-8,1)
plt.show()
'''
fig, axes = plt.subplots(nrows=5, ncols=4, figsize=(20,25))
for i,des in enumerate(DES):
    x, y = i/4, i%4
    if y%2==0: t, dataTable = '(Trainset)', get_dataTable(trainfile)
    else: t, dataTable = '(Testset)', get_dataTable(testfile)
    actives = [float(v) for i,v in enumerate(dataTable[des]) if \
               dataTable['Active'][i]=='1']
    inactives = [float(v) for i,v in enumerate(dataTable[des]) if \
                 dataTable['Active'][i]=='0']
    axes[x,y].boxplot([actives, inactives])
    axes[x,y].set_xticklabels(['Active','Inactive'],fontsize=15)
    axes[x,y].set_title(des+' Energys '+t, fontsize=15)
plt.show()


    
