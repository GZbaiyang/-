import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontProperties

font_path = "./fonts/simhei.ttf"
my_font = FontProperties(fname=font_path)

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300

# 正常显示中文
plt.rcParams['font.sans-serif'] = [my_font.get_name()]

# 正常显示负号
plt.rcParams['axes.unicode_minus'] = False

# 加载不同地区访问用户量统计文件
df_area = pd.read_excel('不同地区访问用户量统计.xlsx')

# 加载不同来源渠道访问用户量统计文件
df_channel = pd.read_excel('不同来源渠道访问用户量统计.xlsx')

# 设置页面标题
st.title('用户访问量统计可视化大屏')


# 第一个图表：不同地区访问用户量柱状图
fig1, ax1 = plt.subplots()
sns.barplot(x='地区信息', y='独立会话标识总数', data=df_area, ax=ax1)
ax1.set_title('不同地区访问用户量柱状图')
ax1.set_xlabel('地区')
ax1.set_ylabel('访问用户量')
ax1.tick_params(axis='x', rotation=90)
st.pyplot(fig1)

# 第二个图表：不同来源渠道访问用户量饼图
fig2, ax2 = plt.subplots()
df_channel['独立会话标识总数'].plot(kind='pie',
                              ax=ax2,
                              labels=df_channel['来源渠道'],
                              autopct='%1.1f%%',
                              startangle=90)
ax2.set_title('不同来源渠道访问用户量饼图')
ax2.axis('equal')
st.pyplot(fig2)

# 第三个图表：不同地区访问用户量分布箱线图
fig3, ax3 = plt.subplots()
sns.boxplot(x='地区信息', y='独立会话标识总数', data=df_area, ax=ax3)
ax3.set_title('不同地区访问用户量分布箱线图')
ax3.set_xlabel('地区')
ax3.set_ylabel('访问用户量')
ax3.tick_params(axis='x', rotation=90)
st.pyplot(fig3)



