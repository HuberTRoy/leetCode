"""
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

 

Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
 

Note:

-30000 <= A[i] <= 30000
1 <= A.length <= 30000

给一个前后连通的数组，求里面和最大的子数组。

不连通的之前已经做过了，每个点的状态有两个，一个是加上之前的 > 0，一个是加上之前的小于 0，此点保存的值为 加上与不加较大的一个。

连通的话呢...一开始致力于用O(n)就找出可以开始的点...走了些弯路：
1. 尝试从 0 开始找第一个非负，没有覆盖全部情况。比如这样 8 -1 -3 8 -5 -5 -5 8.
2. 尝试把点设在从后向前的负数的前面的最大正数。 比如 8 -1 -3 8 -5 -5 -5 8，就选 8 -1 -3 8 -5 -5 -5，这样可以过90%.. 出错的情况忘了记录。
3. 看样子只能 o(n²)。

结束后看 Discuss 里的讨论，大神就是大神... 首尾相连的情况其实就是 sum(A) - sum(min A[subarray])。

ok... 掌握这条信息后直接就可以做出来了，找最小的情况与最大也没什么区别。

284ms

测试地址：
https://leetcode.com/contest/weekly-contest-105/problems/maximum-sum-circular-subarray/

"""
class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        dp = [A[0]]
        maxes = A[0]
        
        for i in range(1, len(A)):
            if A[i] + dp[i-1] > 0:
                maxes = max(maxes, A[i]+dp[i-1], A[i])
                dp.append(max(A[i]+dp[i-1], A[i]))
            else:
                dp.append(A[i])
                maxes = max(maxes, A[i])
        
        if maxes < 0:
            return maxes
        
        dp = [A[0]]
        
        mines = A[0]
        
        for i in range(1, len(A)):
            if A[i] + dp[-1] < 0:
                mines = min(mines, A[i]+dp[-1], A[i])
                dp.append(min(A[i]+dp[-1], A[i]))
            else:
                dp.append(A[i])
                mines = min(mines, A[i])
        
        
        maxes = max(maxes, sum(A) - mines)

        return maxes
