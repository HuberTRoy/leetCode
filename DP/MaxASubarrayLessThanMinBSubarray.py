"""
今日头条笔试第四题：
给两个长度为n的数组，a,b。
求有多少个 [l,r]，其中max(a[l:r])<min(b[l:r])。


思路：
DP
3 2 1
3 3 3

Dp1 = [(3), (2), (1)]
    ↓
      [(3), (2, 3), (1)]
    ↓
      [(3), (2, 3), (1, 2, 3)]

Dp2求的是最小。
然后求一下个数。
---
不优化还是挺慢的。

"""
import random

tests = ([
[3, 2, 1],
[3, 3, 3] 
], # 3   2 < 3 1 < 3 (2, 1) < (3, 3)
[
[3, 3, 4 ,5 ,7],
[2, 3, 5, 1, 2]
], # 1   4 < 5
[
[5, 6, 5, 3, 1, 8],
[7, 8, 7, 2, 1, 9]
],  # 7   5 < 7 6 < 8  5 < 7 (5, 6) < (7, 8) (5, 6, 5) < (7, 8, 7), (6, 5) < (8, 7), 8 < 9
[[random.randint(1, 1000000000) for i in range(5000)],
[random.randint(1, 1000000000) for i in range(5000)]]
)


def maxALEminB(a, b):
    dp1 = [[i] for i in a]
    dp2 = [[i] for i in b]

    for i in range(1, len(dp1)):
        value = dp1[i][0]
        for j in dp1[i-1]:
            if j > value:
                dp1[i].append(j)
            else:
                dp1[i].append(value)

    for i in range(1, len(dp2)):
        value = dp2[i][0]
        for j in dp2[i-1]:
            if j < value:
                dp2[i].append(j)
            else:
                dp2[i].append(value)

    result = 0
    for i, j in zip(dp1, dp2):
        for i2, j2 in zip(i, j):
            if i2 < j2:
                result += 1
    return result

# for i in tests:
#     print(maxALEminB(*i))

# 可优化
def maxALEminB(a, b):
    dp1 = [[i] for i in a]
    dp2 = [[i] for i in b]

    result = 0

    for i in range(1, len(dp1)):
        value = dp1[i][0]
        value2 = dp2[i][0]
        if value < value2:
            result += 1

        for j in range(len(dp1[i-1])):
            maxA = dp1[i-1][j] if dp1[i-1][j] > value else value
            minB = dp2[i-1][j] if dp2[i-1][j] < value2 else value2
            if maxA < minB:
                result += 1
            dp1[i].append(maxA)
            dp2[i].append(minB)

    if dp1[0][0] < dp2[0][0]:
        result += 1

    return result

for i in tests:
    print(maxALEminB(*i))

