import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from spicy import stats

# 다중변수 데이터 (변수가 2개 이상임)
# df = pd.read_csv('../dfdata/iris.csv') # 변수가 몇개인가? -> 5개임(컬럼이 5개)
# print(df)
# 다중변수 데이터에서 변수는 컬럼으로 표현, 개별 관측값이 행.
# 변수 간의 관계를 파악하는 것이 핵심.
# '각 변수에 대해 단일 변수 데이터 분석 -> 변수들 간의 관계 분석'순으로 진행하는 것이 일반적.
# 기본적인 탐색 기법은 산점도와 상관 분석

#%% <산점도(Scatter Plot)> "두 변수로 구성된 데이터의 분포를 시각적으로 확인하는 그래프"
# 관측값들의 분포를 통해 두 변수 간의 관계를 파악하는 데 유용한 도구
# mtcars = pd.read_csv('../dfdata/mtcars.csv')
# print(mtcars)
# 자동차의 중량(wt)과 연비(mpg) 사이의 관계를 산점도를 통해 분석
# mtcars.plot.scatter(x='wt',y='mpg',s=50,c='red',marker='.') # x축 변수, y축 변수, pointSize, pointColor, pointMaker
# plt.show()
# mtcars_vars=['mpg','disp','drat','wt']
# 다중 산점도의 작성
# pd.plotting.scatter_matrix(mtcars[mtcars_vars])
# 여러 변수 간의 짝지어진 산점도를 한 번에 그릴 수 있는 방법
# 주대각선을 기준으로 대칭이 됨.
# plt.show()

# df = pd.read_csv('../dfdata/iris.csv')
# 그룹이 있는 다중 산점도의 작성
# dict = {'setosa':'red', 'versicolor':'green', 'virginica':'blue'}
# dict는 중괄호인걸 기억할 것.
# colors = list(dict[key] for key in df.Species) # 각 점의 색을 지정
# df객체의 Species컬럼에 있는 데이터가 setosa인 경우 red로, versicolor인 경우 green으로, virginica인경우에는 blue로 변환하여 
# colors객체에는 최종적으로 색상에 대한 정보만 저장
# print(dict['setosa']) # -> red를 반환.
# print(colors)
# df.plot.scatter(x='Petal_Length', y='Petal_Width', s=30, c=colors, marker='o')
# Petal(꽃잎)의 길이가 길수록 Petal의 폭도 넓어진다, Setosa 품종은 다른 두 품종에 비해 꽃잎의 길이와 폭이 확연히 작다 ... 식으로 분석 가능.
# plt.show()

# 산점도에 그룹 범례 표시
# color_map = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
# fig, ax = plt.subplots()
# for label, data in df.groupby('Species'):
#     ax.scatter(x=data['Petal_Length'], y=data['Petal_Width'], s=30,
#         c=color_map[label], marker='o', label=label)
#     print(data)
# ax.set_xlabel('Petal_Length')
# ax.set_ylabel('Petal_width')
# ax.legend()
# plt.show()


#%% <상관분석> "선형적 관계 정도를 수치적으로 나타내는 방법"
# 상관계수(r, correlation coefficient)는 두 변수 간 선형성의 정도를 나타내는 척도로 사용
# » -1 ≤ r ≤ 1
# » r > 0 : 양의 상관 관계 (x 가 증가하면 y 도 증가)
# » r < 0 : 음의 상관 관계 (x 가 증가하면 y 는 감소)
# » r 이 1 이나 –1에 가까울수록 x, y 의 상관성이 높다.
# 상관계수 값이 0.5보다 크거나 -0.5보다 작으면 두 변수의 상관성이 높다고 판단

# beers = [5,2,9,8,3,7,3,5,3,5] # 음주량
# bal = [0.1,0.03,0.19,0.12,0.04,0.0095,0.07,0.06,0.02,0.05] # 혈중알콜 농도
# beers와 bal의 상관관계를 분석한다면?
# dict = {'Beers':beers, 'Bal' : bal}
# df = pd.DataFrame(dict)
# print(df)
# df.plot.scatter(x='Beers',y='Bal',title='Beers~Blood Alcohol Level')
# x와 y는 df의 변수(컬럼명)임.
# plt.show()

# 선형회귀를 위한 계산식.
# m, b = np.polyfit(beers, bal, 1) # 1차 다항식을 x=beers, y=bal로 만듦 polynomial(다항식)
# plt.plot(beers, m * np.array(beers) + b) # y = mx + b꼴
# plt.show()
# print(df['Beers'].corr(df['Bal'])) # 두 변수간 상관계수 계산
# print(df['Bal'].corr(df['Beers'])) # 순서는 상관없음

# 여러 변수들간 상관계수
# df2 = pd.read_csv('../dfdata/iris.csv')
# df2 = df2.loc[:, ~df2.columns.isin(['Species'])] # 품종 컬럼 제외
# print(df2.corr()) 

# (+) Knowledge
# df.corr(method='person') # 피어슨 상관 계수 (기본)
# df.corr(method='kendall') # 켄달-타우 상관 계수 - 두 변수 값들의 "순위"를 기준으로 상관성 계산
# df.corr(method='spearman') # 스피어먼 상관 계수


#%% <선 상관분석 그래프>
# 선그래프를 작성하는 메서드는 plot()

# late = pd.Series([5,8,7,9,4,6,12,13,8,6,6,4], index=list(range(1,13)))
# late.plot(title='Late student per month',xlabel='Month',ylabel='Frequency',linestyle='solid')
# linestyle이 선의 종류를 의미함 solid면 실선
# plt.show()
# late.plot(title='Late student per month', # 제목
#  xlabel= 'month', # x축 레이블
#  ylabel='frequency', # y축 레이블
#  linestyle='dashed', # 선의 종류 (점선)
#  marker='o') # 점의 종류 - 실제 데이터 값이 있는 지점에 점을 찍음
# plt.show()

# 복수의 선그래프 작성
late1 = [5,8,7,9,4,6,12,13,8,6,6,4]
late2 = [4,6,5,8,7,8,10,11,6,5,7,3]
late = pd.DataFrame({'class_1':late1, 'class_2':late2}, index=list(range(1,13)))
# 각 컬럼 데이터는 하나의 선(Line)으로 표현되며, 여러 컬럼이 있을 경우 여러 개의 선 그래프로 나타남.
late.plot(xlabel='Month',ylabel='Frequency',title='Late student per month',linestyle='solid',marker='o')
plt.legend(loc='upper left') # 범례 지정 (loc는 범례를 띄울 위치 지정)
plt.show()


