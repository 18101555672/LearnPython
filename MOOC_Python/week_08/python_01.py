# 实例：体育竞技分析
# 步骤一：打印程序的介绍性信息 —printInfo()
# 步骤二：获得程序运行参数：proA，proB，n —getInputs()
# 步骤三：利用球员A和球员B的能力值，模拟n局比赛 —simNGames(),simOneGame(),gameOver()
# 步骤四：输出球员A和球员B获胜比赛的场次及概率 —printSummary()
import random
def printInfo():
    print('这个程序模拟两个选手A和B的某种竞技比赛')
    print('程序运行需要A和B的能力值（以0到1之间的小数表示）')

def getInputs():
    a = eval(input('请输入选手A的能力值：'))
    b = eval(input('请输入选手B的能力值：'))
    n = eval(input('模拟比赛的场次：'))
    return a,b,n

def gameOver(a,b):
    return a == 15 or b == 15

def simOneGame(probA,probB):
    scoreA,scoreB = 0,0
    serving = 'A'
    while not gameOver(scoreA,scoreB):
        if serving == 'A':
            if random.random() < probA:
                scoreA += 1
            else:
                serving = 'B'
        else:
            if random.random() < probB:
                scoreB +=1
            else:
                serving = 'A'
    return scoreA,scoreB

def simNGames(n,proA,proB):
    winsA,winsB = 0,0
    for i in range(n):
        scoreA,scoreB = simOneGame(proA,proB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA,winsB

def printSummary(winsA,winsB):
    n = winsA + winsB
    print('竞技分析开始，共模拟{}场比赛'.format(n))
    print('选手A获胜{}场比赛，胜率为{:.2f}%'.format(winsA,winsA/n*100))
    print('选手B获胜{}场比赛，胜率为{:.2f}%'.format(winsB,winsB/n*100))

def main():
    printInfo()
    probA,probB,n = getInputs()
    winsA,winsB = simNGames(n,probB,probA)
    printSummary(winsA,winsB)

if __name__ == '__main__':
    main()













