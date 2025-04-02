import pandas as pd  # pandas 라이브러리 임포트 (데이터 처리용)
import matplotlib.pyplot as plt  # matplotlib 라이브러리 임포트 (그래프 그리기용)
from pandas.api.types import CategoricalDtype  # pandas에서 자료형을 설정하기 위한 CategoricalDtype 임포트

# 그래프에 한글을 나타내기 위한 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # 그래프에서 한글을 사용할 수 있게 폰트를 설정
plt.rcParams['axes.unicode_minus'] = False  # 그래프에서 음수 부호가 깨지지 않도록 설정

## (1) 데이터 준비 -------------------------
# 'BostonHousing.csv' 파일을 읽어와 DataFrame으로 저장
df = pd.read_csv('dfdata/BostonHousing.csv')

# 분석에 필요한 5개의 컬럼만 선택하여 새로운 DataFrame 생성
df = df[['crim', 'rm', 'dis', 'tax', 'medv']]  # 'crim' : 범죄율, 'rm' : 방의 개수, 'dis' : 직업센터까지의 거리, 'tax' : 재산세, 'medv' : 주택가격

# 각 컬럼에 대한 한글 제목을 리스트로 정의
titles = ['1인당 범죄율', '방의 개수', '직업센터까지의 거리', '재산세', '주택가격']

## (2) 그룹 컬럼 추가 ----------------------
# 'grp'라는 새로운 컬럼을 생성하여 주택가격을 기준으로 'L', 'M', 'H'로 그룹화
grp = pd.Series(['M' for i in range(len(df))])  # 우선 모든 행에 'M' (중간)을 할당
grp.loc[df.medv >= 25.0] = 'H'  # 주택가격이 25.0 이상이면 'H' (높음)로 그룹화
grp.loc[df.medv <= 17.0] = 'L'  # 주택가격이 17.0 이하이면 'L' (낮음)으로 그룹화

# 'grp' 컬럼을 DataFrame에 추가
df['grp'] = grp

# 'grp' 컬럼의 자료형을 'L', 'M', 'H' 순서대로 설정하고 순서를 지정 (주택가격 그룹의 순서를 의미)
new_odr = ['H', 'M', 'L']  # 높은 가격(H), 중간(M), 낮은 가격(L)
new_dtype = CategoricalDtype(categories=new_odr, ordered=True)  # 순서가 있는 범주형 자료형으로 지정
df.grp = df.grp.astype(new_dtype)  # 'grp' 컬럼의 자료형을 변경
df.grp.dtype  # 'grp' 컬럼의 자료형 확인

## (3) 데이터셋 기본정보 확인 ----------------------
# 데이터셋의 크기(행, 열의 개수) 확인
df.shape

# DataFrame의 처음 5개의 행을 출력하여 데이터 구조 확인
df.head()

# 각 컬럼의 자료형을 확인
df.dtypes

# 'grp' 컬럼에서 각 그룹(L, M, H)의 개수를 출력 (주택가격 그룹별 분포)
df.grp.value_counts(sort=False)

## (4) 히스토그램 ----------------------
# 히스토그램을 그리기 위한 화면을 2x3 형태로 분할
fig, axes = plt.subplots(nrows=2, ncols=3)

# 그래프 간 여백을 설정 (세로 여백 0.5, 가로 여백 0.3)
fig.subplots_adjust(hspace=0.5, wspace=0.3)

# 각 분할된 화면에 히스토그램을 그리기
for i in range(5):
    # 각 컬럼별로 히스토그램을 그리고, 'titles' 리스트에 있는 제목을 사용하여 x축과 y축 레이블 지정
    df[df.columns[i]].plot.hist(ax=axes[i//3, i%3], ylabel='', xlabel=titles[i])

# 전체 그래프에 제목 지정
fig.suptitle('Histogram', fontsize=14)

# 히스토그램 그래프를 화면에 나타내기
fig.show()

## (5) 상자그림 (Boxplot) ----------------------
# 상자그림을 그리기 위한 화면을 2x3 형태로 분할
fig, axes = plt.subplots(nrows=2, ncols=3)

# 그래프 간 여백을 설정 (세로 여백 0.5, 가로 여백 0.3)
fig.subplots_adjust(hspace=0.5, wspace=0.3)

# 각 분할된 화면에 상자그림을 그리기
for i in range(5):
    # 각 컬럼별로 상자그림을 그리고, 'titles' 리스트에 있는 제목을 사용하여 레이블 지정
    df[df.columns[i]].plot.box(ax=axes[i//3, i%3], label=titles[i])

# 전체 그래프에 제목 지정
fig.suptitle('Boxplot', fontsize=14)

# 상자그림 그래프를 화면에 나타내기
fig.show()
