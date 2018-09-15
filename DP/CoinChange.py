"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

思路是DP:

1. 一次失败的尝试：
子问题定位 当前钱数需要的最少硬币量。
代码写的有点问题，导致运行异常缓慢。

外层循环是 1-amount ，逐个点去寻找。
内层循环则一遍遍重复与已经解出来的点进行对比，这样做包含了很多无用的信息。

2. 经过思考后，发现问题所在，

[1, 2, 5] 11

7这个点，所需要的不是从 1-6 都进行一遍判断后取最小值。
只需要2,5,6这三个点就可以。
具体是 7-5,7-2,7-1。

---
这样就是一个经典的DP算法。这个算法可以通过，但有时也会 TLE...

---
二次优化:
外层循环大可不必 1 - amount，可以 min(coins) - amount。
这样可以提高一些效率。

---
三次尝试：
可以把外层循环与内层循环调换。这样的效率同样是 O(n*amount)。


测试地址：
https://leetcode.com/problems/coin-change/description/

beat 33%...

"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = {0: 0}
        mins = min(coins)
        inf = float('inf')
        for i in range(mins, amount+1):
            dp[i] = min((dp.get(i-j, inf)+1 for j in coins))
        
        # for i in coins:
        #     for j in range(i, amount+1):
        #         dp[j] = min(dp.get(j, inf), dp.get(j-i, inf)+1)

        # for i in range(mins, amount+1):
            # dp[i] = min((dp.get(i-j, inf)+1 for j in coins))
            # temp = []
            # for j in coins:
            #     temp.append(dp.get(i-j, inf)+1)
            # dp[i] = min(temp)

        if dp.get(amount) == inf:
            return -1
        return dp.get(amount, -1)

        # coins = set(coins)
        # dp = [(0, 0)]
        # for i in range(1, amount+1):
            # temp = []
            # for j in range(len(dp)-1, -1, -1):
            #     j = dp[j]
            #     if i - j[1] in coins:
            #         temp.append((j[0]+1, i))
            # if temp:
                # dp.append(min(temp, key=lambda x: x[0]))
        # print(dp)
        # if dp[-1][1] == amount:
            # return dp[-1][0]
        
        # return -1

a = Solution()

# print(a.coinChange([70, 71], 142))
print(a.coinChange([70,177,394,428,427,437,176,145,83,370], 7582))