# DK
beginner
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'    #设置字体名称
radar_labels = np.array(['研究型(I)','艺术型(A)','社会型(S)',\
                         '企业型(E)','常规型(C)','现实型(R)']) #数组雷达标签
nAttr = 6
data = np.array([[0.40, 0.32, 0.35, 0.30, 0.30, 0.88],
                 [0.85, 0.35, 0.30, 0.40, 0.40, 0.30],
                 [0.43, 0.89, 0.30, 0.28, 0.22, 0.30],
                 [0.30, 0.25, 0.48, 0.85, 0.45, 0.40],
                 [0.20, 0.38, 0.87, 0.45, 0.32, 0.28],
                 [0.34, 0.31, 0.38, 0.40, 0.92, 0.28]]) #使用array函数创建一个多维数组，数据值
data_labels = ('艺术家', '实验员', '工程师', '推销员', '社会工作者','记事员')
angles = np.linspace(0, 2*np.pi, nAttr, endpoint=False)  #生成一组数据0-360°划分为6个区域
print(angles)
data = np.concatenate((data, [data[0]]))  #数据拼接
angles = np.concatenate((angles, [angles[0]]))  #数据拼接
fig = plt.figure(facecolor="white")  #设置背景颜色
plt.subplot(111, polar=True)  #分成1*1的图，使用第一个。使用极坐标
plt.plot(angles,data,'o-', linewidth=1)  #画点。1、2：点的坐标。3、点样式。4、线宽。
plt.fill(angles,data, alpha=0.25)  #填充颜色  alpha表示透明度
#设置极轴，参数为网格线角度、标记文本
plt.thetagrids(angles*180/np.pi, radar_labels)
#1、2:设置标题的坐标（左下角为原点）3、标题名4、位置5、字体大小
plt.figtext(0.52, 0.95, '霍兰德人格分析', ha='center', size=20)
#显示图中的标签 loc:位置 labelspacing:图例条目的垂直间距。返回一个图例类型
legend = plt.legend(data_labels, loc=(0.94, 0.80), labelspacing=0.1)
plt.setp(legend.get_texts(), fontsize='large')
plt.grid(False)  #显示网格
plt.savefig('holland_radar.jpg')  #保存图片
plt.show()  #显示图片


