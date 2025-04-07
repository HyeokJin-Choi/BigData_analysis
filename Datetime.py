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

df2 = pd.read_csv(file_path, parse_dates=['date'], index_col='date')

# 날짜 컬럼에서 연도, 월 정보 추출
df2.reset_index(inplace=True)
df2['year'] = [d.year for d in df2.date]
df2['month'] = [d.strftime('%b') for d in df2.date]

# 연도별 고유 값 찾기
years = df2['year'].unique()

# 무작위 색상 설정
np.random.seed(100)
mycolors = np.random.choice(list(mpl.colors.XKCD_COLORS.keys()), len(years), replace=False)

# 월을 숫자로 변환 (1: Jan, 2: Feb, ..., 12: Dec)
month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
df2['month_num'] = df2['month'].map(month_dict)

# 시각화
plt.figure(figsize=(16, 12), dpi=80)
for i, y in enumerate(years):
    if i > 0:
        # 월 순서대로 x축, value를 y축으로 그래프 그리기
        subset = df2.loc[df2.year == y, :]
        plt.plot(subset['month_num'], subset['value'], color=mycolors[i], label=y)
        
        # 마지막 값에 텍스트 추가
        plt.text(subset['month_num'].iloc[-1] - 0.9, subset['value'].iloc[-1], str(y), fontsize=12, color=mycolors[i])

# x, y축 설정 및 레이블 추가
plt.gca().set(xlim=(-0.3, 12), ylim=(2, 30), ylabel='$Drug Sales$', xlabel='$Month$')
plt.yticks(fontsize=12, alpha=.7)
plt.xticks(np.arange(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], fontsize=12, alpha=.7)
plt.title('Time series data', fontsize=20)
plt.legend()
plt.show()
