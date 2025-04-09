import pandas as pd
import numpy as np


# *** 새로운 열을 추가할때에는 ''따옴표를 붙이지 않음. 열을 불러 사용할때에는 ''따옴표를 사용.
df = pd.read_csv('../dfdata/exam.csv')
df.agg(mean_math=('math','mean')) #math의 평균값 (=) df_test = pd.DataFrame({'math' : df['math'].mean()}, index = ['mean_math'])
df.groupby('nclass', as_index = False).agg(mean_math=('math','mean')) # nclass컬럼을 기준으로 그룹화해서 보여주되, math는 평균값으로 계산함.
# as_index = False 설정을 추가하면 인덱스가 nclass 값이 아닌, 절대 인덱스로 설정됨. 그리고 그 옆에 nclass를 순으로 출력함.
# (+) 여기서 컬럼명을 할때 대괄호를 하지 않는 이유는? -> 집계 함수의 결과로 생성된 새로운 컬럼에 이름을 붙이기 위해서.
# 집계함수 종류 -> sum, mean, median, count, std, min, max ...
df.groupby('nclass').mean() # 통계량을 한번에 구하는 방법. 위의 집계함수에서 '()'를 붙여서 사용하면 됨.

car = pd.read_excel('../dfdata/mpg.xlsx')
car.groupby(['manufacturer', 'drv']).agg(mean_cty = ('cty','mean')) # 집단 내의 집단을 만듦. manufacturer가 상위집단, drv가 하위집단.
# 그룹화는 (mean_cty컬럼)은 car['cty']의 평균값으로 계산함.
# 따라서 manufacturer의 drv가 같은 행들의 car['cty']의 평균값으로 그룹화되는 것임.

car['drv'].value_counts() # 해당 컬럼의 집단별 빈도를 쉽게 구하는 코드. 자동 내림차순 정렬 (+) 시리즈로 출력되기 때문에, query() 사용불가.
# (=) car.groupby('drv').agg(drv_count = ('drv','count'))
# car.groupby('drv').agg(drv_count = ('drv','count')).query('drv_count>100')는 DataFrame으로 출력되기 때문에 query() 사용가능


#%%
bins=[-1,20,40,60,80,100]
df.loc[0,'math']=1 #값을 실제로 바꿈.
df_cut = pd.cut(df['math'],bins,labels=['F','D','C','B','A']) # 교수님께서는 df.math형태로 접근함.
#print(df_cut) # df_cut은 df의 math컬럼을 bins값을 기준으로 'F' < 'D' < 'C' < 'B' < 'A'순으로 등급을 매김. 시리즈형태의 출력.


#%%
dfiris = pd.read_csv('../dfdata/iris.csv')

sort1 = dfiris.sort_values(by='Species')
#print(sort1['Species'].head(10)) 
#print(dfiris['Species'].unique()) # dfiris객체의 Species컬럼의 원소 종류 출력
species_category = ['versicolor','virginica','setosa']
dfiris['Species'] = pd.Categorical(dfiris['Species'], categories=species_category, ordered=True)
# species_category로 정렬 순서를 지정하여, dfiris객체의 Species컬럼을 정렬함. ordered를 Ture해줘야 순서가 있는 범주형 데이터로 설정할 수 있음.
#print(dfiris['Species'].unique()) # 지정한 정렬 순서랑 상관없이 dfiris객체의 Species컬럼의 원소 종류를 출력
sort2 = dfiris.sort_values(by='Species')
#print(sort2['Species'].head(10))  # 제대로 정렬됨


#%% Quiz
# 1. exam.csv를 활용하여, 각 분반별 영어 점수의 합계를 출력하라.

# 2. 어떤 차종의 도시 연비가 높은지 비교하려고 함. category별 cty평균을 구하라. (car 객체를 사용할 것.)

# 3. 2번의 출력 결과는 category값 알파벳순으로 정렬되어 있다. cty의 평균이 높은 순(내림차순을 의미)으로 정렬하라.

# 4. 3번의 출력결과에서  평균이 가장 높은 회사 세 곳을 출력하라. (car 객체를 사용할 것.)

# 5. 회사별 'compact' 차종 수를 내림차순으로 정렬해 출력하라. (car 객체를 사용할 것.) 

# 6. 제조 회사별로 'suv' 자동차의 도시 및 고속도로 합산 연비 평균을 구해 내림차순으로 정렬하고, 1~5위까지 출력하라. (car 객체를 사용할 것.)
# (+ Hint) assign() 함수는 pandas에서 DataFrame에 새로운 열(column)을 추가하거나 수정할 때 사용되는 매우 유용한 함수 



#<정답>
# 1. df.groupby('nclass').agg(english_sum = ('english','sum'))

# 2. car.groupby('category').agg(category_mean=('cty', 'mean'))

# 3. car.groupby('category').agg(category_mean=('cty', 'mean')).sort_values('category_mean',ascending=False)

# 4. print(car.groupby('category').agg(category_mean=('cty', 'mean')).sort_values('category_mean',ascending=False).head(3))

# 5. print(car.query('category=="compact"').groupby('manufacturer').agg(car_count = ('manufacturer','count')).sort_values('car_count',ascending=False))

# 6. 
# car.query('category == "suv"') \
#     .assign(total = (car['cty']+car['hwy'])/2) \
#         .groupby('manufacturer') \
#             .agg(mean_data = ('total','mean')) \
#                 .sort_values('mean_data',ascending = False) \
#                     .head(5)


# %%
