import random
# 生成一组牌（五十二张）
cards = []
for i in ['K','Q','J',10,9,8,7,6,5,4,3,2,'A']:
    for l in range(1,5):
        cards.append(str(i)+'_'+str(l))
# 随机获取五张牌
def getCard():
    card = []
    for i in range(5):
        n = random.choice(cards)
        card.append(n)
        cards.remove(n)
    print('随机的五张牌为',card)
    return card
# 将获取的五张牌转换成相应数值
def transformNum(card):
    num = []
    for i in card:
        if i[0:-2] in ['K','Q','J']:
            num.append(10)
        elif i[0:-2] == 'A':
            num.append(1)
        else:
            num.append(int(i[0:-2]))
    print(num)
    return num
# 计算牛
def getBossy(num):
    n = 0
    while n != 60:
        for a in range(5):
            for b in range(5):
                if b == a:
                    continue
                else:
                    for c in range(5):
                        if c == b or c == a:
                            continue
                        else:
                            n += 1
                            sum = num[a] + num[b] + num[c]
                            if sum % 10 == 0:
                                s = 0
                                for i in num:
                                    s += i
                                bossy = s - sum
                                if bossy % 10 == 0:
                                    if s == 50:
                                        print('五花牛！')
                                        return '五花牛！'
                                    else:
                                        print('牛牛！')
                                        return '牛牛！'
                                else:
                                    print('牛{}'.format(str(bossy)[-1]))
                                    return '牛{}'.format(str(bossy)[-1])
    print('没牛')
    return '没牛'

getBossy(transformNum(getCard()))
getBossy([10,10,10,10,10])
getBossy([10,2,10,3,5])
getBossy([10,2,10,3,10])
getBossy([10,2,10,3,3])


