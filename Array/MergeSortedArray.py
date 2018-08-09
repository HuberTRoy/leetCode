"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]


合并两个排序过的整数数组。

要求在nums1中做修改。

测试用例：
https://leetcode.com/problems/merge-sorted-array/description/

第一版：
思路与merge two sorted list 一致...
passed 但是效率较低。

第二版：
直接以倒序的方式，从尾到头判断，这样不需要额外的空间，列表，效率也自然要高。
passed，但还不是最高的。

第三版：
通过的解法中有一种非常聪明的：

由于本身是在nums1中操作，基于 merge two sorted list 的思想中的：
如果有一方结束了那么就把另一方直接合并过去。

但我们是在nums1中做修改，所以可以修改下判断规则：

不再以整个m+n作为while的依据而是m和n都不为0。
若m为0,那么合并剩余的n到nums1中，
若n为0,则无需做任何动作，因为本来就是nums1.。




"""
class Solution(object):
    # 第一版：
    # def merge(self, nums1, m, nums2, n):
    #     """
    #     :type nums1: List[int]
    #     :type m: int
    #     :type nums2: List[int]
    #     :type n: int
    #     :rtype: void Do not return anything, modify nums1 in-place instead.
    #     """
    #     nums3 = nums1[:m]
        
    #     nums1_index = 0
    #     nums2_index = 0
    #     nums3_index = 0
        
    #     mn = m+n
    #     length_nums3 = len(nums3)
    #     length_nums2 = len(nums2)
        
    #     while nums1_index < mn:
    #         if nums3_index == length_nums3:
    #             for i in nums2[nums2_index:]:
    #                 nums1[nums1_index] = i
    #                 nums1_index += 1
    #             break
                
    #         if nums2_index == length_nums2:
    #             for i in nums3[nums3_index:]:
    #                 nums1[nums1_index] = i
    #                 nums1_index += 1
    #             break
                    
    #         if nums3[nums3_index] < nums2[nums2_index]:
    #             nums1[nums1_index] = nums3[nums3_index]
    #             nums3_index += 1
    #         else:
    #             nums1[nums1_index] = nums2[nums2_index]
    #             nums2_index += 1
    #         nums1_index += 1

    # 第二版：
    # def merge(self, nums1, m, nums2, n):
    #     """
    #     :type nums1: List[int]
    #     :type m: int
    #     :type nums2: List[int]
    #     :type n: int
    #     :rtype: void Do not return anything, modify nums1 in-place instead.
    #     """
    #     mn = m + n - 1
        
    #     while mn >= 0:
            
    #         if m == 0:
    #             for i in nums2[:n][::-1]:
    #                 nums1[mn] = i
    #                 mn -= 1
    #             break
    #         if n == 0:
    #             for i in nums1[:m][::-1]:
    #                 nums1[mn] = i
    #                 mn -= 1
    #             break
            
    #         if nums1[m-1] > nums2[n-1]:
    #             nums1[mn] = nums1[m-1]
    #             m -= 1
    #         else:
    #             nums1[mn] = nums2[n-1]
    #             n -= 1
    #         mn -= 1

    # 第三版
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        mn = m + n - 1
        
        while m > 0 and n > 0:
           
            
            if nums1[m-1] > nums2[n-1]:
                nums1[mn] = nums1[m-1]
                m -= 1
            else:
                nums1[mn] = nums2[n-1]
                n -= 1
            mn -= 1
        
        if n > 0:
            nums1[:n] = nums2[:n]
