"""
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
1. The length of the given array will not exceed 50,000.
2. All the numbers in the input array are in the range of 32-bit integer.

如果索引 i < j 并且 nums[i] > 2 * nums[j]，那么就称它为牛波翻转对。

给一个数组，返回里面有几个牛波翻转对。

思路：

一个 Dp 思路，从后向前，解出每一个点若要达成牛波翻转对所需要的值是多少。

比如 1 , 要达成需要 2 以上。
    3, 则需要 6 以上。

将这些放到一个列表里，然后来新值之后判断若将它插入这个列表的话所插入的位置（下标），
这个位置即为已经判断过的能与它达成牛波翻转对的位置。

用二分法可以达成 n log n 的查询，美中不足的是列表的插入仍需要 O(n)。

beat 17%

测试地址：
https://leetcode.com/problems/reverse-pairs/description/


"""
import bisect

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _base = []
                
        result = 0
        
        for i in range(len(nums)-1,-1,-1):
            index = bisect.bisect_left(_base, nums[i])
            result += index
            bisect.insort_right(_base, nums[i]*2)
    
        return result
        