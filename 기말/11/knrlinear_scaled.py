# 해당 코드는 생선의 길이와 무게로 도미와 빙어를 구별하는 k-최근접 회귀분석 코드임.
# 길이와 무게의 두 특성은 다르기 때문에 데이터의 전처리가 필요함.
# 표준점수 z를 사용.
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

# 데이터 전처리
mean = np.mean(train_input, axis=0)
std = np.std(train_input, axis=0)

# 표준화된 train값
train_scaled = (train_input - mean) / std
new = ([25, 150] - mean) / std

# 그래프 준비
fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # 1행 3열

# 1️⃣ 원래 데이터 (스케일 전)
axes[0].scatter(train_input[:, 0], train_input[:, 1])
axes[0].scatter(25, 150, marker='^', color='red')
axes[0].set_title('Original Data')
axes[0].set_xlabel('Length')
axes[0].set_ylabel('Weight')

# 2️⃣ 표준화된 데이터
axes[1].scatter(train_scaled[:, 0], train_scaled[:, 1])
axes[1].scatter(new[0], new[1], marker='^', color='red')
axes[1].set_title('Standardized Data')
axes[1].set_xlabel('Length (scaled)')
axes[1].set_ylabel('Weight (scaled)')

# 표준화된 훈련 데이터를 사용해 KNN 모델 재학습
kn.fit(train_scaled, train_target)
# 테스트 데이터도 훈련 데이터의 평균과 표준편차를 이용해 동일하게 표준화
test_scaled = (test_input - mean)/std
# 새 데이터([25, 150]의 표준화 버전) 주변의 가장 가까운 5개의 훈련 샘플 정보(거리와 인덱스) 구하기
distance, indexes = kn.kneighbors([new])
# ▶️ 세 번째 그래프: 표준화된 데이터 분포와 이웃 시각화
axes[2].scatter(train_scaled[:, 0], train_scaled[:, 1])
axes[2].scatter(new[0], new[1], marker='^', color = 'red')
axes[2].scatter(train_scaled[indexes,0],train_scaled[indexes,1],marker='D')
axes[2].set_title('Standardized Data with Neighbors')
axes[2].set_xlabel('Length (scaled)')
axes[2].set_ylabel('Weight (scaled)')

# 그래프 보여주기
plt.tight_layout()
plt.show()

# 표준화를 진행한 후 예측 결과가 달라진 이유는 두 특성(길이와 무게)의 단위와 크기 차이로 인해 생긴 문제를 해결했기 때문
print(kn.predict([new]))


