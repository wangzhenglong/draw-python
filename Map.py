import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from mpl_toolkits.basemap import Basemap

# 地图
# 定义画布
p1 = plt.figure(dpi=300, figsize=(24, 8))  # 画布尺寸
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 定义季节标题
season = ['春', '夏', '秋', '冬']
for n in range(4):
    # 添加子画布
    p1.add_subplot(1, 4, n + 1)
    # 给子画布添加标题
    plt.title(season[n])
    # 绘制地图
    m = Basemap(llcrnrlon=77, llcrnrlat=14, urcrnrlon=140, urcrnrlat=51, projection='lcc', lat_1=33, lat_2=45,
                lon_0=100)
    # 画海岸线
    # m.drawcoastlines()
    # 画国际线
    # m.drawcountries(linewidth=1.5)
    # 读取省行政划分数据-用于画省线
    m.readshapefile('C:\\Users\\admin\\Desktop\\全国空气\\区划\\省', 'states', drawbounds=True)
    # 获取当前绘图区的坐标系
    ax = plt.gca()
    # 在大陆各省形状上填充颜色
    for i, shp in enumerate(m.states_info):
        if shp['省'] == '重庆市':
            poly = Polygon(xy=m.states[i],
                           facecolor='red',  # 填充红色
                           )
            ax.add_patch(poly)  # 在坐标系中添加省域多边形

# 画布展示
plt.show()
