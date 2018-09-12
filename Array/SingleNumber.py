"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4


给定一个非空数组，除了一个元素外，其余均出现两次。找出它。

需要在线性时间内，且不用额外空间。

用到了 missing number 的思路，利用异或的性质，相同的异或会抵消掉。

直接在原数组上操作，用了 i 变量，一个变量都不用要怎么写？
Discuss里也没找到相关的。

测试地址：
https://leetcode.com/problems/single-number/description/

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(1, len(nums)):
            nums[i] = nums[i] ^ nums[i-1]
        
        return nums[-1]

