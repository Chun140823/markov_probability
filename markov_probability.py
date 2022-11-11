from typing import List

import numpy as np

weather_chance = {"晴天": ["晴天", "晴天", "晴天", "晴天", "晴天", "多云", "多云", "多云", "多云", "雨天"],
                  "雨天": ["雨天", "雨天", "雨天", "雨天", "雨天", "雨天", "多云", "多云", "多云", "晴天"],
                  "多云": ["雨天", "雨天", "雨天", "雨天", "雨天", "晴天", "晴天", "晴天", "晴天", "多云"]
                  }

sunny = weather_chance.get("晴天")
rainy = weather_chance.get("雨天")
cloudy = weather_chance.get("多云")

p11 = cloudy.count("多云") / len(cloudy)
p12 = cloudy.count("雨天") / len(cloudy)
p13 = cloudy.count("晴天") / len(cloudy)
p21 = rainy.count("多云") / len(rainy)
p22 = rainy.count("雨天") / len(rainy)
p23 = rainy.count("晴天") / len(rainy)
p31 = sunny.count("多云") / len(sunny)
p32 = sunny.count("雨天") / len(sunny)
p33 = sunny.count("晴天") / len(sunny)

probability_transfer = [[p11, p12, p13], [p21, p22, p23], [p31, p32, p33]]
print(probability_transfer)

P1 = np.array(probability_transfer)  # 第一天
P2 = np.dot(P1, P1)  # 第二天
P3 = np.dot(P2, P1)  # 第三天
P4 = np.dot(P3, P1)  # 第四天
P5 = np.dot(P4, P1)  # 第五天
P6 = np.dot(P5, P1)  # 第六天

while True:

    print("请输入当前的天气情况: ")
    print("1. 如果是\"多云\", 请输入\"1\"")
    print("2. 如果是\"雨天\", 请输入\"2\"")
    print("3. 如果是\"晴天\", 请输入\"3\"")

    inp = input("请输入: ")

    i = (P1, P2, P3, P4, P5, P6)

    if inp == str(1):
        for j in range(1, 7):
            for index, value in enumerate(i):
                if j - 1 == index:
                    print("在 " + str(j) + " 天后可能是多云的概率是：" + str(value[0, 0]))
                    print("在 " + str(j) + " 天后可能是雨天的概率是：" + str(value[0, 1]))
                    print("在 " + str(j) + " 天后可能是晴天的概率是：" + str(value[0, 2]))
        break

    elif inp == str(2):
        for j in range(1, 7):
            for index, value in enumerate(i):
                if j - 1 == index:
                    print("在 " + str(j) + " 天后可能是多云的概率是：" + str(value[1, 0]))
                    print("在 " + str(j) + " 天后可能是雨天的概率是：" + str(value[1, 1]))
                    print("在 " + str(j) + " 天后可能是晴天的概率是：" + str(value[1, 2]))
        break

    elif inp == str(3):
        for j in range(1, 7):
            for index, value in enumerate(i):
                if j - 1 == index:
                    print("在 " + str(j) + " 天后可能是多云的概率是：" + str(value[2, 0]))
                    print("在 " + str(j) + " 天后可能是雨天的概率是：" + str(value[2, 1]))
                    print("在 " + str(j) + " 天后可能是晴天的概率是：" + str(value[2, 2]))
        break

    else:
        continue
