import tensorflow as tf 

from tensorflow.examples.tutorials.mnist import input_data

DATA_DIR = './data'

data = input_data.read_data_sets(DATA_DIR, one_hot = True)

# 입력 데이터를 위핚 플레이스홀더
x = tf.placeholder(tf.float32, [None, 784])
# 가중치
W = tf.Variable(tf.zeros([784, 10]))
# 편향 - bias
b = tf.Variable(tf.zeros([10]))
# 정답 레이블을 위핚 플레이스 홀더
y_true = tf.placeholder(tf.float32, [None, 10])

#훈련시 정답 예측값
y_pred = tf.nn.softmax(tf.matmul(x,W)+b)

#cross entropy 손실 함수 연산 노드
cross_entropy = -tf.reduce_mean(y_true * tf.log(y_pred))

#경사하강법에 의한 최적화
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# 정답 판별 연산 노드 - 정답 예측 인덱스과 정답 레이블 인덱스 일치 여부 판단 
correct_mask = tf.equal(tf.argmax(y_pred, 1), tf.argmax(y_true, 1))

#정확도 계산 연산 노드
accuracy = tf.reduce_mean(tf.cast(correct_mask, tf.float32))

# 과적합(overfitting)에 대비하는 방법 : 데이터 스킵, 훈련쪼개서 나눠서 하기 
NUM_STEP =1000
MINIBATCH_SIZE =100 


with tf.Session() as sess:
    #학습 위한 변수 초기화
    sess.run(tf.global_variables_initializer())

    #학습
    for _ in range(NUM_STEP): 
        
        batch_xs, batch_ys = data.train.next_batch(MINIBATCH_SIZE)
        sess.run(train_step, feed_dict = {
             x: batch_xs, #data.test.images,      # 훈련 이미지 
             y_true : batch_ys #data.test.labels # 훈련 이미지 정답 레이블 
        })

    #테스트
    ans = sess.run(accuracy, feed_dict ={ 
        x : data.test.images, 
        y_true: data.test.labels 
        })

print("Accuracy : {:.4}%".format(ans * 100))
