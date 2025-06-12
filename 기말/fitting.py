# 해당 코드는  **농어(perch)**의 **길이(length)**에 따라 **무게(weight)**를 예측하는 회귀(regression) 모델.
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#linear regression
perch_length = np.array([8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0, 21.0,
       21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5, 22.5, 22.7,
       23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5, 27.3, 27.5, 27.5,
       27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0, 36.5, 36.0, 37.0, 37.0,
       39.0, 39.0, 39.0, 40.0, 40.0, 40.0, 40.0, 42.0, 43.0, 43.0, 43.5,
       44.0])
perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0,
       115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0,
       150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0,
       218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0,
       556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0,
       850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0,
       1000.0])

# perch_length	입력값(독립 변수) — 물고기의 길이
# perch_weight	타겟값(종속 변수) — 물고기의 무게
# train_input	훈련에 사용할 물고기 길이 데이터
# test_input	테스트에 사용할 물고기 길이 데이터
# train_target	훈련에 사용할 물고기 무게 데이터
# test_target	테스트에 사용할 물고기 무게 데이터
# train_input,test_input,train_target,test_target = train_test_split(perch_length,perch_weight,random_state=42)

# # 머신러닝 모델에 데이터를 넣기 위해 입력 데이터를 2차원 형태로 바꿔주는 역할
# train_input = train_input.reshape(-1,1)
# test_input = test_input.reshape(-1,1)
# # 2차원 형태로 바뀜
# # print(train_input)

# # 근접값을 3으로 설정하고, 농어의 길이를 이용해 무게를 분류함.
# knr = KNeighborsRegressor(n_neighbors=5)
# knr.fit(train_input, train_target)

# # train < test 라면 과소적합, train > test라면 과대적합.
# # 과소적합이라면 KNeighbors문제에서 k의 값을 줄일 필요가 있음.(모델을 좀 더 복잡하게 훈련.)
# # 과대적합이라면 KNeighbors문제에서 k의 값을 늘릴 필요가 있음.(모델을 좀 더 단순하게 훈련.)
# print('train',knr.score(train_input, train_target))
# print('test',knr.score(test_input, test_target))

#%% 톡성 공학
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('https://bit.ly/perch_csv_data')
perch_full=df.to_numpy()
# print(perch_full)

train_input,test_input,train_target,test_target = train_test_split(perch_full,perch_weight,random_state=42)

poly = PolynomialFeatures(include_bias=False)
# # x1 = 2, x2 = 3
# poly.fit([[2,3]])
# # x1, x2, x1^2, x1*x2, x2^2
# print(poly.transform([[2,3]]))

poly.fit(train_input)
train_poly = poly.transform(train_input)
print(train_poly.shape)
print(poly.get_feature_names_out()) # x0, x1, x2에 관해서 제곱하고, 곱하고...
print(train_input) # 특성이 3개임을 확인.

lr = LinearRegression()
lr.fit(train_poly,train_target)
# R^2의 계산방법 
# y_pred = lr.predict(train_poly)
# y_true = train_target
# r2 = 1 - np.sum((y_true - y_pred)**2) / np.sum((y_true - np.mean(y_true))**2)
print(lr.score(train_poly,train_target))
test_poly=poly.transform(test_input)
print(lr.score(test_poly,test_target))
