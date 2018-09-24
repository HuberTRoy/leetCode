"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

search in rotated sorted array 变形版本：

与之前的区别是有重复，重复的值会造成什么样的影响呢？

1, 1, 1, 1, 1, 1, 2, 1, 1

在这个例子中

旋转的点是 1, 如果再用之前的方法，nums[0] 是没办法保证比旋转的点之后的元素都大的，
循环之后的mid是1，不大于nums[0] 不大于 mid 的情况中会把hi变为mid这样就会造成之后的数据丢失。
其他的情况可以与 I 一样。

我想到的解决方法：
1. 可以把与 nums[0] 相同的一直吞并。 这里用的方法是一直迭代。

总时间复杂度的话最差会有 O(n + log n)。

测试地址：
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

beat 89% 24ms

平均24 - 28 ms。

"""
class Solution(object):
    def find_rotate(self, nums):
        target = nums[0]
        lo = 1

        for i in range(1, len(nums)):
            if nums[i] == target:
                lo += 1
            else:
                break
    
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
            return False
        
        rotate_index = self.find_rotate(nums)
        
        lo = 0
        hi = rotate_index

        one = self.bi_search(nums, target, lo, hi)
        if one != -1:
            return True
        
        two = self.bi_search(nums, target, hi, len(nums))
        if two != -1:
            return True
        return False
