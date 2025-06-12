# 필요한 라이브러리 불러오기
import seaborn as sns
from scipy import stats

# 1.데이터셋 불러오기
titanic = sns.load_dataset("titanic")

# 2.선실(pclass)과 생존여부(alive) 컬럼에 대해 피벗을 적용하여 교차표를 작성한후 내용을 확인
# 3.선실별 생존비율을 계산한다.
# 4.교차표의 기대빈도를 확인한다.
# 5.카이제곱검정을 실시한후 p-value값을 확인한다.
df1 = titanic.groupby(['pclass','alive']).agg(count=('pclass','count')).unstack('pclass')
print(stats.chi2_contingency(df1))

# 결과를 확인해보니, array에서 나타나는 값이 모두 5 이상으로 나타남. 따라서 카이제곱 검정을 거칠 수 있음.
# 또한 유의수준(p-value) 0.05 기준으로 매우 작기 때문에, 귀무가설 기각
# → 즉, 선실 등급(pclass)과 생존 여부(survived)는 독립이 아니다
# → 둘 사이에 통계적으로 유의미한 관계가 있다

#%% 아래 코드는 수업시간에 교수님께서 'alive'컬럼이 아닌, 'survived'컬럼을 이용한 예시를 보여주셧기에, 같이 첨부함.
df1 = titanic.groupby(['survived','pclass']).agg(count=('pclass','count')).unstack('pclass')
print(stats.chi2_contingency(df1))

