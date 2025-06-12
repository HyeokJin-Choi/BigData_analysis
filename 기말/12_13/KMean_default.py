import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns

# 데이터 준비비
df = pd.read_csv('C:/Users/samsung/Desktop/BigData_analysis/dfdata/iris.csv')
df.drop('Species',axis=1,inplace=True)

# 데이터 표준화(데이터 스케일링)
scaler = StandardScaler()
result = scaler.fit_transform(df)
df_scaled = pd.DataFrame(result, columns=df.columns)
print(df_scaled.head())

# 군집화
model = KMeans(n_clusters=3, n_init=10, random_state=123) 
model.fit(df_scaled) 

# 군집화 결과 확인
print(model.cluster_centers_)              # 군집 중심점 좌표, 차원의 축소를 안 했으니 각 점은 4개의 좌표를 가짐
print(model.labels_)                           # 각행의 군집 번호, n_clusters를 3으로 설정했으니 0 1 2 이렇게 세개의 군집으로 구분됨
print(model.inertia_)                         # 군집 평가 점수, 각 행의 각 중심점과의 거리에 대한 합산을 계산한 것이므로, 해당 값이 작아야 잘 뭉쳐있음을 의미
# 따라서 model.inertia_로 최적의 n_clusters의 값을 설정할 수 있음.

# 차원축소
pca = PCA(n_components=2)          
transform = pca.fit_transform(df_scaled)          # 2차원으로 축소 
transform = pd.DataFrame(transform)
transform['cluster'] = model.labels_              # 군집정보 추가
print(transform.head())

# 시각화
sns.scatterplot(
    data=transform,
    x = 0,                              # x축 
    y = 1,                              # y축
    hue="cluster",                      # 원의 색 
    palette='Set2',                     # 팔레트 선택
    legend=False                        # 범례표시 여부
)

# 산점도를 확인해보면 알 수 있듯, 실제 iris 품종에 따른 데이터 분포와 거의 일치함.
plt.show()
