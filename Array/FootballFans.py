"""
好像是今日头条2018 秋招算法题？

球场C 可容纳 M*N个球迷。统计有几组球迷群体：

1. 每组球迷群体会选择相邻的作为（8个方位。）
2. 不同球迷群体不会相邻。
3. 给一个 M*N 的二维球场，0为没人，1为有人，求出群体个数P以及最大的群体人数Q.

OK, bug free.

类似算法的 leetcode：
https://leetcode.com/problems/number-of-islands/description/  解答请看 NumberOfIslands.py
https://leetcode.com/problems/max-area-of-island/description/ 解答请看 MaxAreaOfIsland.py

"""

test = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
[0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
]

# 6 8

def makeAroundXY(x, y):
    # ((x, y)....)
    return ((x, y-1),
            (x, y+1),
            (x-1, y),
            (x+1, y),
            (x-1, y-1),
            (x-1, y+1),
            (x+1, y+1),
            (x+1, y-1))

def getFootballFans(court):
    """
        [[0, 0, 0].....]
        从 0,0 开始，如果遇到1则进入递归：
        递归结束条件：
            四周都是 0或边界。
            结束时将搜索到的人数添加。
        未结束时根据四周的情况进入相同的递归。
    """

    fans_groups = []
    x = 0
    y = 0

    x_length = len(court[0])
    y_length = len(court)

    def helper(x, y, result=0):
        nonlocal court
        Xy = makeAroundXY(x, y)
        for i in Xy:
            try:
                if i[0] < 0 or i[1] < 0:
                    continue

                if court[i[1]][i[0]] == 1:
                    court[i[1]][i[0]] = 0
                    result += 1
                    t = helper(i[0], i[1], 0)
                    result += t
            except IndexError:
                continue
        else:
            return result


    for y in range(y_length):
        for x in range(x_length):
            if court[y][x] == 1:
                court[y][x] = 0
                fans_groups.append(helper(x, y, 1))



    if not fans_groups:
        return (0, 0)

    return (len(fans_groups, max(fans_groups)))

getFootballFans(test)