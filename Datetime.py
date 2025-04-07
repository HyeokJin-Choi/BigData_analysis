import pandas as pd
import numpy as np
from dateutil.parser import parse
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기 및 전처리
file_path = "C:/Users/thdgh/Downloads/time_series2.csv"
df = pd.read_csv(file_path) 
df['new_Date'] = pd.to_datetime(df['date'])
df.drop('date', axis=1, inplace=True)
df.set_index('new_Date', inplace=True)

# 시각화 설정
plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

# 그래프 그리기 함수 정의
def plot_df(df, x, y, title="", xlabel='Date', ylabel='Value', dpi=100):
    plt.figure(figsize=(16, 5), dpi=dpi)
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()

# 함수 실행
plot_df(df, x=df.index, y=df.value, title='Time series data')
