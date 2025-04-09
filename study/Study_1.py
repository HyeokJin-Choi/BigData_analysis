import pandas as pd
import numpy as np

df = pd.read_csv('dfdata/exam.csv')
df.index
df.columns
df.describe() #기술의 통계 mean결과 count결과 std결과 ....
df.info() # df의 객체 정보
df.sort_values(by='math',ascending=True).head(5)

df['total'] = df['math'] + df['science'] # math컬럼과 science컬럼의 합을 새로운 total이라는 컬럼으로 df에 추가함.
# df['total3'] = df[['math','science']].sum(axis=1) # axis = 1이라면 열의 합계(두 math와 science를 합쳐서 하나의 컬럼으로 만듦). 따라서 위의 코딩과 같은 역할. axis = 0이라면 행의 합계.
df['total'].mean()
df['total'].sum()
df['test'] = np.where(df['total']>=df['total'].mean(),'pass','fail')


#df.query('test >= total.mean()') # query는 문자열 내에서 변수나 함수 호출을 사용할 수 없고, 변수로 지정해야함. 
# 이렇게 사용하고 싶다면 mean_total = df['total'].mean() 지정 후 df.query('total >= @mean_total')
df['total']>=df['total'].quantile(0.9) # df['total']컬럼의 상위 10%의 결과를 보여줌. df.sort_values(by='total',ascending=False)로 확인해볼것.
df.insert(6,'total2',200) # 6번째 열을 삽입함. 해당 열의 이름은 total2이며 모든 원소의 값을 200으로 설정함.
df.dtypes # 각 컬럼들의 data type을 확인함
df['total2'].astype('str') # total2 컬럼의 data type을 Object형으로 고침. (문자열은 기본적으로 Object타입)
# category타입은 범주형 데이터를 분석할 때 용량과 속도 면에서 매우 효과적. 문자열의 특수한 형태, 몇 가지 번주가 가능한 문자열임.
df.drop(['total2'], axis=1) # axis = 1이면 열, axis = 0이면 행을 뜻. 현재 해당 코드에서 total2는 열임.
# df.drop([0], axis=0) #index가 0번인 행을 삭제

#%%
df = pd.read_csv('dfdata/weather.csv')
df[df['max_wind'].isna()] # 누락된 데이터를 표시, 두번 감싸는 이유는 dataFrame화 해서 보여주기 위함. df.iloc[559] 일치하는 지 확인. NaN으로 출력(Not a Number)
# df[]안에 또 df를 선언하면서 접근하는 이유는, 해당 열(단일 열만 pandas에서 지원)에 대해서 메서드를 실행시키기 위함임.
df.isnull().sum() # 누락된 데이터에 대한 개수(.sum()함수가 개수의 출력을 보조) 출력, notnull()은 반대.
df.dropna() # 누락된 데이터 제거.
df.fillna(0) # 누락된 데이터를 0으로 채움.

#%%
df_Univ = pd.DataFrame([['공부','운동','연애','회장'],['공부','연애','운동','회장'],['취업','공부','연애','운동']],index=['2학년','3학년','4학년'] ,columns = ['1순위','2순위','3순위','4순위'])
df_Social = pd.DataFrame([['취업','연애','공부','운동'],['결혼','직장','운동','취미'],['아내','취미','직장','운동']],index=['20대','30대','40대'] ,columns = ['1순위','2순위','3순위','4순위'])
df_concat = pd.concat([df_Univ,df_Social], axis = 0) # axis가 0이면 행의 밑에 붙임. axis가 열이면 열 옅에 붙임. 기준은 []의 안에서 먼저 등록된(콤마를 기준으로 가장 왼쪽) 객체를 기준.

#%%
df_Military = pd.DataFrame({'이름' : ['박병필','송홍영','정지석','최혁진','최강'],'군번' : [1001,1002,1003,1004,1005]})
df_Militarykind = pd.DataFrame({'이름' : ['박병필','송홍영','정지석','최혁진'], '군종' : ['땅개','땅개','땅개','해병대']})
df_man = pd.merge(df_Military, df_Militarykind, how='left', on='이름') # how가 inner면 on으로 설정한 컬럼에서 같은 데이터들만 보여주는 것. 
# how가 outer면 on으로 설정한 컬럼이 같지 않아도 보여줌. 대신 결측치에 대해 대해서 NaN으로 출력함.
# how가 left면 df_Military는 무조건 다 가져오고, 결측치에 대해 대해서 NaN으로 출력함.
# how가 right면 df_Militarykind 무조건 다 가져오고, 결측치에 대해 대해서 NaN으로 출력함.

#%% Quiz 
#---------------------------------------------------------------------------------
# 1. max_wind에 누락된 데이터가 존재한다면, 해당 값을 max_wind의 평균값으로 대체하라.

#---------------------------------------------------------------------------------
# 2. df_man = df_man = pd.merge(df_Military, df_Militarykind, how='right', on='이름')의 결과값을 적어보아라. (+) 현재의 객체를 이용한다면 how = ''의 어떤 동작과 일치하게 하는가?

# 3. df_man = df_man = pd.merge(df_Military, df_Militarykind, how='outer', on='이름')의 결과와 같은 결과를 출력하는 merge는? (현재의 객체를 기준)
#   (1)-how='inner' (2)-how='left' (3)-how='right'

#---------------------------------------------------------------------------------
# 4. df_Military객체에서 이름이 '최강'인 행을 삭제하라.




#<정답>
# 1. 
# print(df.isnull().sum())
# df['max_wind'] = np.where(df['max_wind'].isnull(),df['max_wind'].mean(),df['max_wind'])
# df['max_wind'] = df['max_wind'].fillna(df['max_wind'].mean())
# df['max_wind'].fillna(df['max_wind'].mean(), inplace = True) # inplace = True는 df['max_wind'] = 이런 식으로 실제로 저장된 데이터 값을 바꾸는 역할.
# print(df.isnull().sum())

#2.

#3. (2)

#4. df_Military.drop(df_Military[df_Military['이름'] == '최강'].index, axis=0, inplace=True)


