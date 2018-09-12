"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

给出从 0 - n的数，找出其中缺少的那个。


思路：
一开始的思路只有 set ... set(n+1)，set(nums)，然后取差集。
这种方法固然可以通过测试，不过题目要求使用常数空间也就是 O(1)。

后来经过 Discuss 区里的点拨，发现几种有趣的方法：

1. 使用异或。 两个相同的数会相互抵消掉。也就是说，从0-n异或一遍。然后在用这个数把nums里的给异或一遍。好了剩下的就是那个缺少的了。
2. 使用和。思路与异或有异曲同工之妙，0-n加一遍。然后在减去，剩下的也是。

运用数学方法，很妙。

测试地址：
https://leetcode.com/problems/missing-number/description/

这里用了加。异或一样的。

beat 88% 28ms.

"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # x = list(set(range(max(nums)+1)) - set(nums))
        # if x:
        #     return x.pop()
        # else:
        #     return max(nums)+1
        all_nums = sum(range(len(nums)+1))
        
        for i in nums:
            all_nums -= i
        
        return all_nums
