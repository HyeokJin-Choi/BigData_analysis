import pandas as pd
import numpy as np


# *** 새로운 열을 추가할때에는 ''따옴표를 붙이지 않음. 열을 불러 사용할때에는 ''따옴표를 사용.
df = pd.read_csv('dfdata/exam.csv')
df.agg(mean_math=('math','mean')) #math의 평균값 (=) df_test = pd.DataFrame({'math' : df['math'].mean()}, index = ['mean_math'])
df.groupby('nclass', as_index = False).agg(mean_math=('math','mean')) # nclass컬럼을 기준으로 그룹화해서 보여주되, math는 평균값으로 계산함.
# as_index = False 설정을 추가하면 인덱스가 nclass 값이 아닌, 절대 인덱스로 설정됨. 그리고 그 옆에 nclass를 순으로 출력함.
# (+) 여기서 컬럼명을 할때 대괄호를 하지 않는 이유는? -> 집계 함수의 결과로 생성된 새로운 컬럼에 이름을 붙이기 위해서.
# 집계함수 종류 -> sum, mean, median, count, std, min, max ...
df.groupby('nclass').mean() # 통계량을 한번에 구하는 방법. 위의 집계함수에서 '()'를 붙여서 사용하면 됨.

car = pd.read_excel('dfdata/mpg.xlsx')
car.groupby(['manufacturer', 'drv']).agg(mean_cty = ('cty','mean')) # 집단 내의 집단을 만듦. manufacturer가 상위집단, drv가 하위집단.
# 그룹화는 (mean_cty컬럼)은 car['cty']의 평균값으로 계산함.
# 따라서 manufacturer의 drv가 같은 행들의 car['cty']의 평균값으로 그룹화되는 것임.

car['drv'].value_counts() # 해당 컬럼의 집단별 빈도를 쉽게 구하는 코드. 자동 내림차순 정렬 (+) 시리즈로 출력되기 때문에, query() 사용불가.
# (=) car.groupby('drv').agg(drv_count = ('drv','count'))
# car.groupby('drv').agg(drv_count = ('drv','count')).query('drv_count>100')는 DataFrame으로 출력되기 때문에 query() 사용가능





#%% Quiz
# 1. exam.csv를 활용하여, 각 분반별 영어 점수의 합계를 출력하라.

# 2. 어떤 차종의 도시 연비가 높은지 비교하려고 함. category별 cty평균을 구하라. (car 객체를 사용할 것.)

# 3. 3번의 출력 결과는 category값 알파벳순으로 정렬되어 있다. cty의 평균이 높은 순(내림차순을 의미)으로 정렬하라.

# 4. 회사별 'compact'

# 6. 제조 회사별로 'suv' 자동차의 도시 및 고속도로 합산 연비 평균을 구해 내림차순으로 정렬하고, 1~5위까지 출력하라. (car 객체를 사용할 것.)

#<정답>
# 1. df.groupby('nclass').agg(english_sum = ('english','sum'))

# 2. car.groupby('category').agg(category_mean=('cty', 'mean'))

# 3. car.groupby('category').agg(category_mean=('cty', 'mean')).sort_values('category_mean',ascending=False)

# 4. 

# 6. 
# car.query('category == "suv"') \
#     .assign(total = (car['cty']+car['hwy'])) \
#         .groupby('manufacturer') \
#             .agg(mean_data = ('total','mean')) \
#                 .sort_values('mean_data',ascending = False) \
#                     .head(5)
