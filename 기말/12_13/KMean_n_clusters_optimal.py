import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns

# 데이터 준비
df = pd.read_csv('C:/Users/samsung/Desktop/BigData_analysis/dfdata/iris.csv')
df.drop('Species',axis=1,inplace=True)

# 데이터 표준화(데이터 스케일링)
scaler = StandardScaler()
result = scaler.fit_transform(df)
df_scaled = pd.DataFrame(result, columns=df.columns)
print(df_scaled.head())

ks = range(1,10)                    # 군집의 개수
inertias = pd.Series([])            # 군집화 평가 결과

for k in ks:
    model = KMeans(n_clusters=k,
                   n_init=10, random_state=123)
    model.fit(df_scaled) # 함수는 모델이 데이터를 기반으로 학습을 진행하는 과정
    inertias.loc[k] = model.inertia_

plt.figure(figsize=(7, 4))
inertias.plot.line(title = 'Inertias Score',
                   xlabel= 'number of clusters, k',
                   ylabel = 'inertia')
plt.show()
