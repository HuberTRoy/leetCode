"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

数组中两个数相加，得到目标。

排序后的数组查找最快的就是二分法了。
基本思路：
排序，
二分查找。

用目标逐个相减然后查找是否存在（其实可以顺便返回位置，这样就不用index了。）。

所以时间复杂度 O(nlogn)

改进：
有O(n) 方式。

2018/8/17：
O(n) 方式总结：

在有序状态下，从后向前是逐渐缩小，从前向后逐渐增大。
[-4, -1, 0, 1, 2]
 0             4

当 start + end < target 时，end已经不能在增大了，只能增大start。
当 start + end > target 时，start不能在缩小了，只能缩小end。

一直到找到 target 或 start 与 end 相遇结束。


测试数据：
https://leetcode.com/problems/two-sum/description/

"""

try:
    range = xrange
except NameError:
    range = range

class Solution(object):
    def twoSum(self, nums, target):

        result = self._twoSum(nums, target)
        a = nums.index(result[0])
        # b = nums.index(result[-1], a+1)
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == result[1]:
                return [a, i]
                # b = i
                # break
        # return [a, b]
        
    
    def _twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        sortedNums = sorted(nums)
        start = 0
        end = len(sortedNums) - 1
        while start <= end:
            # print(nums[start] + nums[end])
            if sortedNums[start] + sortedNums[end] == target:
                return sortedNums[start], sortedNums[end]
            
            if sortedNums[start] + sortedNums[end] > target:
                end -= 1
            else:
                start += 1
                
    # def binarySearch(self, rawList, target):
    #     split = len(rawList) // 2
        
    #     left = rawList[:split]
    #     right = rawList[split:]
        
        
    #     if not left and not right:
    #         return None
        
    #     if left and left[-1] == target:
    #         return True
        
    #     if right and right[0] == target:
    #         return True
        
    #     if len(left) > 1 and left[-1] > target:
    #         return self.binarySearch(left, target)
        
    #     if len(right) > 1 and right[0] < target:
    #         return self.binarySearch(right, target)
        
        
    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """

    #     sortedNums = sorted(nums)
    #     for i, data in enumerate(sortedNums):
            
    #         if self.binarySearch(sortedNums[:i]+sortedNums[i+1:], target-data):
    #             result = sorted([nums.index(data), nums.index(target-data)])
    #             if result[0] == result[1]:
    #                 return [result[0], nums[result[0]+1:].index(target-data)+result[0]+1]
                
    #             return result
            # elif target < 0 and data > target:
                # if self.binarySearch(nums[:i]+nums[i+1:], target-data):
                    # return sorted([i, nums[i+1:].index(target-data)+i+1])

