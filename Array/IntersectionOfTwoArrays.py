"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.


找两个数组里的重复数据。

唯一，任意顺序。

集合，取交集即可。

零启动。

beat 100% 20ms.

测试地址：
https://leetcode.com/problems/intersection-of-two-arrays/description/

"""
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        return list(set(nums1) & set(nums2))
