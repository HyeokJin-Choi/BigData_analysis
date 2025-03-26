import pandas as pd
import numpy as np

irisdf = pd.read_csv('dfdata/iris.csv')
# irisdf.info() # 열의 개수와 해당 열이 가지는 원소에 대한 특징을 산출
# print(irisdf.head(10))
# print(irisdf['Species'].unique()) # Species컬럼의 종류 확인.
# print(irisdf.loc[:,~irisdf.columns.isin(['Species'])]) # Species 컬럼을 제거한 irisdf내용 출력
# sort1 = irisdf.sort_values(by='Species')
# irisdf.info()
# print(irisdf['Species'].unique()) # sort를 알파벳 순서로 했기 때문에 알파벳 순으로 나옴
# species_category=['versicolor','virginica','setosa']
# irisdf['Species'] = pd.Categorical(irisdf['Species'],categories = species_category, ordered = True)
# # Categorical 함수는 클래스 생성자로써 원본 데이터의 카테고리화를 진행한다.(해당 원소만 다룰 수 있게)
# irisdf.info()
# print(irisdf['Species'].unique())



examdf = pd.read_csv('dfdata/exam.csv')
# print(examdf.describe())
#examdf['total'] = examdf['math'] + examdf['science']
# examdf['test'] = np.where(examdf[])
# print(np.where(examdf['total']>160,'pass','fail'))
#w = examdf['math']>examdf['math'].quantile(0.9) # True Or Fals를 반환.
#print(examdf[w]) # index부분에 True, False를 반환되는값을 넣을 시 해당 조건에 맞는 행을 도출
#print(examdf.columns)
examdf2 = examdf[['math', 'english', 'science']]
# examdf['sum'] = examdf2.sum(axis=1)
# print(examdf)
examdf2.sum(axis=1)

# agg()함수를 단독으로 사용하면 시리즈 자료구조 형태로 반환하므로, query()를 사용하여 조건을 부여하지 못하고, loc를 통해서 조건을 부여해야하는 단점이 있음.
# groupby()함수를 사용하면 데이터프레임 자료구조 형태로 반환하므로, query()를 사용하여 조건을 부여할 수 있음


mpg = pd.read_excel('dfdata/mpg.xlsx')
data = mpg.query('category == "suv"') \
    .assign(total = (mpg['cty'] + mpg['hwy'])/2) \
        .groupby('manufacturer') \
            .agg(total_mean = ('total','mean')) \
                .sort_values('total_mean',ascending = False) \
                    .head(5)
                    
data_test = mpg.groupby(['category'],as_index=False).agg(cty_mean = ('cty','mean'))


