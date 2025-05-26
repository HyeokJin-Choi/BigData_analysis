import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# 데이터 불러오기 및 전처리
df = pd.read_csv('C:/Users/win/Desktop/iris.csv')
df = df.drop('Species', axis=1)
print(df.head())

# 표준화
scaler = StandardScaler()
result = scaler.fit_transform(df)
df_scaled = pd.DataFrame(result, columns=df.columns)
print(df_scaled.head())

# KMeans 클러스터링
model = KMeans(n_clusters=3, n_init=10, random_state=123) # 데이터는 3개의 그룹(k=3) 으로 나눔
model.fit(df_scaled)
print(model.cluster_centers_)
print(model.labels_)
print(model.inertia_)

# PCA 변환
# 원래 iris 데이터는 총 4개의 특성(sepal length, sepal width, petal length, petal width)을 가지고 있어서 4차원 데이터
pca = PCA(n_components=2) # PCA를 통해 이를 2개의 주성분(Principal Components) 으로 축소 → 2차원 공간에 표현
transform = pca.fit_transform(df_scaled)
transform = pd.DataFrame(transform)
transform['cluster'] = model.labels_
print(transform.head())

# 시각화
sns.scatterplot(data=transform, x=0, y=1, hue="cluster", palette='Set2', legend=False)
plt.title("KMeans Clustering Result (PCA 2D Projection)")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.show()

