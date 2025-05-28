import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
df = pd.read_csv('../dfdata/ind_ttest.csv')
# 데이터 탐색
# df.head()
# df.groupby('group').count() # 그룹별 표본 크기
# df.groupby('group').mean() # 그룹별 평균
# df.groupby('group').boxplot(grid=False)
# plt.show()
group_1 = df.loc[df.group=='A','height']
group_2 = df.loc[df.group=='B','height']
print(group_1)
print(group_2)
# 정규성 검정
print(stats.shapiro(group_1))
print(stats.shapiro(group_2))
# 등분산성 검정
print(stats.levene(group_1, group_2))
# 독립표본 T-검정
result = stats.ttest_ind(group_1, group_2, equal_var=True)
print(result)
