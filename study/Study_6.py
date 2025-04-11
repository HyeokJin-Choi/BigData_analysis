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


# 2단계 - 그룹 컬럼 추가
# medv를 기준으로 medv가 25.0이상이면 'H', 17.0이하면 'L', 중간이면 'M'으로 그룹을 구분하여
# df객체에 grp라는 컬럼으로 추가하시오.
# 이후 grp 컬럼의 자료형을 범주형(categorical type)으로 변경하고
# grp 컬럼의 레이블 순서를 기본 알파벳 순서('H', 'L', 'M')에서 논리적 순서('H', 'M', 'L')로 변경하시오.


# 3단계 - 데이터셋의 형태와 기본적인 내용 파악
print() # 행과 열의 개수를 띄우시오.
print() # 상위 10개의 행을 띄우시오.
print() # 컬럼별 자료형을 띄우시오. 
print() # grp의 분포를 정렬없이 띄우시오.

# 4단계 - 히스토그램으로 관측값의 분포 확인
# 화면 분할을 2x3크기로 정의하고, 각 분할 영역에 그래프 작성하시오.
# 각 그래프는 위에서 정의한 df의 각 컬럼들로 정의하시오.
# 각 그래프의 제목은 titles 객체를 이용하여 띄우시오.
# 통합 그래프에 제목을 'Histogram'으로 지정하시오.
# 그래프의 여백을 주는 코드는 fig.subplots_adjust(hspace=0.5,wspace=0.3)임.
# 해당 그래프를 해석하시오.

# 5단계 - 상자그림으로 관측값의 분포 확인

# 6단계 - 그룹별 관측값의 분포 확인
# 그룹별 상자그림을 그리시오.(.boxplot(column = df.columns[i], by='grp',grid=False,ax=axes[i//3,i%3],xlabel=titles[i]))
# 해당 그래프를 해석하시오.

# 7단계 - 다중 산점도를 통한 변수 간 상관관계의 확인
# df객체에 대한 산점도 그래프를 띄우시오.
# 해당 그래프를 해석하시오.

# 8단계 - 그룹 정보를 포함한 변수 간 상관관계의 확인
# 그룹이 있는 산점도 그래프를 출력하시오.
# 해당 그래프를 해석하시오.

# 9단계 - 변수 간 상관계수의 확인
# 상관관계를 해석하시오.






# %% <정답>
# 1단계
df = pd.read_csv('dfdata/BostonHousing.csv')
df = df[['crim','rm','dis','tax','medv']] # df는 DataFrame형태임. 따라서[[컬럼명1, 컬럼명2 ...]]형태로 가져와야함.


# 2단계
grp = pd.Series('M'for i in range(len(df))) # grp을 우선 M으로 가득 채움 (기본값 설정)
grp.loc[df.medv >= 25.0] = 'H'
grp.loc[df.medv <= 17.0] = 'L'
# loc[] 안에서는 **Boolean mask (True/False로 이루어진 시리즈)**나 정확한 인덱스를 넘겨야지, 그래야 Pandas가 올바르게 이해하고 동작
# grp.loc[[df['medv'] <= 17.0]]식으로 동작할 수 없음.
df['grp'] = grp
new_odr = ['H','M','L']
new_dtype = CategoricalDtype(categories=new_odr, ordered=True)
df.grp = df.grp.astype(new_dtype)
# print(df.grp.dtype) # df의 data type인 category를 출력


# 3단계
print(df.shape) # 행과 열의 개수를 띄우시오.
print(df.head(10)) # 상위 10개의 행을 띄우시오.
print(df.dtypes) # 컬럼별 자료형을 띄우시오. 
print(grp.value_counts(sort=False)) # grp의 분포를 정렬없이 띄우시오.


# 4단계
titles = ['1인당 범죄율', '방의개수', '직업센터까지의 거리','재산세','주택가격']
fig, axes = plt.subplots(nrows=2, ncols=3)
fig.subplots_adjust(hspace=0.5,wspace=0.3) 
for i in range (5):
    df[df.columns[i]].plot.hist(xlabel=titles[i],ylabel='',ax=axes[i//3,i%3])
fig.suptitle('Histogram', fontsize=14)
fig.show()
# 그래프에 대한 해석 (관측값들의 분포가 정규분포 형태가 아닐 경우, 분포에 대한 해석이 필요하다.)
# • 방의 개수(rm)와 주택 가격(medv) 변수는 종 모양의 정규분포에 가까운 형태를 보인다.
# • 반면, 1인당 범죄율(crim)과 직업센터까지의 거리(dis)는 관측값들이 한쪽으로 치우쳐 분포하는 특징을 가진다.
# • 재산세(tax) 변수는 중간에 관측값이 없는 "빈 구간"이 존재하는 특징이 있다.


# 5단계
fig, axes = plt.subplots(nrows=2,ncols=3)
fig.subplots_adjust(hspace=0.5, wspace=0.3)
for i in range(5):
    df[df.columns[i]].plot.box(xlabel=titles[i],by=grp, ylabel='', ax = axes[i//3,i%3])
fig.suptitle('BoxPlot', fontsize=14)
fig.show()

# 6단계
fig, axes = plt.subplots(nrows=2, ncols=3)
fig.subplots_adjust(hspace=0.5,wspace=0.3) # 그래프 여백
# 각 분할 영역에 그래프 작성하기
for i in range(5) :
    df.boxplot(column=df.columns[i], by='grp', grid=False, ax=axes[i//3,i%3], xlabel=titles[i])
fig.suptitle('Boxplot by group', fontsize=14)
fig.show()
# 그래프에 대한 해석
# – 주택 가격이 높은 지역과 중간 지역의 범죄율은 낮다.
# – 반면, 주택 가격이 낮은 지역의 범죄율은 높게 나타난다.
# • 주택 가격별 그룹에 따른 방 개수(rm)을 비교하면, 주택 가격이 높을수록 방 개수도 많아지는 경향을 보인다.
# • 주택 가격이 중간인 지역과 낮은 지역의 방 개수 평균 차이는 크지 않지만, 분포의 차이가 존재한다.
# – 중간 가격 그룹: 방 개수가 5.2~6.8 사이로 비교적 균일하게 분포
# – 낮은 가격 그룹: 방 개수가 4.5~7.2 사이로 넓게 퍼져 있어 변동성이 크다.

# 7단계
pd.plotting.scatter_matrix(df.iloc[:,:5])
plt.show()
# 그래프에 대한 해석
# • BostonHousing 데이터셋에서 주택 가격(medv)과 양의 상관성이 있는 변수는
# rm(가구당 방의 개수)로 확인된다.
# • 반면, crim(1인당 범죄율)은 주택 가격과 음의 상관성을 보인다.
# • 이는 다음과 같이 해석할 수 있다.
# – 가구당 방의 개수가 많을수록 집의 크기가 커지므로 주택 가격이 높아지는 경향이
# 있다.
# – 범죄율이 높은 지역에서는 주택 가격이 하락하는 경향을 보인다.

# 8단계
dict = {'H':'red', 'M' : 'green', 'L' : 'gray'}
colors = list(dict[key] for key in df.grp)
pd.plotting.scatter_matrix(df.iloc[:,:5],c=colors)
plt.show()
# 그래프에 대한 해석
# • 산점도 (crim-medv), (rm-medv), (dis-medv), (tax-medv)를 분석한 결과, 주택 가격
# 그룹별로 분포 위치가 뚜렷하게 구분됨을 확인할 수 있다.
# • 특히, 주택 가격 중간 그룹(녹색 점)은 상위 그룹(빨간색)이나 하위 그룹(회색)에
# 비해 변동폭이 좁다는 특징을 보인다.
# – 즉, 중간 가격대의 주택들은 가격 변동성이 상대적으로 낮은 경향을 가진다.

# 9단계
print(df.iloc[:,:5].corr())
# 상관관계에 대한 해석
# • 주택 가격(medv)과 가장 높은 상관관계를 가진 변수는 rm(가구당 방의 개수)이며, 상관계수는 0.6954이다.
# – 이는 주택 가격이 방 개수와 강한 양의 상관관계를 가지고 있음을 의미한다.
# • 산점도에서 음의 상관성이 높아 보였던 crim(1인당 범죄율)은 실제 상관계수가 0.3883으로, 기대만큼 높은 음의 상관성을 가지지는 않는다.
# – 즉, 범죄율이 주택 가격에 영향을 미치기는 하지만, 그 정도가 강하지 않음을 알 수 있다.
