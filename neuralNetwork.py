import numpy as numpy
from scipy.special import expit


class neuralNetwork:
    # 신경망 초기화하기
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate, path = None):
        # 입력, 은닉, 출력 계층의 노드 개수 설정
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        # 학습률
        self.lr = learningrate

        # 가중치 행렬 wih와 who
        # 배열 내 가중치는 w_i_j로 표기 (약식으로 wij)
        # 노드 i에서 다음 계층의 노드 j로 연결됨을 의미
        # w11 w21
        # w12 w22 등
        self.wih = numpy.random.normal(
            0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(
            0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))

        # 활성화 함수로 시그모이드 함수 설정
        self.activation_function = lambda x: expit(x)

    # 신경망 학습시키기
    def train(self, inputs_list, targets_list):
        # 입려 리스트를 2차원의 행렬로 변환
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        # 은닉 계층으로 들어오는 신호를 계산
        hidden_inputs = numpy.dot(self.wih, inputs)
        # 은닉 계층에서 나가는 신호를 계산
        hidden_outputs = self.activation_function(hidden_inputs)

        # 최종 출력 계층으로 들어오는 신호를 계산
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # 최종 출력 계층에서 나가는 신호를 계산
        final_outputs = self.activation_function(final_inputs)

        # 2단계 가중치 업데이트
        # 출력 계층의 오차(실제 값 - 계산 값)
        output_errors = targets - final_outputs
        # 은닉 계층의 오차는 가중치 값의 비례로 재조정
        hidden_errors = numpy.dot(self.who.T, output_errors)

        # 은닉 계층과 출력 계층간의 가중치 업데이트
        self.who += self.lr*numpy.dot((output_errors*final_outputs*(1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        # 입력 계층과 은닉 계층간의 가중치 업데이트
        self.wih += self.lr*numpy.dot((hidden_errors*hidden_outputs*(1.0 - hidden_outputs)), numpy.transpose(inputs))

    def query(self, inputs_list):
        # 입력 리스트를 2차원 행렬로 변환
        inputs = numpy.array(inputs_list, ndmin=2).T

        # 은닉 계층으로 들어오는 신호를 계산
        hidden_inputs = numpy.dot(self.wih, inputs)
        # 은닉 계층에서 나가는 신호를 계산
        hidden_outputs = self.activation_function(hidden_inputs)

        # 최종 출력 계층으로 들어오는 신호를 계산
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # 최종 출력 계층에서 나가는 신호를 계산
        final_outputs = self.activation_function(final_inputs)

        return final_outputs


if __name__ == "__main__":
    # 입력, 은닉, 출력 노의 수
    input_nodes = 3
    hidden_nodes = 3
    output_nodes = 3
    # 학습률 0.3 정의
    learning_rate = 0.3
    # 신경망의 인스턴스 생성
    ne = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

    print("n.query = ", ne.query([1.0, 0.5, -1.5]))
