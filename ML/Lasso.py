import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
import matplotlib.pyplot as plt

# 특성의 종류가 별로 없다면 특성공학으로 특성을 늘리고, 단위가 서로 다르면 이를 정규화해서 모델 성능을 높인다

df = pd.read_csv("https://bit.ly/perch_csv_data")
perch_full = df.to_numpy()
perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0,
       115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0,
       150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0,
       218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0,
       556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0,
       850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0,
       1000.0])

train_input, test_input, train_target, test_target = train_test_split(perch_full,perch_weight,random_state=42)

poly=PolynomialFeatures(degree=5, include_bias=False) #특성 개수를 늘리는 것은 degree인자로 설정
poly.fit(train_input)
train_poly=poly.transform(train_input)

lr = LinearRegression()
lr.fit(train_poly,train_target)
test_poly = poly.transform(test_input)
print(lr.score(train_poly,train_target))
print(lr.score(test_poly,test_target))

#특성 정규화 하기
ss = StandardScaler()
ss.fit(train_poly)
train_scaled=ss.transform(train_poly)
test_scaled=ss.transform(test_poly)


# 릿지의 적절한 alpha값을 조정하여 적절한 alpha값 찾기.
alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]
train_score, test_score = [], []
for alpha in alpha_list:
    lasso = Lasso(alpha = alpha, max_iter=10000)
    lasso.fit(train_scaled,train_target)
    train_score.append(lasso.score(train_scaled,train_target))
    test_score.append(lasso.score(test_scaled,test_target))
    
plt.plot(np.log10(alpha_list),train_score)
plt.plot(np.log10(alpha_list),test_score)
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.show()

