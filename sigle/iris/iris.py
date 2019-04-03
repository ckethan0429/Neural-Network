import tensorflow as tf 
from dataload import load_data 
from classify import Classifier

#데이터 준비
train_data, test_data = load_data('./iris_150.csv', 4, 0.6)

#노드 수 결정
num_input = train_data.x_data.shape[1] #입력노드 수
num_output = train_data.y_data.shape[1] #출력노드 수

#분류기 생성
iris = Classifier(num_input, num_output, 10, 20, 0.01) #성능 미치는 것: 10,20,0.01(hiddennode, lr)

#훈련, 평가
iris.train(train_data, 10000, 100) #성능 미치는 것: 1000(훈련횟수)
iris.test(test_data)

#질의
answer = iris.query([[5.8, 4, 1.2, 0.2]])
print(answer)
iris.close()