"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.

思路 Dp，处理下 1 即可。 不考虑 0，nums[i] 不会为 0。

beat 19%

测试地址:
https://leetcode.com/problems/subarray-product-less-than-k/description/

可剪枝优化。
"""
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        dp = []
        result = 0
        start = 0
        for i in range(len(nums)):
            if nums[i] < k:
                result += 1
                dp = [nums[i]]
                start = i
                break
        
        for i in range(start+1, len(nums)):
            if nums[i] == 1 and nums[i] < k:
                dp.append(1)
                result += len(dp)
                continue
                
            new = []
            
            if nums[i] < k:
                result += 1
                new.append(nums[i])
                
            
            for j in dp:
                if j * nums[i] < k:
                    result += 1
                    new.append(j * nums[i])
            
            dp = new
        return result
        