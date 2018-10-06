"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


给定一个阶梯数，每次可以上一步，也可以上两步，输出有爬到顶有几种方式。

和 decode ways 非常相似的思路，刚解出 decode ways...这个相当于买一赠一了。

思路：
 只有一层时，只有一种方式，一步。
 只有两层是，有两种方式，一步一步，两步。
 有三层时，有三种方式，一步一步一步，一步两步，两步一步。
 ...

 3 层时的子问题来自于 2层时的子问题与1层时的子问题。

beat 97%

测试地址：
https://leetcode.com/problems/climbing-stairs/description/
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 1:
            return 0
        
        if n == 1:
            return 1
        
        dp = []
        dp.append(1)
        dp.append(2)
        
        for i in range(2, n):
            dp.append(dp[i-1]+dp[i-2])
        return dp[-1]
        