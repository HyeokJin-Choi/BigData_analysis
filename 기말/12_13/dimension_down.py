import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 데이터 준비비
df = pd.read_csv('C:/Users/samsung/Desktop/BigData_analysis/dfdata/iris.csv')
df.drop('Species',axis=1,inplace=True)

# 데이터 표준화(데이터 스케일링)
scaler = StandardScaler()
result = scaler.fit_transform(df)
df_scaled = pd.DataFrame(result, columns=df.columns)
print(df_scaled.head())

# 차원축소
pca = PCA(n_components=2) # 2차원으로 축소
transform = pca.fit_transform(df_scaled)  # df_scaled(4차원) -(pca)-> transform(2차원)
transform = pd.DataFrame(transform)
print(transform.head())

# 시각화
transform.plot.scatter(x=0, y=1, title='PCA plot') # 산점도
plt.show()
