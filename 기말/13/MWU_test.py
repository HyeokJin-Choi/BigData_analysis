# 맨 휘트니 U 검정 : 독립성은 만족하지만 정규 분포를 만족하지 않을 때 시행하는 검정 방법
# 학생들을 A, B 두 그룹으로 나누고 A그룹에는 일반 필기구를 B그룹에는 새로 개발된 필기구를 주어 일주일을 사용하게 한 뒤 만족도를 조사하였다.
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/samsung/Desktop/BigData_analysis/dfdata/mw_test.csv')
print(df.head())
# 두 그룹의 표본의 크기가 30 미만이므로 정규성을 만족하지 못하는 것을 확인할 수 있음.
print(df.groupby('group').count()) # 그룹별 표본 크기
print(df.groupby('group').mean()) # 그룹별 평균
print(df.groupby('group').boxplot(grid=False))
plt.show()

group_1 = df.loc[df.group=='A','score']
group_2 = df.loc[df.group=='B','score']
print(group_1)
print(group_2)

# 맨 휘트니 검정 실시
# 가설 설정 :
# 귀무가설(H0): 두 그룹의 만족도는 차이가 없다
# 대립가설(H1): 두 그룹의 만족도는 차이가 있다
print(stats.mannwhitneyu(group_1,group_2))
# p-value가 0.085로써 유의수준보다 크다. 따라서 귀무가설 채택

