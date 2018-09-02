"""
We have an array A of non-negative integers.

For every (contiguous) subarray B = [A[i], A[i+1], ..., A[j]] (with i <= j), we take the bitwise OR of all the elements in B, obtaining a result A[i] | A[i+1] | ... | A[j].

Return the number of possible results.  (Results that occur more than once are only counted once in the final answer.)

 

Example 1:

Input: [0]
Output: 1
Explanation: 
There is only one possible result: 0.
Example 2:

Input: [1,1,2]
Output: 3
Explanation: 
The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.
Example 3:

Input: [1,2,4]
Output: 6
Explanation: 
The possible results are 1, 2, 3, 4, 6, and 7.


对子数组进行或运算，最后结果是有多少个唯一的解。
思路是DP：
走的弯路：
一开始写的：
[1, 1, 2, 2, 4]
A[0] = {1}
基于A[0]，判断是否在A[0]里，不在的话在添加，在的话就继承A[0]。
A[1] = {1}
A[2] = {1, 2, 3}
A[3] = {1, 2 ,3}
运行到这里都没什么错误，因为就碰巧进行了一次相邻的或运算。
A[4] = {1, 2, 3, 4, 5, 6, 7}
到了这里就有了错误，4不应该与这么多进行或运算。

这里就不知道怎么做了，如果要把上一次的结果也加到里面，怎么才能保证所进行的或运算不包含不相邻的两个点如：
[1, 2, 4]
不会进行 [1,4]的运算。

重新的梳理应该是：
[1]
A[0] = {1}
[   1] [1, 1]
A[1] = {1}
注意，这里与上一个进行或运算，但不把上一个也存到A[2]里面，
[        2] [1, 1, 2] [   1, 2]
A[2] = {2, 3}
基于上一个，但不会将上一个的结果加到本次里影响最终运算。
---
最终输出结果时，进行一次全部的set整理。

测试地址：
https://leetcode.com/contest/weekly-contest-100/problems/bitwise-ors-of-subarrays/

Accepted.


"""
class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0

        dp = [{A[0]}]
        
        for i in range(1, len(A)):
            new = {A[i]}
            for j in dp[i-1]:
                new.add(j|A[i])
            dp.append(new)

        return len(set.union(*dp))

