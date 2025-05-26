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


#코드 12-2에 이어서 실행
ks = range(1,10) # 군집의 개수
inertias = pd.Series([]) # 군집화 평가 결과
for k in ks:
    model = KMeans(n_clusters=k, n_init=10, random_state=123)
    model.fit(df_scaled)
    inertias.loc[k] = model.inertia_
plt.figure(figsize=(7, 4))
inertias.plot.line(title = 'Inertias Score',
xlabel= 'number of clusters, k',
ylabel = 'inertia')
plt.show()

