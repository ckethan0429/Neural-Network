import tensorflow as tf 

class Classifier:

    def __init__(self, num_input, num_output, num_hidden, num_hidden2, lr) :

        self.X, self.Y = self.make_placeholder()
        self.model = self.make_model(self.X, num_input, num_output, num_hidden, num_hidden2) 
        self.prediction = tf.argmax(self.model, axis=1) 
        self.cost, self.train_op = self.make_train_op(self.Y, self.model, lr) 
        self.sess = self.make_session()

    def make_placeholder(self):
        return tf.placeholder(tf.float32), tf.placeholder(tf.float32)

    #모델 : 신경망 설정
    def make_model(self, X, num_input, num_output, num_hidden, num_hidden2):
         W1 = tf.Variable(tf.random_uniform([num_input, num_hidden], -1, 1))
         L1 = tf.nn.relu(tf.matmul(X, W1)) 
         W2 = tf.Variable(tf.random_uniform([num_hidden, num_hidden2], -1, 1))
         L2 = tf.nn.relu(tf.matmul(L1, W2)) 
         W3 = tf.Variable(tf.random_uniform([num_hidden2, num_output], -1, 1)) 
         return tf.matmul(L2, W3)

    def make_train_op(self, Y, model, lr):
        #softmax와 에러함수인 교차엔트로피함수 적용
        cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits_v2( labels=Y, logits=model)) 
        #역전파 설정(경사하강법 말고 Adamoptimizer)
        optimizer = tf.train.AdamOptimizer(lr) 
        train_op = optimizer.minimize(cost) 
        return cost, train_op

    def make_session(self):
        sess = tf.Session() 
        sess.run(tf.global_variables_initializer()) 
        return sess

    #훈련 
    #데이터, 훈련횟수, 중간표현값
    def train(self, data, step_num, prn_num): 
        train_dict = {self.X: data.x_data,self.Y: data.y_data} 

        for step in range(step_num): 
            self.sess.run(self.train_op, feed_dict = train_dict)
            
            if(step+1)%prn_num == 0:
                print(step+1, self.sess.run(self.cost,feed_dict = train_dict))


    # 테스트 
    def test(self, data):
        print("예측값 : ", self.sess.run(self.prediction, feed_dict={self.X : data.x_data}))
        test_dict = {self.X: data.x_data, self.Y: data.y_data} 
        target = tf.argmax(self.Y, axis=1) 

        print("실제값 : ", self.sess.run(target, feed_dict={self.Y : data.y_data})) 
        is_correct = tf.equal(self.prediction, target) 
        accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32)) 
        
        print('정확도 : {:.2f}'.format( self.sess.run(accuracy* 100, feed_dict=test_dict)) )

    # 질의
    def query(self, x_data): 
        return self.sess.run(self.prediction, feed_dict={self.X : x_data}) 
        
    def close(self): 
        self.sess.close()