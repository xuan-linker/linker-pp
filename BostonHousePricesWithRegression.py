# 导入需要用到的package
import numpy as np
import json


def load_data():
    # 读入训练数据
    datafile = '../work/housing.data'
    data = np.fromfile(datafile, sep=' ')
    print(data)

    # 数据形状变换
    # 读入之后的数据被转化成1维array，其中array的第0-13项是第一条数据，第14-27项是第二条数据，以此类推....
    # 这里对原始数据做reshape，变成N x 14的形式
    feature_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
                     'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']  # 特征数组标签
    feature_num = len(feature_names)
    print("feature_num:{}".format(feature_num))
    print("data:{}".format(data))
    data = data.reshape([data.shape[0] // feature_num, feature_num])  # //取整除 - 返回商的整数部分（向下取整）
    print(data)

    # 查看第一个数据，检查是否符合修改的预期
    firstData = data[0]
    print("firstData:{}".format(firstData))
    print("firstData's shape :{}".format(firstData.shape))  # shape 矩阵长度

    # 数据集划分

    ratio = 0.8  # 数据集比例
    offset = int(data.shape[0] * ratio)  # 测试集数量
    training_data = data[:offset]  # 从左边起始位置开始-offset停止

    print("training_data.shape:{}".format(training_data.shape))

    # 数据归一化
    # 将每个特征进行归一化处理，使得每个特征的取值缩放到0~1之间。
    # 好处：1.模型训练更高效。2.特征前的权重可以代表该变量对预测结果的贡献度

    # 计算train数据集的最大值，最小值，平均值
    maximums, minimus, avgs = \
        training_data.max(axis=0), \
        training_data.min(axis=0), \
        training_data.sum(axis=0) / training_data.shape[0]
    # 对数据进行归一化
    for i in range(feature_num):
        data[:, i] = (data[:, i] - minimus[i]) / (
                maximums[i] - minimus[i])  # data[:, i]表示对一个二维数组，取该二维数组第一维中的所有数据，第二维中取第i个数据
        # print(data[:, i])

    # 训练集和测试集的划分比例
    training_data = data[:offset]
    test_data = data[offset:]
    return training_data, test_data


class Network(object):
    def __init__(self, num_of_weights):
        # 随机产生w的初始值
        # 为了保持程序每次运行结果的一致性，
        # 此处设置固定的随机数种子
        np.random.seed(0)
        self.w = np.random.randn(num_of_weights, 1)
        self.b = 0.

    # 前向计算的过程，从特征和参数到输出预测值的计算过程；线性回归模型的完整输出是z=t+b
    def forward(self, x):
        z = np.dot(x, self.w) + self.b
        return z

    def loss(self, z, y):  # loss 采用均方差
        error = z - y
        cost = error * error
        cos = np.mean(cost)
        return cost


# 获取数据
training_data, test_data = load_data()
x = training_data[:, :-1]
y = training_data[:, -1:]
# 查看数据
print(x[0])
print(y[0])

net = Network(13)
# 此处可以一次性计算多个样本的预测值和损失函数
x1 = x[0:3]
y1 = y[0:3]
z = net.forward(x1)
print('predict: ', z)
loss = net.loss(z, y1)
print('loss:', loss)

