import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype

# 데이터 탐색 실습
# BostonHousing 데이터셋은 미국 보스턴 지역의 주택 가격 정보와 주택 가격에 영향을 미치는 다양한 요소를 갖는 파일

#%% Quiz
# 0단계 - 그래프에 한글 나타내기 준비
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 1단계 - 데이터 준비 
# BostonHousing.csv에서 'crim','rm','dis','tax','medv' 컬럼만 가져오시오.

df = pd.read_csv('../dfdata/BostonHousing.csv')
df = df[['crim','rm','dis','tax','medv']] # df는 DataFrame형태임. 따라서[[컬럼명1, 컬럼명2 ...]]형태로 가져와야함.

# 2단계 - 그룹 컬럼 추가
# medv를 기준으로 medv가 25.0이상이면 'H', 17.0이하면 'L', 중간이면 'M'으로 그룹을 구분하여
# df객체에 grp라는 컬럼으로 추가하시오.
# 이후 grp 컬럼의 자료형을 범주형(categorical type)으로 변경하고
# grp 컬럼의 레이블 순서를 기본 알파벳 순서('H', 'L', 'M')에서 논리적 순서('H', 'M', 'L')로 변경하시오.
grp = pd.Series('M'for i in range(len(df)))
grp.loc[df.medv >= 25.0] = 'H'
grp.loc[df.medv <= 17.0] = 'L'
# loc[] 안에서는 **Boolean mask (True/False로 이루어진 시리즈)**나 정확한 인덱스를 넘겨야지, 그래야 Pandas가 올바르게 이해하고 동작
# grp.loc[[df['medv'] <= 17.0]]식으로 동작할 수 없음.
df['grp'] = grp
new_odr = ['H','M','L']
new_dtype = CategoricalDtype(categories=new_odr, ordered=True)
df.grp = df.grp.astype(new_dtype)
print(df.grp.dtype)




# %%
