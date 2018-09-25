"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

你是专业强盗计划偷钱。每个房子都有钱，不能连续偷，否则会触发警报，计划能偷的最多的钱，要偷哪些房子。

用Dp的子问题思路：
不能连续的偷：

1 和 2只能偷这两个，没得选择。
3 能顺带偷1。
4 则需要在 1 和 2 中抉择。
5 则需要在 2 和 3 中抉择。
所以

子问题则是每个点能偷到的最大数。

初始化3个
例
[2,7,9,3,1]
dp = [2,7,11(9+2)]
max(3+7, 3+2)
dp = [2,7,11(9+2),10(3+7)]
max(1+11,1+7)
dp = [2,7,11(9+2),10(3+7),12(1+11)]

可以中途记录，也可以最后max，当然中途记录的话效率的最高的。

就这个测试来说max也没差。

测试地址：
https://leetcode.com/problems/house-robber/description/

beat 99% 20ms

"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        if len(nums) <= 2:
            return max(nums)
        
        robber = [nums[0], nums[1], nums[2] + nums[0]]
        
        for i in range(3, len(nums)):
            robber.append(max(nums[i] + robber[i-2], nums[i] + robber[i-3]))

        return max(robber)
