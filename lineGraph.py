import pandas as pd
import matplotlib.pyplot as plt
late = pd.Series([5,8,7,9,4,6,12,13,8,6,6,4],
                 index=list(range(1,13)))
late.plot(title='Late student per month', # 제목
 xlabel= 'month', # x축 레이블
 ylabel='frequency', # y축 레이블
 linestyle='solid') # 선의 종류, 실선
plt.show()

late.plot(title='Late student per month', # 제목
 xlabel= 'month', # x축 레이블
 ylabel='frequency', # y축 레이블
 linestyle='dashed', # 선의 종류, 점선
 marker='o') # 점의 종류
plt.show()
