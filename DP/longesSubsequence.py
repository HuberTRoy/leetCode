"""
整体思路是使用 DP。
DP 的核心是找到子问题。
该问题的子问题当前从此点向前与哪些组合可以形成最长的子串。
但与初级的抛硬币不同（要判断的只有3个），判断的点为从此点向前的所有点（子问题）。
时间复杂度 O(n**2)。
测试用例：
https://leetcode.com/problems/longest-increasing-subsequence/description/

另：有一个 O(nlogn) 的算法，暂未研究。

"""

"""
牛刀小试，DP 抛硬币，1 3 5 最少凑11。
def coins(num):

    coins_result = {'0': 0}
    for i in range(1, num+1):
        coins_5, coins_3, coins_1 = float('inf'), float('inf'), float('inf') 
        if i-5 >= 0:
            coins_5 = coins_result[str(i-5)] + 1
        if i-3 >= 0:
            coins_3 = coins_result[str(i-3)] + 1
        if i-1 >= 0:
            coins_1 = coins_result[str(i-1)] + 1

        coins_result[str(i)] = min([coins_5, coins_3, coins_1])
    print(coins_result)
    print(coins_result[str(num)])

# coins(100)
"""

class Solution(object):
    def lengthOfLIS(self, strings):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not strings:
            return 0
        long_ss = []

        for i in strings:
            if not long_ss:
                long_ss.append(([i], 1))
                continue
            maxs = max(long_ss, key=lambda x: x[0][-1] < i and x[1]+1)
            if maxs[0][-1] >= i:
                long_ss.append(([i], 1))
            else:
                long_ss.append((maxs[0]+[i], maxs[1]+1))

        return max(long_ss, key=lambda x: x[1])[1]