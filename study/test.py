import pandas as pd
import numpy as np

# 데이터 입력
#code1
temp = pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

temp.index = ['온도','습도','CO2']
temp.columns = ['06시','12시','18시','00시']

temp.size # dataframe의 원소 개수
temp.dtypes # dataframe의 각 열의 type, Series 같은 경우는 .dtype
len(temp) # dataframe은 행의 개수를 띄움.
temp.shape # dataframe은 행과 열을 띄움.

temp.loc['습도':'CO2','12시':'00시'] # 12~00시의 행들을 띄우는 슬라이싱, 절대 인덱스로 하면 뒤의 값-1까지 슬라이싱하지만,
    #레이블로 슬라이싱 할 시 뒤의 레이블도 포함한 결과를 출력함
    
result = temp.loc['온도']
result.where(result>2).dropna()

test = pd.Series([1,2,3,4])
test.iloc[3] = 100; # iloc는 값의 변경이 가능하지만, 값의 추가는 불가능.
New = pd.Series({'MUS':100}) # 레이블이 지정된 원소를 가짐
test = test._append(New) # 이처럼 작성해야 변화 o, test._append()만 사용하면 변화x

test = test._append(pd.Series([100]), ignore_index = True) # 기존 인덱스와 관계없이 연속적인 새로운 인덱스가 생성, 
    #New = pd.Series({'MUS':100})을 통해 지정한 'MUS'인덱스 무시
    
test2 = test.drop(test.size - 1) #레이블 지정시, 해당 행 제거. 절대인덱스 지정시 해당 행 제거. 정수는 절대 인덱스 취급
    #inplace 매개변수를 사용하면 실제로 삭제함. test.drop(test.size - 1, inplace = True)

test2 = test # 참조의 관계이므로, test2를 수정하면 test도 수정됨.
test2 = test.copy() #복사를 하므로, test2를 수정해도 test에선 아무런 효과x


# --------------------<과제실습>---------------------
test = pd.Series([781,650,705,406,580,450,550,640],
                 index = ['A','B','C','D','E','F','G','H'])
test.where((test < 500)|(test > 700)).dropna()
test.where(test > test.loc['B']).dropna()
test.where(test < 600).dropna().index
test.where(test < 600)*1.2
test.mean(), test.sum(), test.std()
test.loc[['A','C']] = [810,820]; test
test.loc['J'] = 400; test
test.drop('J', inplace = True); test
test2 = test.copy(); test2 += 500; result = pd.DataFrame({'test':test, 'test2':test2}); result
#----------------------------------------------------

test = pd.read_csv('../dfdata/iris.csv')
test.info() # 객체에 대한 정보,열에 대한 모든 정보(컬럼명, null값 여부, 자료형)
test.shape, test.shape[0], test.shape[1] #[]를 붙이면 행(0), 열(1) 구분해서 개수 파악
test.head() # 데이터 앞부분 보기. default = 5개, 정수 넣으면 해당 정수값만큼 앞부분.
test.tail() # 데이터 뒷부분 보기. default = 5개, 정수 넣으면 해당 정수값만큼 뒷부분.
test['Species'].unique() #지정한 컬럼의 원소 종류(원소로 나온 값의 중복을 제거하여) 파악
test.loc[:,~test.columns.isin(['Species'])] # 행은 그대로 가져오되(:), 열은 'Species'를 가져오지 말것.(~)
