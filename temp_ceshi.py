# -*- coding: utf-8 -*-
import json

def load_data(file_read):
    rf = open(file_read, 'r', encoding='utf8')
    k = 0
    kk = []
    for line in rf:
        k += 1
        line = line.strip()
        data_dict = json.loads(line)

        kk.append(len(data_dict["conversation"]))
    b = {}
    for i in kk:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    print(b)
    rf.close()


def load_data1(file_read):
    rf = open(file_read, 'r', encoding='utf8')
    k = 0
    for line in rf:
        k += 1
        line = line.strip()
        data_dict = json.loads(line)
        for sen in data_dict["goal"]:
            print(sen)
        print()
        for sen in data_dict["conversation"]:
            print(sen)
        input("--")
    rf.close()


def load_data2(file_read):
    rf = open(file_read, 'r', encoding='utf8')
    k = 0
    for line in rf:
        k += 1
        line = line.strip()
        data_dict = json.loads(line)
        if len(data_dict["goal"][0]) != 3:
            print(len(data_dict["goal"][0]))
    rf.close()


root_dir = "C:/Users/25363/Downloads/新建文件夹/Compressed/Dialogue-Retrieval/知识驱动对话数据/data/"
file_read = root_dir + "dev.txt"
load_data2(file_read)

# train 19858  goal(2,3)  knowledge（平均 14.1584）    conversation(两个15，其余全是偶数，平均 9.0542)
# goal  {2: 11720, 3: 8138}
# knowledge  {8: 1, 9: 30, 10: 213, 11: 873, 12: 2031, 13: 3662, 14: 4854, 15: 4279, 16: 2314, 17: 1069, 18: 352, 19: 120, 20: 47, 21: 11, 22: 1, 23: 1}
# conversation  {16: 33, 18: 4, 8: 11698, 10: 6262, 12: 1530, 14: 329, 15: 2}

# dev   2000   goal(2,3)  knowledge（平均 14.2075）    conversation（全部为偶数，平均 9.054 ）
# goal {2: 1210, 3: 790}
# knowledge {9: 9, 10: 25, 11: 79, 12: 210, 13: 351, 14: 466, 15: 424, 16: 252, 17: 121, 18: 45, 19: 13, 20: 3, 21: 2}
# conversation  {16: 4, 18: 1, 8: 1181, 10: 632, 12: 145, 14: 37}

# test  5000   goal(2,3)  knowledge(平均 14.1952)      history（全是偶数，920个为零, 最大14，最小0）
# goal {2: 3033, 3: 1967}
# knowledge {8: 1, 9: 5, 10: 48, 11: 227, 12: 459, 13: 910, 14: 1223, 15: 1174, 16: 550, 17: 257, 18: 106, 19: 22, 20: 5, 21: 8, 22: 2, 23: 3}
# history 分布 {0: 920, 2: 1176, 4: 1157, 6: 1140, 8: 478, 10: 105, 12: 21, 14: 3}
