"""
I
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

II

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


I 比较好理解，找到此前中最小的一个与当前相减，最后取最大的一个即可。

II 有点绕：
1 2 3 这样一个递增段，在 1 买入， 3卖出时是最大的。不过 1 买入，2卖出 2在买入，3卖出 是同样的效果。
如果 1 - 3 中出现一个比 1 小的，那么替换即可，若出现大的用大的减去即可。


I测试地址：
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

II测试地址：
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/



"""
# I
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        mins = prices[0]
        maxes = 0
        
        for i in range(1, len(prices)):
            mins = min(prices[i], mins)
            maxes = max(prices[i]-mins, maxes)
        
        return maxes

# II
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sums = 0
        
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                sums += prices[i+1] - prices[i]
        
        return sums
