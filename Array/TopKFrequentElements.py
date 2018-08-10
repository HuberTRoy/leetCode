"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

思路：
首先是计算出每个数字出现的频率，之后排序频率，输出最高的k位。

字典（哈希表），sorted（排序）。

beat 88%

测试用例：
https://leetcode.com/problems/top-k-frequent-elements/description/

"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        nums_dict = {}
        
        for i in nums:
            try:
                nums_dict[i] += 1
            except KeyError:
                nums_dict[i] = 1
        
        return sorted(nums_dict, key=lambda x: nums_dict[x], reverse=True)[:k]
