import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 折线图
file = open('C:\\Users\\admin\\Desktop\\全国空气\\PM2.5-cy-season\\all.csv', 'r')
df = pd.read_csv(file)
citys = list(dict.fromkeys(df['市/区'].real))
c = np.unique(df['市/区'])
fig = plt.figure(dpi=300, figsize=(24, 8))
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
for i, city in enumerate(citys):
    data = df.loc[df['市/区'] == city]
    ax1 = fig.add_subplot(5, 6, i + 1)
    p1, = ax1.plot(data["年度"], data["春"], ls='-', lw=1, c='g')
    p2, = ax1.plot(data["年度"], data["夏"], ls='-', lw=1, c='r')
    p3, = ax1.plot(data["年度"], data["秋"], ls='-', lw=1, c='y')
    p4, = ax1.plot(data["年度"], data["冬"], ls='-', lw=1, c='b')
    ax1.set_title(city, loc='center')

# 添加说明
plt.legend(handles=[p1, p2, p3, p4], labels=['春', '夏', '秋', '冬'],
           loc='upper center', bbox_to_anchor=(1.5, 0.5), fancybox=False, shadow=False, ncol=3)
plt.subplots_adjust(wspace=0.1, hspace=0.5)
plt.savefig('season.png', bbox_inches='tight')
# plt.show()
plt.close()
