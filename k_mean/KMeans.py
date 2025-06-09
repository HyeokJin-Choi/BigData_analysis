import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

df = pd.read_csv('iris.csv')


inertia=[]
for k in range(2,7):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(df[['Petal_Length']])
    inertia.append(km.inertia_)
    
plt.plot(range(2,7),inertia)
plt.xlabel('k')
plt.ylabel('inertia')
plt.show()
