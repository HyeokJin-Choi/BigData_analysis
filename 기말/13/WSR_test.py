# 윌콕슨 부호 순위 검정 : 독립성, 정규 분포를 만족하지 않을 때 시행하는 검정 방법
# A 제품에 불만이 많은 소비자 8명을 선정하여 성능이 개선된 제품을 한 달간 사용하게 한 후 불만도가 감소하였는지를 검정
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/samsung/Desktop/BigData_analysis/dfdata/wilcoxon_test.csv')
print(df.head())
print(df[['pre', 'post']].mean()) # 그룹별 평균
print((df['pre']-df['post']).mean()) # post,pre 차이의 평균

fig, axes = plt.subplots(nrows=1, ncols=2)
print(df['pre'].plot.box(grid=False, ax=axes[0]))
plt.ylim([60,100])
print(df['post'].plot.box(grid=False, ax=axes[1]))
plt.show()

# 윌콕슨 부호 순위 검정 실시
# 가설 설정 :
# 귀무가설(H0): 제품 개선 전과 개선 후의 불만도 점수는 차이가 없다
# 대립가설(H1): 제품 개선 전과 개선 후의 불만도 점수는 차이가 있다
print(stats.wilcoxon(df['pre'],df['post']))
# p-value가 0.25로써 유의수준보다 크다. 따라서 귀무가설 채택
# 즉 고객 불만도가 낮아졌다고 볼 수 있는 근거가 없다.

