"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

给一组数组，返回能不能到达最后的位置。每个位置包含的是从此点出发可走的最远距离，在哪里落脚随意。

思路：

从 0 开始，找到剩下的里面 下标 + 能走多远 最大的一个。然后一直重复即可。

下面的这个代码并不是一遍的 O(n) ，用此思路也可以优化成 O(n)，不优化了，没什么优化难点。
关键字：
current_index 变更为上次range的末尾，并相应的减去。

beat 66%

测试地址：
https://leetcode.com/problems/jump-game/description/

"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
            
        
        dp = [nums[0]]
        current_index = 0
        
        while 1:
            if current_index + dp[-1] >= len(nums)-1:
                return True
            base = 0
            index = current_index
            for i in range(current_index, current_index+dp[-1]+1):
                if nums[i] + i > base:
                    base = nums[i] + i
                    index = i
            
            if current_index == index:
                return False
            
            current_index = index
            dp.append(base-index)