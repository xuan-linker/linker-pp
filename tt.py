import numpy as np

# 创建数组arr
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print('第1个数组arr：', arr)
# print('向arr数组添加元素：')
# print(np.append(arr, [[9, 10], [11, 12]]))
# print('原数组：', arr)
# print('沿轴 0 添加元素：')
# print(np.append(arr, [[9, 10, 11, 12], [11, 11, 11, 11]], axis=0))
# print('沿轴 1 添加元素：')
# print(np.append(arr, [[9, 10], [11, 12]], axis=1))
circlesDistance = np.zeros((2, 4))
print("circlesDistance:{0}".format(circlesDistance))
i = 0
circlesDistance[i, 0] = 1
print("circlesDistance:{0}".format(circlesDistance))
