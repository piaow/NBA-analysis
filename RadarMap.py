import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

nba = pd.read_csv(r'ScoreFouth.csv',encoding='utf-8')

#转换数据到同一数据级别
nba_total = nba.sum(axis=0)
for  i in range(1,9):
    nba.iloc[:,i] = nba.iloc[:,i]/nba_total[i]

for  i in range(1,9):
    print(nba.iloc[:,i])

#提取数据
nba.set_index(nba['球员'],inplace=True)  #把球员列设置成
nba = nba.iloc[:,1:]  #从第一列开始提取

#设置中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#构造雷达图的数据
values = nba.iloc[0,:]
values1 = nba.iloc[1,:]
values2 = nba.iloc[2,:]
values3 = nba.iloc[3,:]
labels = nba.columns

N=len(values)
#设置雷达
angles = np.linspace(0,2*np.pi,N,endpoint= False)
#闭合数据
values = np.concatenate(( values ,[values[0]] ))
values1 = np.concatenate(( values1 ,[values1[0]] ))
values2 = np.concatenate(( values2 ,[values2[0]] ))
values3 = np.concatenate(( values3 ,[values3[0]] ))
angles = np.concatenate(( angles,[angles[0]] ))
labels = np.concatenate((labels,[labels[0]] ))

#绘制雷达
fig = plt.figure()
ax = fig.add_subplot(111,polar = True)   #开启极坐标模式
ax.plot(angles,values,'ro-',label='杜兰特')
ax.fill(angles ,values , 'r', alpha=0.5)

ax.plot(angles,values1,'bo-',label='库里')
ax.fill(angles ,values1 , 'b', alpha=0.5)

ax.plot(angles,values2,'yo-',label='乔治')
ax.fill(angles ,values2 , 'y', alpha=0.5)

ax.plot(angles,values3,'go-',label='佛罗赞')
ax.fill(angles ,values3 , 'g', alpha=0.5)

#设置标签
ax.set_thetagrids(angles*180/np.pi,labels)
ax.set_ylim(0,0.35)
plt.title('球员数据')
plt.legend(bbox_to_anchor=(1.3,1.1))
plt.show()



