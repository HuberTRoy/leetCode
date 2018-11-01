"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

思路：
二分。

瓶颈依然在于插入列表中的时候需要的时间复杂度为 O(n)。

beat
82%

测试地址:
https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/

"""
import bisect

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        x = []
        result = []
        
        for i in nums[::-1]:
            result.append(bisect.bisect_left(x, i))
            bisect.insort(x,i)
        
        return result[::-1]