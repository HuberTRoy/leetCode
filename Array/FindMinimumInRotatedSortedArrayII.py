"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?

与Search in Rotated Sorted Array II 中讨论的一样，主要就是重复的数。用同样的方法即可。

解释请看 SearchInRotatedSortedArrayII.py.

beat 100% 20ms~24ms都有可能。

测试地址：
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/

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
    
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        rotate = self.find_rotate(nums)
        
        if rotate == len(nums):
            return nums[0]
        
        return nums[rotate]
        