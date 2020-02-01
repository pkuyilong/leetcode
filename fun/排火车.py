import random
import time

# 0代表大王和小王
# pokers = [list(range(1, 14)) for i in range(4)] + [0, 0]
pokers = []
for i in range(4):
    pokers += list(range(1, 14))
pokers += [0, 0]
# print(pokers)


idx_poker = {}
for i in range(14):
    if i == 0:
        idx_poker[i] = "Jocker"
    elif i < 11:
        idx_poker[i] = str(i)
    elif i == 11:
        idx_poker[i] = "J"
    elif i == 11:
        idx_poker[i] = "J"
    elif i == 12:
        idx_poker[i] = "Q"
    elif i == 13:
        idx_poker[i] = "K"


def deal():
    random.shuffle(pokers)
    print("洗牌 {}".format(pokers))
    return pokers


def start():
    pokers = deal()
    poker_pos_dict = {}
    poker_queue = []
    for idx, poker in enumerate(pokers):
        print("火车 {}".format([idx_poker[item] for item in poker_queue]))
        time.sleep(1)
        print("新牌 {}".format(idx_poker[poker]))
        time.sleep(1)
        # print("第 {} 张扑克牌是 {}".format(idx, poker))
        if len(poker_queue) == 0:
            poker_queue.append(poker)
            poker_pos_dict[poker] = 0
        else:
            # 如果有相同的牌在其中
            if poker in poker_pos_dict.keys():
                # 清理队列
                start_pos = poker_pos_dict[poker]
                poker_list = poker_queue[start_pos:] + [poker]
                print("\n####出现重复#### {} \n".format([idx_poker[item] for item in poker_list]))
                for _ in range(len(poker_queue) - start_pos):
                    removed_poker = poker_queue.pop()
                    poker_pos_dict.pop(removed_poker)

            else:
                # 更新字典
                poker_pos_dict[poker] = len(poker_queue)
                poker_queue.append(poker)


if __name__ == '__main__':
    start()
