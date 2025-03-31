import pandas as pd
import matplotlib.pyplot as plt


# 데이터 읽기
df = pd.read_csv('C:/Users/thdgh/Downloads/dfdata/iris.csv')


# 화면 분할 정의
fig, axes = plt.subplots(nrows=2, ncols=2)


# 각 분할 영역에 그래프 작성하기
df['Petal_Length'].plot.hist(ax=axes[0,0])
df['Petal_Length'].plot.box(ax=axes[0,1])


fd = df['Species'].value_counts()


fd.plot.pie(ax=axes[1,0])
fd.plot.barh(ax=axes[1,1])

# 통합 그래프에 제목 지정
fig.suptitle('Multiple Graph Example', fontsize=14)

# 분할 그래프 화면에 나타내기
plt.show()
