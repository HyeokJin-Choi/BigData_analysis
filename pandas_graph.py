import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 읽기
df = pd.read_csv('C:/Users/thdgh/Downloads/dfdata/iris.csv')

# 품종별 Petal_Length 추출
setosa = df.query('Species == "setosa"')['Petal_Length']
versicolor = df.query('Species == "versicolor"')['Petal_Length']
virginica = df.query('Species == "virginica"')['Petal_Length']

# 서브플롯 생성 (1행 3열)
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 각 서브플롯에 KDE 그래프 개별로 그리기
setosa.plot.kde(ax=axes[0], title='Setosa')
versicolor.plot.kde(ax=axes[1], title='Versicolor')
virginica.plot.kde(ax=axes[2], title='Virginica')

# 축 라벨 설정
axes[0].set_xlabel('Petal Length')
axes[0].set_ylabel('Density')

axes[1].set_xlabel('Petal Length')
axes[1].set_ylabel('Density')

axes[2].set_xlabel('Petal Length')
axes[2].set_ylabel('Density')

# 전체 제목
fig.suptitle('Petal Length KDE by Species', fontsize=14)

plt.tight_layout()
plt.show()
