import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from spicy import stats

# 평균값과 중앙값의 차이점은 평균값은 이상치에 영향을 많이 받고, 중앙값은 이상치에 크게 영향을 받지 않음
# 절사평균이란 데이터의 하위 n%와 상위 n%를 제외하여 남은 값들을 이용하여 평균을 계산함.
# scipy module 의 stats.trim_mean 가 절사평균

# df = pd.Series([60,62,64,65,68,69,120])
# print("df.mean() = ",df.mean()) # 120이라는 값 하나 때문에 평균이 확 떠버림
# print("df.median() = ", df.median()) # 이는 중간에 있는 값 자체를 표현하기 때문에 이상치와는 크게 영향x
# print("stats.trim_mean(df,0.2) = ", stats.trim_mean(df,0.2))
# stats.trim_mean(df, n) 하위 n%와 상위 n%를 제외하여 평균값 계산
# 따라서 위의 코드는 하위 20%와 상위 20%를 제외한 나머지 60%의 데이터를 기준으로 평균을 계산

# 사분위수(quantile)란 주어진 데이터를 크기순으로 나열한 후, 이를 4등분하는 지점에 있는 값.
# 3개의 등분점이 제1사분위수(Q1), 제2사분위수(Q2)(중앙값과 동일), 제 3분위수(Q3)라 불림.
# print("---df.quantile([0.25,0.50,0.75])---\n", df.quantile([0.25,0.50,0.75]))

# print("df.var() = ", df.var(), "| df.std() = ", df.std())
# 분산과 표준편차가 클수록 데이터간의 크기 차이가 큼.
# 분산과 표준편차가 작을수록 데이터간의 크기 차이가 작음.


#%% 히스토그램
# titanic = pd.read_csv("../dfdata/titanic.csv")
# titanic = titanic.dropna(subset='age', axis=0) # 나이의 분포를 보기 위함. 따라서 나이가 없는 데이터는 버림. axis = 0이니 해당 사람의 정보(행)를 없애는 것.
# plt.rcParams['font.family'] = 'Malgun Gothic' # 한글 폰트 변경 (맑은 고딕) *순서 중요.
# plt.rcParams['axes.unicode_minus'] = False # 마이너스부호 깨짐 방지
# titanic['age'].plot.hist(xlabel="나이", ylabel="분포", title="타이타닉-나이 분포", figsize=(6,4)) # figsize는 그래프의 크기를 인치 단위로 지정.
# 연속형 데이터에서는 특정 구간을 나누고, 해당 구간에 속하는 값들의 개수를 세는 방식으로 히스토그램을 작성함.
# 단일 변수 범주형 데이터의 분석에서 사용한 막대그래프와 유사
# plt.show()


#%% 여러 그래프를 한번에 띄우기
# df = pd.read_csv("../dfdata/iris.csv")
# fig, axes = plt.subplots(nrows=2, ncols=2) # 2x2 즉, 4개의 그래프 띄울 수 있음. 
# 각 분할 영역에 그래프 작성하기. axes는 4개의 서브 그래프를 의미
# df['Petal_Length'].plot.hist(ax=axes[0,0]) # (0,0)위치에는 df['Petal_Length']에 대한 히스토그램
# df['Petal_Length'].plot.box(ax=axes[0,1]) # (0,1)위치에는 df['Petal_Length']에 대한 상자 그림
# 상자 그림(Box Plot)이란 "사분위수를 시각적으로 표현한 그래프 형태"
# fd = df['Species'].value_counts() # fd객체를 df['Species']에 대한 개수로 설정
# fd.plot.pie(ax=axes[1,0]) # (1,0)위치에는 fd객체에 대한 원형 그래프
# fd.plot.barh(ax=axes[1,1]) # (1,1)위치에는 fd객체에 대한 수평 막대 그래프
# 통합 그래프에 제목 지정
# fig.suptitle('Multiple Graph Example', fontsize=14) # fig는 통합된 전체 그래프를 의미
# 분할 그래프 화면에 나타내기
# plt.show()

# print(titanic['age'].value_counts(bins=6,sort=False)) # age 값이 0세 ~ 80세 사이니, bins=6이면 약 13.3살 단위로 구간 나누어짐.



#%% Quiz
# 1. titanic객체를 이용하여 타이타닉에 탑승했던 남성과 여성의 나이 분포를 하나의 히스토그램으로 출력하라. (단 alpha = 0.5)

# 2. titanic객체를 age를 6개의 구간으로 나누고, 히토그램의 막대를 초록색으로 설정하여 출력하라.

# 3. 학생 12명의 취미를 조사하였더니 다음과 같았다. 이 데이터를 사용하여 아래에서 제시하는 작업을 수행해보자.
# "등산","낚시","골프","수영","등산","등산","낚시","수영","등산","낚시","수영","골프"
# 3)-1. 데이터를 hobby(판다스 시리즈)에 저장하고 내용을 확인하시오.
# 3)-2. 취미별 도수분포표를 작성하시오.
# 3)-3. 도수분포표를 막대그래프와 원그래프로 시각화하되, 한 화면에 작성하시오.

# 4. BostonHousing 데이터셋은 보스턴 지역의 주택 가격 및 관련 정보를 담고 있다. 여기서 집값(medv) 데이터만 추출하여 분석해 보자.
# 4)-1. BostonHousing 데이터셋에서 집값(medv) 데이터 컬럼만 추출하여 house_price에 저장하고 내용을 확인하시오.
# 4)-2. 집값의 평균, 중앙값, 사분위수를 확인하시오.
# 4)-3. 사분위수를 기준으로 4개 구간의 집값 평균을 구하고 이를 막대그래프로 시각화하시오.
# 4)-4. 집값의 분포를 상자그림으로 시각화하시오.
# 4)-5. 집값의 분포를 히스토그램으로 시각화하되, 구간 수를 8로 설정하시오.


# <정답>
# 1.
# titanic.query('sex=="male"')['age'].plot.hist(ylabel="man", alpha = 0.5)
# titanic.query('sex=="female"')['age'].plot.hist(ylabel="woman", alpha = 0.5)
# plt.show()

# 2. 
# titanic['age'].plot.hist(ylabel="Frequency", bins = 6, color = "green")
# plt.show()

# 3.
# 3)-1.
# plt.rcParams['font.family'] = 'Malgun Gothic' # 순서상 한글을 사용하기 전에 써야함.
# hobby = pd.Series(["등산","낚시","골프","수영","등산","등산","낚시","수영","등산","낚시","수영","골프"])
# print(hobby)
# 3)-2.
# hobbyGraph = hobby.value_counts()
# print(hobbyGraph)
# 3)-3.
# fig, axes = plt.subplots(nrows=1, ncols=2)
# hobbyGraph.plot.bar(ax = axes[0])
# hobbyGraph.plot.pie(ax = axes[1])
# fig.suptitle('Students Hobby',fontsize=14)
# plt.show()

# 4.
# 4)-1.
# BostonHousing = pd.read_csv('../dfdata/BostonHousing.csv')
# house_prise = BostonHousing['medv']
# print(house_prise)
# 4)-2.
# print(house_prise.mean(),'\n', house_prise.median(),'\n' ,house_prise.quantile([0.25,0.50,0.75]))
# 4)-3.
# q1 = house_prise[house_prise<house_prise.quantile(0.25)].mean()
# q2 = house_prise[house_prise<house_prise.quantile(0.50)].mean()
# q3 = house_prise[house_prise<house_prise.quantile(0.75)].mean()
# q4 = house_prise[house_prise>=house_prise.quantile(0.75)].mean()
# plt.rcParams['font.family'] = 'Malgun Gothic'
# avg_series = pd.Series(
#     [q1, q2, q3, q4],
#     index=["Q1 미만", "Q1~Q2", "Q2~Q3", "Q3 이상"]
# )
# avg_series.plot.bar(xlabel='사분위 구간', ylabel='평균 집값', title='사분위수 기준 구간별 평균 집값', rot=0)
# plt.show()
# 4)-4.
# house_prise.plot.box(ylabel='Price')
# plt.show()
# 4)-5.
# house_prise.plot.hist(bins=8)
# plt.show()



# %%
