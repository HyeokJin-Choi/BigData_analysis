import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/samsung/Desktop/BigData_analysis/dfdata/ind_ttest.csv')
# 데이터 탐색
# print(df.head())
# print(df.groupby('group').count()) # 그룹별 표본 크기
# print(df.groupby('group').mean()) # 그룹별 평균
# print(df.groupby('group').boxplot(grid=False))
# plt.show()

# 두 그룹은 다른 비료 A, B를 각각 투여함
group_1 = df.loc[df.group=='A','height']
group_2 = df.loc[df.group=='B','height']
print(group_1)
print(group_2)
# ---> 독립성 만족 O

# 정규성 검정 -> scipy.stats.shapiro() 함수를 통해 나온 **정규성 검정 결과 (Shapiro-Wilk test)**
# 해당 코드의 결과의 p-value가 0.05이상이면 정규성을 만족한다는 결과를 도출.
# Shapiro-Wilk test의 가설은 다음과 같습니다:
# 귀무가설 (H₀): 데이터는 정규분포를 따른다
# 대립가설 (H₁): 데이터는 정규분포를 따르지 않는다
print(stats.shapiro(group_1))
print(stats.shapiro(group_2))
# ---> 정규성 만족 O

# 등분산성 검정 -> 두 집단 이상에서 **분산이 서로 같은지(등분산성)**를 검정하는 등분산성 검정
# 해당 코드의 결과의 p-value가 0.05이상이면 등분산성을 만족한다는 결과를 도출.
# 가설 설정:
# 귀무가설(H₀): 두 집단(또는 여러 집단)의 분산은 같다 (등분산성 만족)
# 대립가설(H₁): 적어도 한 집단의 분산은 다르다 (등분산성 불만족)
print(stats.levene(group_1, group_2))
# ---> 등분산성 만족 O

# 독립표본 T-검정 실행 가능
# 가설 설정 :
# 귀무가설(H₀): 두 그룹의 평균은 차이가 없다.
# 대립가설(H₁): 두 그룹의 평균은 차이가 있다.
result = stats.ttest_ind(group_1, group_2, equal_var=True)
print(result)
