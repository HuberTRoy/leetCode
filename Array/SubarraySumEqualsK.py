"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].


思路：
1. 直接用了暴力的搜索法，TLE。
2. Discuss 里用的哈希 + 保留和的方式。
具体的是：
   pre 一直累加。
   如果 pre - k 存在于保存的字典中，那么结果里加上这个次数即可。

这种方法可行。但暂时没搞明白具体的原理。


测试地址：
https://leetcode.com/problems/subarray-sum-equals-k/description/

"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dicts = {0:1}
        
        result = 0
        
        pre_sum = 0
        
        for i in nums:
            pre_sum += i
            
            result += dicts.get(pre_sum-k, 0)
            
            dicts[pre_sum] = dicts.get(pre_sum, 0) + 1

        return result
        