import pandas as pd
import matplotlib.pyplot as plt

# 折线图
file1 = open('C:\\Users\\admin\\Desktop\\全国空气\\年均值-重庆.csv', 'r')
file2 = open('C:\\Users\\admin\\Desktop\\全国空气\\年均值-四川.csv', 'r')
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
# 获取code集合
code1 = list(dict.fromkeys(df1['code'].real))
code2 = list(dict.fromkeys(df2['code'].real))
# 设置画布比例
fig = plt.figure(dpi=300, figsize=(16, 8))
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 获取颜色集
cm = plt.get_cmap('gist_rainbow')

# 重庆
ax1 = fig.add_subplot(1, 2, 1)
ax1.set_title('重庆', loc='center')
list1 = []
list2 = []
for i, code in enumerate(code1):
    data = df1.loc[df1['code'] == code]
    for columns in enumerate(data):
        # 循环划线，上色
        p, = ax1.plot(data["year"], data["PM2.5"], ls='dashed', lw=1, c=cm(i // 3 * 3.0 / len(code1)))
    # 组装折线对象
    list1.append(p)
    # 组装折现说明
    list2.append(code)
# 添加说明
plt.legend(handles=list1, labels=list2,
           loc='upper center', bbox_to_anchor=(-0.3, 1), fancybox=False, shadow=False, ncol=3)
# 四川
ax2 = fig.add_subplot(1, 2, 2)
plt.yticks([])
ax2.set_title('四川', loc='center')
list3 = []
list4 = []
for i, code in enumerate(code2):
    data = df2.loc[df2['code'] == code]
    for columns in enumerate(data):
        p2, = ax2.plot(data["year"], data["PM2.5"], ls='dashed', lw=1, c=cm(i // 3 * 3.0 / len(code2)))
    list3.append(p2)
    list4.append(code)

plt.legend(handles=list3, labels=list4,
           loc='upper center', bbox_to_anchor=(1.3, 1), fancybox=False, shadow=False, ncol=3)
# 设置子图间距
plt.subplots_adjust(wspace=0.1, hspace=0)
plt.savefig('avg-cy.png', bbox_inches='tight')
# plt.show()
plt.close()
