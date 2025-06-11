# 해당 코드는 생선의 길이와 무게로 도미와 빙어를 구별하는 k-최근접 회귀분석 코드임. ~8page
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8, 
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7, 
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

#fish_length와 fish_weight 리스트를 (길이, 무게)의 2차원 배열로 합침.
fish_data= np.column_stack((fish_length,fish_weight))
# print(fish_data.shape)
# 상위 35개의 물고기는 1 (도미 등 양식 대상 생선), 나머지 14개는 0 (빙어 등 작은 생선)으로 라벨링
fish_target = np.concatenate([np.ones(35),np.zeros(14)])
# print(fish_target) 1, 0의 값만 가짐.

# train_test_split()의 기본값은 75% 훈련, 25% 테스트 비율
train_input,test_input,train_target,test_target = train_test_split(fish_data,fish_target,stratify=fish_target,random_state=42)
# 따라서 36개가 train, 13개가 test로 됨.
# print(train_input.shape,test_input.shape)

kn = KNeighborsClassifier() # kn은 K-최근접 이웃(KNN) 분류기 객체. 기본값으로 n_neighbors=5 (가장 가까운 5개의 데이터를 참고해서 예측)
kn.fit(train_input,train_target) # 훈련 데이터를 사용해 모델을 저장.
# 테스트 데이터를 넣어서 정확도(Accuracy)를 출력. score()는 내부적으로 predict()를 호출하고, 예측값과 실제 test_target을 비교하여 정답률을 계산
# print(kn.score(test_input,test_target)) 

# 길이 25cm, 무게 150g인 물고기가 어떤 종류(클래스)로 분류되는지를 K-최근접 이웃(KNN) 모델을 통해 예측
# 출력이 0이면 빙어, 1이면 도미
# print(kn.predict([[25,150]]))

# 길이, 무게를 기준으로 그래프를 그림
# plt.scatter(train_input[:,0],train_input[:,1])
# plt.scatter(25,150,marker='^')
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()

# 기본값으로 n_neighbors=5로 설정되어 있으니, 길이 25, 무게 150인 물고기의 최근접 이웃 5마리의 결과를 보여줌.
# 출력의 앞쪽 arrays는 이웃간의 거리를, 뒷 arrays는 이웃의 index값을 출력함
# print(kn.kneighbors([[25,150]]))




