"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.


与1不同的是这个首尾相连，是个环。

   1
 3  2
  1

只有3户人家时只能抢一户。
只有4户人家时能抢其中的两户。

5户以上时可以应用1时的规则，不过这次不要把最后一户算进来。
进行两次，一次以 0 为首，第二次以 -1 为首。

两次即可包含所有结果了。

效率 O(n)。

beat 100% 20ms

测试地址：
https://leetcode.com/problems/house-robber-ii/description/



"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        if len(nums) <= 3:
            return max(nums)
        
        if len(nums) <= 4:
            return max(max(nums), nums[1]+nums[-1], nums[2]+nums[0])
        
        robber = [nums[0], nums[1], nums[2]+nums[0]]
        
        for i in range(3, len(nums)-1):
            robber.append(max(nums[i] + robber[i-2], nums[i] + robber[i-3]))
        
        maxes = max(robber)
        
        nums = [nums[-1]] + nums
        nums.pop()

        robber = [nums[0], nums[1], nums[2]+nums[0]]
        
        for i in range(3, len(nums)-1):
            robber.append(max(nums[i] + robber[i-2], nums[i] + robber[i-3]))
        
        
        return max(robber+[maxes])
