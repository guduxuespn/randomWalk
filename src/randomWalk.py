import matplotlib.pyplot as plt
import random
from random import choice


class RandomWalk():

    
    def __init__(self, loop=5000):
        # 设置循环次数
        self.loop = loop
        # 设置起始位置坐标
        self.x = [50]
        self.y = [0]


    def get_random_walk_x(self):
        '''这个函数将生成用于绘制数据的x轴的列表'''

        # 设置循环次数
        # loop = 10000

        for i in range(1, self.loop):
            # 从规定的序列中随机取的方向
            direction = choice([-1, 1])
            # 从规定的序列中随机取的步长
            distance = choice([0, 1, 2, 3, 4, 5, 6])

            # 分别计算下一步的步长
            next_x = direction * distance

            # 分别计算下一步的坐标
            self.x.append(self.x[len(self.x) - 1] + next_x)

        return self.x


    def get_random_walk_y(self):
        '''这个函数将生成用于绘制数据的y轴的列表'''

        # # 设置循环次数
        # loop = 10000

        # # 设置起始位置坐标
        # x = [50]
        # y = [30]

        for i in range(1, self.loop):
            # 从规定的序列中随机取的方向
            direction = choice([-1, 1])

            # 从规定的序列中随机取的步长
            distance = choice([0, 1, 2, 3, 4, 5, 6])

            # 分别计算下一步的步长
            next_y = direction * distance

            # 分别计算下一步的坐标
            self.y.append(self.y[len(self.y) - 1] + next_y)

        return self.y

    # print(len(get_random_walk_x()), len(get_random_walk_y()))

    def show_date(self, a, b):
        '''将获得的数据绘制出来'''
        plt.scatter(a, b, s=10, cmap=plt.cm.Blues, edgecolors=None)
        plt.show()
