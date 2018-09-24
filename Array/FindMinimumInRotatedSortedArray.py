"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

找旋转过的排序数组中最小的数。

有旋转则旋转点最小，无则 0 最小。

beat: 100% 20ms
      48%  24ms

测试地址：
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

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
    
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        rotate = self.find_rotate(nums)
        
        if rotate == len(nums):
            return nums[0]
        
        return nums[rotate]
