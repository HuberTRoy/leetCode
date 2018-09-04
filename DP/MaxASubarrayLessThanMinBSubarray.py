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

tests = (
# [
# [3, 2, 1],
# [3, 3, 3] 
# ], # 3   2 < 3 1 < 3 (2, 1) < (3, 3)
# [
# [3, 3, 4 ,5 ,7],
# [2, 3, 5, 1, 2]
# ], # 1   4 < 5
[
[5, 6, 5, 3, 1, 8, 1, 1, 3, 5],
[7, 8, 7, 2, 1, 9, 5, 7, 8, 1]
],  # 7   5 < 7 6 < 8  5 < 7 (5, 6) < (7, 8) (5, 6, 5) < (7, 8, 7), (6, 5) < (8, 7), 8 < 9
[[random.randint(1, 1000000000) for i in range(100000)],
[random.randint(1, 1000000000) for i in range(100000)]]
)


# def maxALEminB(a, b):
#     dp1 = [[i] for i in a]
#     dp2 = [[i] for i in b]

#     for i in range(1, len(dp1)):
#         value = dp1[i][0]
#         for j in dp1[i-1]:
#             if j > value:
#                 dp1[i].append(j)
#             else:
#                 dp1[i].append(value)

#     for i in range(1, len(dp2)):
#         value = dp2[i][0]
#         for j in dp2[i-1]:
#             if j < value:
#                 dp2[i].append(j)
#             else:
#                 dp2[i].append(value)

#     result = 0
#     for i, j in zip(dp1, dp2):
#         for i2, j2 in zip(i, j):
#             if i2 < j2:
#                 result += 1
    
#     print(dp1)
#     print(dp2)
#     return result

# for i in tests:
#     print(maxALEminB(*i))


# 优化版
# 1e5 个随机数由原来的无结果变为 2.5s 可解。
# 在无重复的数据时时间复杂度会退化为 O(N²).
# 

def maxALEminB(a, b):
    """
        思路与前一致，前一版的主要瓶颈在于有太多重复的数据，若可以将这些重复的数据统计到一起，可以极大的减少对比次数。
        [[3], [2], [1]]
        现在变为 
        [[(3, 1)], [(2, 1)], [(1, 1)]]
        即缩小重复的数据的检测结果。
        例：
        [5, 6, 5, 3, 1, 8, 1, 1, 3, 5],
        [[5], [6, 6], [5, 6, 6], [3, 5, 6, 6], [1, 3, 5, 6, 6], [8, 8, 8, 8, 8, 8], ...]
        dp1的检测为，若当前的值大于之前中的值的某一个[-1:0]，从前到后是按升序排列的。
                    就从最初出现的那个地方截断，之前的值全部替换为此最大值，若没有一个大于的，则直接将之前的追加到当前的结果中。
        dp2的检测只将 大于 变为 小于。

        关于对比：
            每一组的个数可能不同，但总量是一致的。
            两组同时取出自己的一个数据，若b > a则结果中加上 b 和 a 中出现的次数较少的一个。并减去，开始下一轮，b或a中任意一个的出现次数为0时，
            取出相应的本组的下一个数据，同时为0时开始下一轮循环。
    """
    dp1 = [[[i, 1]] for i in a]
    dp2 = [[[i, 1]] for i in b]

    # [
    #  [
    #   [i, 1]
    #  ]
    # ]
    for i in range(1, len(dp1)):
        value = dp1[i][0]
        j = dp1[i-1]

        # 二次优化后提高了 0.2 s.
        if j[0][0] > value[0]:
            dp1[i].extend(j)
            continue

        for x in range(len(j)-1, -1, -1):
            x2 = j[x]
            if x2[0] <= value[0]:
                dp1[i] = [[value[0], sum([t[1] for t in j[:x+1]])+1]] + j[x+1:]
                break

    for i in range(1, len(dp2)):
        value = dp2[i][0]
        j = dp2[i-1]
        if j[0][0] <= value[0]:
            dp2[i].extend(j)
            continue

        for x in range(len(j)-1, -1, -1):
            x2 = j[x]
            if x2[0] >= value[0]:
                dp2[i] = [[value[0], sum([t[1] for t in j[:x+1]])+1]] + j[x+1:]
                break

    result = 0
    for i, j in zip(dp1, dp2):
        valueA = 0
        valueB = 0
        while 1:
            if not i and not j:
                break

            if valueA == 0:
                a = i.pop()
                valueA = a[1]
            if valueB == 0:
                b = j.pop()
                valueB = b[1]

            minx = min(valueA, valueB)

            if b[0] > a[0]:
                result += minx

            valueA -= minx
            valueB -= minx

    return result


# 可优化
# def maxALEminB(a, b):
#     dp1 = [[i] for i in a]
#     dp2 = [[i] for i in b]

#     result = 0

#     for i in range(1, len(dp1)):
#         value = dp1[i][0]
#         value2 = dp2[i][0]
#         if value < value2:
#             result += 1

#         for j in range(len(dp1[i-1])):
#             maxA = dp1[i-1][j] if dp1[i-1][j] > value else value
#             minB = dp2[i-1][j] if dp2[i-1][j] < value2 else value2
#             if maxA < minB:
#                 result += 1
#             dp1[i].append(maxA)
#             dp2[i].append(minB)

#     if dp1[0][0] < dp2[0][0]:
#         result += 1

#     return result

for i in tests:
    print(maxALEminB(*i))

