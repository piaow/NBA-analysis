import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

nba = pd.read_csv(r'Kurant.csv',encoding='gbk')

#转换数据到同一数据级别
nba_total = nba.sum(axis=0)
# for  i in range(1,9):
nba.iloc[:,1] = nba.iloc[:,1]/(nba_total[1]-100)
nba.iloc[:,2] = nba.iloc[:,2]/(nba_total[2]-2)

nba.iloc[:,3] = nba.iloc[:,3]/(nba_total[3]-0.5)
nba.iloc[:,4] = nba.iloc[:,4]/(nba_total[4]-3)
nba.iloc[:,5] = nba.iloc[:,5]/(nba_total[5]-4)
nba.iloc[:,6] = nba.iloc[:,6]/(nba_total[6]-25)
nba.iloc[:,7] = nba.iloc[:,7]/(nba_total[7]+13)
nba.iloc[:,8] = nba.iloc[:,8]/(nba_total[8]+3)




#提取数据
nba.set_index(nba['赛季'],inplace=True)  #把球员列设置成
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
ax.plot(angles,values,'ro-',label='2007')
ax.fill(angles ,values , 'r', alpha=0.5)

ax.plot(angles,values1,'bo-',label='2008')
ax.fill(angles ,values1 , 'b', alpha=0.5)

ax.plot(angles,values2,'yo-',label='2009')
ax.fill(angles ,values2 , 'y', alpha=0.5)

ax.plot(angles,values3,'go-',label='2010')
ax.fill(angles ,values3 , 'g', alpha=0.5)

ax.plot(angles,values3,'co-',label='2011')
ax.fill(angles ,values3 , 'c', alpha=0.5)

ax.plot(angles,values3,'mo-',label='2010')
ax.fill(angles ,values3 , 'm', alpha=0.5)

ax.plot(angles,values3,'ko-',label='2010')
ax.fill(angles ,values3 , 'k', alpha=0.5)

ax.plot(angles,values3,'ro-',label='2014')
ax.fill(angles ,values3 , 'r', alpha=0.5)

ax.plot(angles,values3,'bo-',label='2015')
ax.fill(angles ,values3 , 'b', alpha=0.5)

ax.plot(angles,values3,'yo-',label='2016')
ax.fill(angles ,values3 , 'y', alpha=0.5)

ax.plot(angles,values3,'go-',label='2017')
ax.fill(angles ,values3 , 'go-', alpha=0.5)

ax.plot(angles,values3,'co-',label='2018')
ax.fill(angles ,values3 , 'c', alpha=0.5)

ax.plot(angles,values3,'mo-',label='2019')
ax.fill(angles ,values3 , 'm', alpha=0.5)

ax.plot(angles,values3,'ko-',label='2020')
ax.fill(angles ,values3 , 'k', alpha=0.5)

ax.plot(angles,values3,'go-',label='2021')
ax.fill(angles ,values3 , 'g', alpha=0.5)
#设置标签
ax.set_thetagrids(angles*180/np.pi,labels)
ax.set_ylim(0,0.1)
plt.title('球员数据')
plt.legend(bbox_to_anchor=(1.1,1))
plt.show()



