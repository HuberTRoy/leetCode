"""
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

思路：
Dp,
Dp子问题：
分成两个子问题：
第一个子问题是length，第二个是count，记录的话肯定是要记录最长最多的。

第一个子问题：
length:
每个单独的可以看做是1
[4,3,2,0,3,1,7,9,1,7,9]
[1,1,1,1,1,1,1,1,1,1,1]

初始化每个长度均为1。

若现在的num比之前的num大，长度上则在这个长度的基础上+1。
[4,3,2,0,3,1,7,9,1,7,9]
         3>2,3>0，最大都是2。
[1,1,1,1,2,    1,1,1,1,1,1]
...

第二个子问题：
count：
[4,3,2,0,3,1,7,9,1,7,9]
[1,1,1,1,1,1,1,1,1,1,1]

初始化每个count也都是1。

若现在的num比之前的num要大，若是第一次出现，则等于这个次数，否则加上这个次数。
[4,3,2,0,3,1,7,9,1,7,9]
         3>2，由于是第一次出现，数量变为2所记录的数量。
         3>0，第二次出现，数量加上0所记录的数量。
[1,1,1,1,2,    1,1,1,1,1,1]

关于如何判断是不是第一次出现：
首先全部初始化为1。若当前num大于之前num时，可以判断长度是否与之前的相等：
3>2时，此时应该为 (2, 3)，
2 所记录的长度数量为 (1, 1)
3 此时记录的长度数量为 (1, 1)
这时由于是第一次出现，3处长度应为2([2, 3])，但还未变化，所以可以由长度判断是否为第一次。
经过此轮循环后，3处所记录的长度数量应为：(2, 1)

3>0时，这时
0 所记录的长度数量为 (1, 1)
3 所记录的长度数量为 (2, 1)
这时可以直接加。

测试地址：
https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/

O(n^2) 题目最大只有2000个数据，勉强通过。

"""

class Solution(object):

    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        length = [1] * len(nums)
        count = [1] * len(nums)
        
        maxLength = 1

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[j] == length[i]:
                        count[i] = count[j]
                        
                    if length[j]+1 == length[i]:
                        count[i] += count[j]
                    
                    x = max(length[j]+1, length[i])

                    length[i] = x
                    maxLength = max(maxLength, x)

        return sum([count[i] for i,j in enumerate(length) if j == maxLength])



