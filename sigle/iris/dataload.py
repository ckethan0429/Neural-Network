import tensorflow as tf 
import numpy as np



class Obj:
    def __init__(self):
      pass

def one_hot(y_data):
    #2차원 -> 1차원(index니까 정수로 형변환 후)
    index = y_data.astype('uint8').flatten() #1차원
    
    #y_data.shape
    rows = y_data.shape[0]
    cols = index.max() +1
    
    temp = np.zeros((rows,cols), dtype = 'float32')
    #temp = np.zeros((y_data.shape[0],3), dtype = 'float32') 
    temp[np.arange(rows),index] =1.0
    #temp[np.arange(y_data.shape[0]),index] = 1.0 #값 입력
    return temp

def load_data(file_path, num_feature, train_rate):
    data = np.loadtxt(file_path ,delimiter = ',',dtype = 'float32')

    total = data.shape[0]
    base = int(total * train_rate)

    np.random.shuffle(data)
    train_data = data[:base]
    test_data = data[base:]

    train = Obj()
    test = Obj()

    train.x_data = train_data[:,1:num_feature+1]
    train.y_data = one_hot(train_data[:,:1])

    test.x_data = test_data[:,1:num_feature+1]
    test.y_data = one_hot(test_data[:,:1])

    return train, test

if __name__ == "__main__":
    train_data, test_data = load_data('./iris_150(int).csv',4,0.6)
    print(train_data.x_data)
    print(train_data.y_data)
    print(test_data.x_data)
    print(test_data.y_data)
