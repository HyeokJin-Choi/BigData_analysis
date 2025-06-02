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



# 필요한 라이브러리 불러오기
import seaborn as sns
import pandas as pd
from scipy.stats import chi2_contingency

# 1. 타이타닉 데이터 불러오기
titanic = sns.load_dataset("titanic")

# 2. survived와 pclass에 따른 빈도수 집계
df1 = titanic.groupby(['survived', 'pclass']).agg(count=('pclass', 'count')).unstack('pclass')
df1.columns = df1.columns.droplevel(0)  # 다중 인덱스 제거
print("▶ 생존여부와 선실 등급 간 교차표 (빈도수):")
print(df1)

# 3. 카이제곱 검정 수행
chi2, p, dof, expected = chi2_contingency(df1)

# 4. 기대 빈도 출력
expected_df = pd.DataFrame(expected, index=df1.index, columns=df1.columns)
print("\n▶ 기대 빈도:")
print(expected_df)

# 5. 검정 결과 출력
print("\n▶ 카이제곱 검정 결과:")
print(f"카이제곱 통계량: {chi2:.4f}")
print(f"자유도: {dof}")
print(f"p-value: {p:.4f}")

# 6. 결론 도출 (유의수준 0.05 기준)
alpha = 0.05
if p < alpha:
    print("\n✅ 결론: p-value < 0.05 → 선실 등급과 생존 여부 사이에 통계적으로 유의미한 관계가 있습니다.")
else:
    print("\n❌ 결론: p-value ≥ 0.05 → 선실 등급과 생존 여부 사이에 통계적으로 유의미한 관계가 없습니다.")
