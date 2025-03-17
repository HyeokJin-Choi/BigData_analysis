import pandas as pd
import numpy as np

# irisdf = pd.read_csv('dfdata/iris.csv')
# irisdf.info() # 열의 개수와 해당 열이 가지는 원소에 대한 특징을 산출
# print(irisdf.head(10))
# print(irisdf['Species'].unique()) # Species컬럼의 종류 확인.
# print(irisdf.loc[:,~irisdf.columns.isin(['Species'])]) # Species 컬럼을 제거한 irisdf내용 출력

examdf = pd.read_csv('dfdata/exam.csv')
# print(examdf.describe())
examdf['total'] = examdf['math'] + examdf['science']
# examdf['test'] = np.where(examdf[])
# print(np.where(examdf['total']>160,'pass','fail'))
w = examdf['math']>examdf['math'].quantile(0.9) # True Or Fals를 반환.
print(examdf[w]) # index부분에 True, False를 반환되는값을 넣을 시 해당 조건에 맞는 행을 도출
