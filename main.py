import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontProperties

# ----------------------
# 中文字体设置（关键：避免中文乱码）
# ----------------------
# 加载本地字体（确保 fonts 文件夹与 main.py 同级，且包含 SimHei.ttf）
font_path = "./fonts/simhei.ttf"
my_font = FontProperties(fname=font_path)
plt.rcParams["font.family"] = [my_font.get_name()]  # 全局字体设置
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示异常

# ----------------------
# 数据加载
# ----------------------
# 加载数据（确保 Excel 文件与代码同级或路径正确）
df_area = pd.read_excel('不同地区访问用户量统计.xlsx')  # 假设地区数据文件名为这个
df_channel = pd.read_excel('不同来源渠道访问用户量统计.xlsx')

# ----------------------
# 页面标题与布局
# ----------------------
st.title('用户访问量统计可视化大屏')
st.divider()  # 分隔线

# ----------------------
# 第一个图表：不同地区访问用户量柱状图
# ----------------------
st.subheader('1. 不同地区访问用户量分布')
st.caption('通过柱状图展示各地区的独立会话用户总量')  # 辅助说明

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x='地区信息', y='独立会话标识总数', data=df_area, ax=ax1)
ax1.set_title('不同地区访问用户量柱状图', fontsize=12)
ax1.set_xlabel('地区', fontsize=10)
ax1.set_ylabel('访问用户量', fontsize=10)
ax1.tick_params(axis='x', rotation=90)  # 地区名称过长时旋转
st.pyplot(fig1)
st.divider()

# ----------------------
# 第二个图表：不同来源渠道访问用户量饼图
# ----------------------
st.subheader('2. 不同来源渠道用户占比')
st.caption('通过饼图展示各渠道访问用户量的占比情况')

fig2, ax2 = plt.subplots(figsize=(8, 8))
df_channel['独立会话标识总数'].plot(
    kind='pie',
    ax=ax2,
    labels=df_channel['来源渠道'],
    autopct='%1.1f%%',  # 显示百分比
    startangle=90,
    textprops={'fontproperties': my_font}  # 确保饼图标签中文正常显示
)
ax2.set_title('不同来源渠道访问用户量饼图', fontsize=12)
ax2.axis('equal')  # 保证饼图为正圆形
st.pyplot(fig2)
st.divider()

# ----------------------
# 第三个图表：不同地区访问用户量分布箱线图
# ----------------------
st.subheader('3. 不同地区访问用户量分布特征')
st.caption('通过箱线图展示各地区用户量的分布范围、中位数等统计特征')

fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.boxplot(x='地区信息', y='独立会话标识总数', data=df_area, ax=ax3)
ax3.set_title('不同地区访问用户量分布箱线图', fontsize=12)
ax3.set_xlabel('地区', fontsize=10)
ax3.set_ylabel('访问用户量', fontsize=10)
ax3.tick_params(axis='x', rotation=90)
st.pyplot(fig3)



