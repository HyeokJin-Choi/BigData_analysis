# 해당 코드는  **농어(perch)**의 **길이(length)**에 따라 **무게(weight)**를 예측하는 회귀(regression) 모델.
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
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
train_input,test_input,train_target,test_target = train_test_split(perch_length,perch_weight,random_state=42)

# 머신러닝 모델에 데이터를 넣기 위해 입력 데이터를 2차원 형태로 바꿔주는 역할
train_input = train_input.reshape(-1,1)
test_input = test_input.reshape(-1,1)
# 2차원 형태로 바뀜
# print(train_input)

# 근접값을 3으로 설정하고, 농어의 길이를 이용해 무게를 분류함.
knr = KNeighborsClassifier(n_neighbors=3)
knr.fit(train_input, train_target)
# 길이가 50인 농어의 무게에 대해서 예측함.
# print(knr.predict([[50]]))

# distances, indexes = knr.kneighbors([[50]])
# plt.scatter(train_input,train_target)
# plt.scatter(train_input[indexes],train_target[indexes],marker='D')
# # 해당 길이 50의 값을 수정해보면서 농어의 길이에 따른 무게가 어디에 위치하는지 시각적으로 확인
# # 길이를 100으로 수정했을 때 해당 선형회귀의 단점을 확인할 수 있음.
# # -> 훈련세트의 범위를 벗어나면 엉뚱한 값을 예측하기 때문.
# pred_data = knr.predict([[50]])
# plt.scatter(50,pred_data,marker='^')
# plt.show()

#%% KNN의 한계 극복: 선형 회귀를 사용하여 외삽 문제 해결
# KNN은 훈련 데이터 범위 밖의 입력값에 대해 예측력이 떨어지는 단점이 있음.
# 선형 회귀는 전체적인 추세를 학습해 외삽도 가능함.

# lr = LinearRegression()                  # 선형 회귀 모델 객체 생성
# lr.fit(train_input, train_target)        # 훈련 데이터를 이용해 모델 학습
# print(lr.predict([[50]]))               # 길이 50cm인 농어의 무게 예측
# print(lr.coef_, lr.intercept_)          # 기울기와 절편 출력

# plt.scatter(train_input,train_target)
# # y = a*x + b 형태의 일차방정식 예측 모델(y는 예측값 무게, x는 입력값 길이, a는 기울기, b는 절편)
# plt.plot(train_input,lr.coef_*train_input+lr.intercept_)
# # 해당 길이 50의 값을 수정해보면서 농어의 길이에 따른 무게가 어디에 위치하는지 시각적으로 확인
# # 길이를 100으로 수정했을 때 해당 선형회귀의 단점을 극복한 것을 확인할 수 있음.
# plt.scatter(50,lr.predict([[50]]),marker="^")
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()

#%% 위의 회귀 방식은 일차 방정식을 사용하지만, 2차 방정식을 사용한다면?
# 좀 더 정확한 모델이 생성되겠지.

train_poly = np.column_stack((train_input **2, train_input))
test_poly = np.column_stack((test_input**2,test_input))

lr = LinearRegression()                  # 선형 회귀 모델 객체 생성
lr.fit(train_poly, train_target)        # 훈련 데이터를 이용해 모델 학습
print(lr.predict([[50**2,50]]))               # 길이 50cm인 농어의 무게 예측
print(lr.coef_, lr.intercept_)

point = np.arange(15,50)
plt.scatter(train_input,train_target)
# y = a*x^2 + a*x + b, 곡선형태
plt.plot(point, lr.coef_[0]*point**2 + lr.coef_[1]*point + lr.intercept_)
plt.scatter(50,lr.predict([[50**2,50]]),marker="^")
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
