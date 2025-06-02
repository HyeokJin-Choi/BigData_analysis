# 필요한 라이브러리 불러오기
import seaborn as sns
import pandas as pd
from scipy.stats import chi2_contingency

# 1. 데이터셋 불러오기
titanic = sns.load_dataset("titanic")

# 2. pclass와 alive 컬럼을 이용한 교차표 생성
cross_tab = pd.crosstab(titanic['pclass'], titanic['alive'])
print("교차표:")
print(cross_tab)

# 3. 선실별 생존 비율 계산
survival_rate_by_pclass = cross_tab.div(cross_tab.sum(axis=1), axis=0)
print("\n선실별 생존 비율:")
print(survival_rate_by_pclass)

# 4. 카이제곱 검정 및 기대 빈도 계산
chi2, p, dof, expected = chi2_contingency(cross_tab)

# 기대 빈도를 데이터프레임으로 변환해 출력
expected_df = pd.DataFrame(expected, index=cross_tab.index, columns=cross_tab.columns)
print("\n기대 빈도:")
print(expected_df)

# 5. 검정 통계량 및 p-value 출력
print("\n카이제곱 검정 결과:")
print(f"카이제곱 통계량: {chi2:.4f}")
print(f"자유도: {dof}")
print(f"p-value: {p:.4f}")

# 6. 결론 도출
alpha = 0.05
if p < alpha:
    print("\n결론: p-value가 0.05보다 작으므로, 선실 등급과 생존 여부는 유의미한 관련이 있습니다.")
else:
    print("\n결론: p-value가 0.05보다 크므로, 선실 등급과 생존 여부는 관련이 없다고 볼 수 있습니다.")



# 필요한 라이브러리 불러오기
import seaborn as sns
import pandas as pd
from scipy.stats import chi2_contingency

# 1. 데이터셋 불러오기
titanic = sns.load_dataset("titanic")

df1 = titanic.groupby(['survived','pclass']).agg(count=('pclass','count')).unstack('pclass')
print(df1)

chi2_contingency(df1)
