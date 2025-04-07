import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 읽기
df = pd.read_csv('dfdata/timeseries.csv')
df['new_Date']=pd.to_datetime(df['Date'])
df.info()
df['Year'] = df['new_Date'].dt.year
print(df)
