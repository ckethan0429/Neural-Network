def load(self, path):
    #데이터 읽기
    data_frame = pd.read_csv(path, header=None) #pandas import 필요
    values = data_frame
    labels = values[:, 0:1]
    data = values[:,1:]/255.0*0.99+0.01
    return labels, data

def train_from(self, path):
    for label, inputs in zip(*self.load(path)):
        targets = np.zeros(self.onodes)+ 0.01 #numpy import 필요
        targets[label] = 0.99
        self.train(inputs, targets)


def query_from(self, path):
    scorecard = []
    for label, inputs in zip(*self.load(path)):
        outputs = self.query(inputs)
        answer = np.argmax(outputs)
        if(label == answer) :
            scorecard.append(1)
        else:
            scorecard.append(0)

    scorecard_array = np.asarray (scorecard)
    return scorecard_array.sum()/scorecard_array.size


# 신경망의 인스턴스 생성
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes,learning_rate)

#가중치 저장
n.train_from_file("mnist_dataset/mnitst_trans_100.csv")
n.save_weight("./minist")



# 신경망의 인스턴스 생성
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes,learning_rate, "./mnist")
performance = n.query_from_file(("mnist_dataset/mnitst_test_10.csv")

print("performance : ",performance)