import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 柱状图
# 汉字
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 打开文件
file = open("C:\\Users\\admin\\Desktop\\全国空气\\PM2.5-cy\\all.csv", 'r', encoding="gbk")
# 读文件
data = pd.read_csv(file)

# 生成市/区值字典
citys = list(dict.fromkeys(data['市/区'].real))
# 柱宽度
bar_with = 0.5

# 生成多行多列图
fig, ax = plt.subplots(7, 6, sharey=True, dpi=300, figsize=(20, 30))
for i, city in enumerate(citys[:]):
    columns = data.loc[data['市/区'] == city]
    province = columns['省/市'].real
    labels = columns['年度'].real
    t1s = columns['PM2.5<=35的时间占比'].real
    t2s = columns['PM2.5>35的时间占比'].real
    t3s = columns['PM2.5>150的时间占比'].real
    x = np.arange(len(province))
    x1 = int(i / 6)
    y1 = int(i % 6)
    # 画柱图
    p1 = ax[x1][y1].bar(x, t1s, bar_with, color='g')
    p2 = ax[x1][y1].bar(x, t2s, bar_with, bottom=t1s, color='b')
    p3 = ax[x1][y1].bar(x, t3s, bar_with, bottom=1 - t3s, color='r')
    # 设置x轴刻度
    ax[x1][y1].set_xticks(x)
    # 设置x轴标签
    ax[x1][y1].set_xticklabels(labels)
    # 设置标题
    ax[x1][y1].set_title(city)
    if (y1 != 0):
        # 设置y轴刻度不显示
        ax[x1][y1].tick_params(labelleft=False, left=False)
    if i == len(citys) - 1:
        # 添加说明
        plt.legend(handles=[p1, p2, p3], labels=['PM2.5<=35的时间占比', 'PM2.5>35的时间占比', 'PM2.5>150的时间占比'],
                   loc='upper center', bbox_to_anchor=(-2, -0.4), fancybox=False, shadow=False, ncol=3)
# 设置子图间距
plt.subplots_adjust(wspace=0.1, hspace=0.5)
plt.savefig('draw_bar.png', bbox_inches='tight')
# plt.show()
plt.close()
