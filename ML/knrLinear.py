import numpy as np
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

from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(perch_length,perch_weight,random_state=42)

train_input = train_input.reshape(-1,1)
test_input = test_input.reshape(-1,1)

from sklearn.neighbors import KNeighborsRegressor

knr = KNeighborsRegressor(n_neighbors=3) #n_neighbors의 값을 수정하면서 결과를 비교해보기

knr.fit(train_input,train_target)
print("train",knr.score(train_input,train_target))
print("test",knr.score(test_input,test_target))

# n_neighbors 값에 따라 모델의 복잡도가 달라지고, 그에 따라 훈련 데이터와 테스트 데이터에서의 성능이 다르게 나타날 수 있습니다.
# n_neighbors가 작으면 훈련 데이터에서 높은 정확도를 얻을 수 있지만, 테스트 데이터에서 예측 성능이 낮을 수 있습니다(과적합).
# n_neighbors가 크면 훈련 데이터에서 정확도가 떨어질 수 있지만, 테스트 데이터에서 더 안정적이고 일반적인 성능을 보일 수 있습니다(과소적합).

# knr.score()가 의미하는 것
# score(train_input, train_target)
# → 훈련 데이터에 대한 모델의 성능을 의미합니다.
# score(test_input, test_target)
# → 테스트(검증) 데이터에 대한 모델의 일반화 성능을 의미합니다.

# 🔺 훈련 점수 높고, 테스트 점수 낮음 -> 모델이 훈련 데이터에 과하게 적합되어 테스트 데이터에서 성능이 떨어짐 -> 과적합
# 🔻 훈련 점수와 테스트 점수가 모두 낮음 -> 모델이 충분히 학습되지 않음 -> 과소적합
# ✅ 훈련 점수와 테스트 점수가 모두 적당히 높고, 큰 차이 없음 -> 일반화 성능이 좋음 -> 적절한 모델


# 성능 기록 리스트
# 우선순위 1.Train이 1에 가까운지? -> 2.Test가 1에 가가운지? -> 3.Train과 Test의 차이 D가 최소인
# results = []

# # n_neighbors를 1부터 39까지 바꿔가며 평가
# for n in range(1, 40):
#     knr = KNeighborsRegressor(n_neighbors=n)
#     knr.fit(train_input, train_target)
#     train_score = knr.score(train_input, train_target)
#     test_score = knr.score(test_input, test_target)
#     diff = abs(train_score - test_score)

#     # 각 우선순위 요소 저장
#     results.append({
#         'n': n,
#         'train_score': train_score,
#         'test_score': test_score,
#         'D': diff,
#         'train_diff_1': abs(train_score - 1),
#         'test_diff_1': abs(test_score - 1)
#     })

# # 우선순위대로 정렬
# sorted_results = sorted(
#     results,
#     key=lambda x: (x['train_diff_1'], x['test_diff_1'], x['D'])
# )

# # 가장 적절한 결과
# best = sorted_results[0]
# print(f"가장 적절한 n_neighbors 값 = {best['n']}")
# print(f"train_score = {best['train_score']:.4f}, test_score = {best['test_score']:.4f}, D = {best['D']:.4f}")
