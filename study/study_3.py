import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 단일 변수 범주형 데이터 탐색
# 범주형 데이터란? -> 질적 데이터라 부르며, 성별, 등급 등과 같이이 산술 연산이 불가능한 데이터.
# 연속형 데이터란? -> 양적 데이터라 부르며, 키, 몸무게 등과 같이 산술 연산이 가능한 데이터.
# 단일 변수? -> 특성이 하나임.
# 따라서 가능한 작업은 각 범주의 개수를 세는 것
# 종류별로 비율을 알 수 있고, 이 결과를 이용하여 막대 그래프나 원 그래프를 작성할 수 있음.
# 단일변수 범주형 데이터의 예시는 학생 10명이 선호하는 계절을 모아둔 데이터를 생각해보자.
# 계절은 4가지가 끝임. 해당 데이터에서 학생은 4가지의 범주 내에서 결정해야함.
# 따라서 각 범주의 개수를 센다면 -> 학생들이 어느 계절을 선호하는 지 데이터 분석이 가능.
# 변수는 "계절", 학생은 "관측 대상(관측치)"

#%% 막대 그래프

# df = pd.Series(['Spring', 'Summer', 'Fall', 'Winter', 'Fall', 'Fall', 'Spring', 'Summer', 'Fall', 'Spring'])
# print(df.value_counts()) # 도수 분포를 출력함. 개수가 많은 순부터 내림차순으로 출력.
# print(df.value_counts()/df.size) # 비율을 출력.
# df = pd.Categorical(df,categories=['Spring','Summer','Fall','Winter'],ordered=True) # 출력되는 범주의 순서를 내 입맛대로 설정. 계절 순으로 정함.
# df_barGraph = df.value_counts() # 도수 분포의 값을 그릴 예정.
# df_barGraph.plot.bar(xlabel='Season', ylabel='Frequency', rot=0, title='Favorite Season') # x축을 범주로 설정, y축은 관측치(학생) rot는 x축 범주명의 회전 각도
# df_barGraph.plot.barh(xlabel='Season', ylabel='Frequency', rot=0, title='Favorite Season') # 위의 막대그래프를 수평선과 평행하게 눕힌 그래프 (h=horizental)
# plt.show() # 그래프를 띄움


#%% 원형 그래프

# df = pd.Series(['Spring', 'Summer', 'Fall', 'Winter', 'Fall', 'Fall', 'Spring', 'Summer', 'Fall', 'Spring'])
# df = pd.Categorical(df,categories=['Spring','Summer','Fall','Winter'],ordered=True)
# df_barGraph = df.value_counts()
# df_barGraph.plot.pie(ylabel='', autopct='%1.0f%%', title='Favorite Season') # pie가 원형 그래프를 띄우는 함수. ylabel은 항상 공백으로 할 것.
# # autopct는 원형 그래프 내에 뜨는 %의 값. 1.0은 소수점 이하를 나타내지 않겠다는 뜻. 1.1은 소수점 이하 한자리까지 나타내겠다는 ....
# plt.show()


# %% Quiz
# 1. mpg.csv 파일에서 category컬럼의 개수에 따른 분포에서 최대 5위까지를 막대 그래프와 원 그래프로 나타내시오.


# <정답>
# 1. 
# mpg = pd.read_excel('../dfdata/mpg.xlsx')
# mpg_Graph = mpg['category'].value_counts().head(5)
# mpg_Graph.plot.bar(xlabel='Category',ylabel='Count',rot=0,title='MPG Category')
# plt.show()
# mpg_Graph.plot.pie(ylabel='',autopct='%1.0f%%',title='MPG Category')
# plt.show()


