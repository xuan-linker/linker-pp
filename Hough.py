import math

import cv2

# 载入并显示图片
import numpy as np

img = cv2.imread('E:/Desktop/test1.jpg')
cv2.imshow('img', img)
# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)

# 输出图像大小，方便根据图像大小调节minRadius和maxRadius
print(img.shape)
# 霍夫变换圆检测
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 35, param1=50, param2=32, minRadius=2, maxRadius=40)
# 输出返回值，方便查看类型
print("circles:{0}".format(circles))
# 输出检测到圆的个数
print("len:{0}".format(len(circles[0])))

print('-------------我是条分割线-----------------')
# 根据检测到圆的信息，画出每一个圆
for circle in circles[0]:
    # 圆的基本信息
    print(circle[2])
    # 坐标行列
    x = int(circle[0])
    y = int(circle[1])
    # 半径
    r = int(circle[2])
    # 在原图用指定颜色标记出圆的位置
    # img = cv2.circle(img, (x, y), r, (0, 0, 255), 3)
    img = cv2.circle(img, (x, y), r, (0, 0, 255), -1)

# 添加每个圆心的相互距离
# circlesDistance = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
# circlesDistance = np.empty((2, 2), dtype=np.float16)
print((circles[0]))
circlesDistance = np.zeros((len(circles[0]) * len(circles[0]), 4), dtype=np.float32)
print("circlesDistance:{0}".format(circlesDistance))

red = (0, 0, 255)
i = 0
tempCircleX = -1
tempCircleY = -1
x1 = 0
y1 = 0
x2 = 99999
y2 = 99999
count = 0
for circle in circles[0]:
    for c in circles[0]:
        print("[[circle[0], circle[1]], [c[0], c[1]]]")
        print("[[x1[0], y1[1]], [x2[0], y2[1]]]")
        print([[circle[0], circle[1]], [c[0], c[1]]])
        print("i:", i)
        circlesDistance[i, 0] = circle[0]
        circlesDistance[i, 1] = circle[1]
        circlesDistance[i, 2] = c[0]
        circlesDistance[i, 3] = c[1]
        i = i + 1
        # cv2.line(img, (int(x1), int(y1)), (int(x2), int(y2)), red, 3)

        # 圆与圆的距离
        length = np.sqrt(np.square(circle[0] - c[0]) + np.square(circle[1] - c[1]))
        print(length)
        # 初始化第一个圆
        if circle[0] == c[0] and circle[1] == c[1]:
            continue
        if count == 0:
            tempCircleX = circle[0]
            tempCircleY = circle[1]
            count = count + 1
            x1 = circle[0]
            y1 = circle[1]
            x2 = c[0]
            y2 = c[1]
            continue
        #     count = count + 1
        # 是否是同一个圆
        if tempCircleX == circle[0] and tempCircleY == circle[1]:
            # 如果是同一个圆则比价距离大小
            length = np.sqrt(np.square(circle[0] - c[0]) + np.square(circle[1] - c[1]))
            tempLength = np.sqrt(np.square(x1 - x2) + np.square(y1 - y2))
            print("length {0} , tempLength {1}".format(length, tempLength))
            count = count + 1
            # 如果距离小
            if math.isnan(tempLength):
                x1 = circle[0]
                y1 = circle[1]
                x2 = c[0]
                y2 = c[1]
            if length < tempLength:
                x1 = circle[0]
                y1 = circle[1]
                x2 = c[0]
                y2 = c[1]
            else:
                continue
        else:
            # 画出length
            minLength = np.sqrt(np.square(x1 - x2) + np.square(y1 - y2))
            minLength = round(minLength, 2)
            midX = (x1 + x2) / 2
            midY = (y1 + y2) / 2
            font = cv2.FONT_HERSHEY_SIMPLEX  # 定义字体
            # cv2.putText(img, 'there 0 error(s):', (midX, midY), cv2.FONT_HERSHEY_COMPLEX, 6, (0, 0, 255), 25)
            cv2.putText(img, str(minLength), (int(midX), int(midY)), font, 0.5, (255, 0, 0), 1)

            # 画出直线
            print((int(x1), int(y1)), (int(x2), int(y2)))
            cv2.line(img, (int(x1), int(y1)), (int(x2), int(y2)), red, 3)
            x1 = circle[0]
            y1 = circle[1]
            x2 = c[0]
            y2 = c[1]
            count = 0

        print((int(x1), int(y1)), (int(x2), int(y2)))

print("res circlesDistance:{0}".format(circlesDistance))
# draw multi-lines
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
print("pts:{0}".format(pts))
# cv2.polylines(img, [pts], True, (0, 0, 255), 3)  # 如果去掉中括号，只是画四个点
# cv2.line(img, [circle[0], circle[1]], [c[0], c[1]], (0, 255, 0))
# 红色颜色
red = (0, 0, 255)
# 画一右对角线，并指定线粗细为 3
# cv2.line(img, (300, 0), (0, 300), red, 3)
# [[x,y,x,y]]
# 显示新图像
cv2.imshow('res', img)

# 按任意键退出
cv2.waitKey(0)
cv2.destroyAllWindows()
