import pandas as pd
import numpy as np
from dateutil.parser import parse
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

# 데이터 불러오기 및 전처리
file_path = "dfdata/time_series2.csv"
# df = pd.read_csv(file_path) 
# df['new_Date'] = pd.to_datetime(df['date'])
# df.drop('date', axis=1, inplace=True)
# df.set_index('new_Date', inplace=True)

# # 시각화 설정
# plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

# # 그래프 그리기 함수 정의
# def plot_df(df, x, y, title="", xlabel='Date', ylabel='Value', dpi=100):
#     plt.figure(figsize=(16, 5), dpi=dpi)
#     plt.plot(x, y, color='tab:red')
#     plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
#     plt.show()

# # 함수 실행
# plot_df(df, x=df.index, y=df.value, title='Time series data')

df2=pd.read_csv(file_path,parse_dates=['date'],index_col='date')
df2.reset_index(inplace=True)
df2['year']=[d.year for d in df2.date]
df2['month']=[d.strftime('%b') for d in df2.date]

years=df2['year'].unique()
np.random.seed(100)
mycolors=np.random.choice(list(mpl.colors.XKCD_COLORS.key()),len(years),replace=False)
