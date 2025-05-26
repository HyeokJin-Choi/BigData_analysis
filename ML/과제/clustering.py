import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# 데이터 불러오기 및 전처리
df = pd.read_csv('C:/Users/win/Desktop/iris.csv')
df = df.drop('Species', axis=1)
print(df.head())

# 표준화
scaler = StandardScaler()
result = scaler.fit_transform(df)
df_scaled = pd.DataFrame(result, columns=df.columns)
print(df_scaled.head())

# PCA 변환
pca = PCA(n_components=2)
transform = pca.fit_transform(df_scaled)
transform = pd.DataFrame(transform)
print(transform.head())

# 시각화
transform.plot.scatter(x=0, y=1, title='PCA plot')
plt.show()
