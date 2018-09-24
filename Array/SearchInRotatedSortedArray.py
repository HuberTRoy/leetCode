"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

一个排过序的数组被旋转了一下，但不知道在哪个位置旋转的。
给定这样一个数组，并且给定一个目标，找到此数组中是否存在目标。

时间复杂度必须是 O（log n）。

排序过的找某数第一个想法就是 二分法。

这个二分法的关键点在于应该分成两个部分：
1. 递增的部分。
2. 第二个递增的部分。
---
1. 要找的旋转点可以利用 已排序 这个关键词：
由于是已经排过序的所以若是有旋转的 nums[0] 一定是大于所有旋转的元素的。

所以首先的二分是根据以 nums[0] 为 target 找到收个比它小的位置。  
代码在 find_rotate 函数。
因为target是 nums[0] lo 就不管 0 了，直接从1开始。
  lo        hi
4 5 6 7 0 1 2

若 mid 大于 nums[0] 因为是排过序的，而且旋转的情况的话上面也分析过了，不可能有大于 nums[0] 的存在，所以mid左边的不可能存在旋转点。

nums[0] < nums[mid]

lo = mid + 1

否则

hi = mid

这样一轮过后，要么找到旋转点，lo确定后 hi 一直缩小。
             要么无旋转点，lo一直增大。

2. 对于两个递增的部分，分别进行一次普通二分即可。

beat 100%
20ms

测试地址：
https://leetcode.com/problems/search-in-rotated-sorted-array/description/

"""
class Solution(object):
    def find_rotate(self, nums):
        target = nums[0]
        
        lo = 1
    
        hi = len(nums)
        
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target:
                lo = mid + 1
            else:
                hi = mid
        
        return lo
        
    def bi_search(self, nums, target, lo, hi):
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1
        
        return -1      
    
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        rotate_index = self.find_rotate(nums)
        
        lo = 0
        hi = rotate_index
        # print(hi)
        one = self.bi_search(nums, target, lo, hi)
        if one != -1:
            return one
        
        two = self.bi_search(nums, target, hi, len(nums))
        if two != -1:
            return two
        return -1
