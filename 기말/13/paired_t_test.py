import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/samsung/Desktop/BigData_analysis/dfdata/paired_ttest.csv')
# 데이터 탐색
print(df.head())
print(df[['before', 'after']].mean()) # 그룹별 평균
print((df['after']-df['before']).mean()) # before,after 차이의 평균

fig, axes = plt.subplots(nrows=1, ncols=2)
print(df['before'].plot.box(grid=False, ax=axes[0]))
plt.ylim([60,100])
print(df['after'].plot.box(grid=False, ax=axes[1]))
plt.show()

# 정규성 검정
# 해당 데이터는 독립성을 만족하지 않으므로, 각각의 그룹에 대한 정규성을 검정하는 것이 아닌,
# 두 그룹의 차이값을데 대해 검정을 진행해야한다.
print(stats.shapiro(df['after']-df['before']))

# 대응표본 T-검정
# 가설 설정 :
# 귀무가설(H0): 새로운 교수법 이전과 이후의 성적은 차이가 없다. (새로운 교수법 (이후–이전)의 평균은 0이다)
# 대립가설(H1): 새로운 교수법 이전과 이후의 성적은 차이가 있다. (새로운 교수법 (이후–이전)의 평균은 0이 아니다)
result = stats.ttest_rel(df['before'], df['after'])
print(result)
