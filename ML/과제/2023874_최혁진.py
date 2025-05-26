import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 데이터프레임 생성
fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8, 
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7, 
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]
df = pd.DataFrame({
    'length': fish_length,
    'weight': fish_weight
})

# 표준화
scaler = StandardScaler()
result = scaler.fit_transform(df)
df_scaled = pd.DataFrame(result, columns=df.columns)
print(df_scaled.head())

# inertias 계산 (최적의 K값을 구하기 위한)
ks = range(1, 10)
# inertias = pd.Series(dtype='float64')
inertias = pd.Series([])
for k in ks:
    model = KMeans(n_clusters=k, n_init=10, random_state=123)
    model.fit(df_scaled)
    inertias.loc[k] = model.inertia_

# 시각화
plt.figure(figsize=(7, 4))
inertias.plot.line(title='Inertias Score',
                   xlabel='Number of Clusters (k)',
                   ylabel='Inertia')
plt.show()
