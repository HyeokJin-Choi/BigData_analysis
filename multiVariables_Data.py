import pandas as pd  # pandas 라이브러리 임포트 (데이터 처리용)
import numpy as np  # numpy 라이브러리 임포트 (수학 계산용)
import matplotlib.pyplot as plt  # matplotlib 라이브러리 임포트 (그래프 그리기용)

# 음주량 (Beers)과 혈중 알콜 농도 (Blood Alcohol Level, BAL) 데이터 정의
beers = [5, 2, 9, 8, 3, 7, 3, 5, 3, 5]  # 음주량 (비어의 개수)
bal = [0.1, 0.03, 0.19, 0.12, 0.04, 0.0095, 0.07, 0.06, 0.02, 0.05]  # 혈중 알콜 농도

# 딕셔너리로 데이터 묶기
dict = {'beers': beers, 'bal': bal}  # 음주량과 혈중 알콜 농도를 묶어서 딕셔너리로 정의

# pandas DataFrame 생성: 딕셔너리를 기반으로 데이터를 표 형태로 저장
df = pd.DataFrame(dict)  # dict를 사용하여 DataFrame 생성

# 생성된 DataFrame 출력
df  # DataFrame을 출력하여 데이터를 확인

# 산점도 그래프 그리기: 음주량(beers)과 혈중 알콜 농도(bal) 간의 관계를 시각화
df.plot.scatter(x='beers', y='bal', title='Beers~Blood Alcohol Level')  # 산점도 그리기 (x축: beers, y축: bal)

# 회귀식 계산: 음주량(beers)과 혈중 알콜 농도(bal) 사이의 직선 관계를 찾음
m, b = np.polyfit(beers, bal, 1)  # np.polyfit 함수로 선형 회귀 계산 (1은 직선의 차수, 즉 1차 함수)

# 회귀선 그리기: 계산된 회귀식으로 예측된 값을 바탕으로 회귀선을 그래프에 추가
plt.plot(beers, m * np.array(beers) + b)  # 회귀선 (m은 기울기, b는 y절편)
plt.show()  # 그래프 출력

# 두 변수 간 상관계수 계산: 음주량과 혈중 알콜 농도 간의 상관관계를 수치적으로 계산
df['beers'].corr(df['bal'])  # 'beers'와 'bal' 간의 피어슨 상관계수 계산

# 여러 변수들 간의 상관계수 계산: iris 데이터셋에서 여러 변수 간 상관계수를 확인
df2 = pd.read_csv('dfdata/iris.csv')  # 'iris.csv' 파일을 읽어서 DataFrame으로 저장
df2.columns  # DataFrame의 열 이름 출력 (컬럼명 확인)

# 'Species' 열 제외: 품종 컬럼을 제외하고 나머지 숫자형 데이터만 사용
df2 = df2.loc[:, ~df2.columns.isin(['Species'])]  # 'Species' 컬럼 제외

df2.columns  # 다시 컬럼명 확인

# 상관계수 계산: iris 데이터셋의 각 변수 간 상관계수를 계산
df2.corr()  # 각 컬럼 간의 상관계수 계산
