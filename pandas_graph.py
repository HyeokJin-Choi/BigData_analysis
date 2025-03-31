쿼리 추출 
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 읽기
df = pd.read_csv('C:/Users/thdgh/Downloads/dfdata/iris.csv')

# 품종 리스트
species_list = df['Species'].unique()

# 서브플롯 생성 (1행 3열)
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# query() 사용해서 품종별 KDE 그래프
for ax, species in zip(axes, species_list):
    df.query("Species == @species")['Petal_Length'].plot.kde(ax=ax)
    ax.set_title(f'{species} Petal_Length KDE')
    ax.set_xlabel('Petal Length')
    ax.set_ylabel('Density')

# 전체 그래프 제목
fig.suptitle('Petal Length KDE by Species (Using query)', fontsize=14)

plt.tight_layout()
plt.show()
