"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

返回第三大的数，如果不存在则返回最大的，重复的算一个。
https://leetcode.com/problems/third-maximum-number/description/

找到第 k 大个数一般的思路有：
1. 排序后放到数组中，排序算法使用归并和快排在理想情况下都是O(nlogn)，归并比较稳定一些。之后的索引是O(1)。
   这种的适合并不需要插入的情况，因为每次插入的时间复杂度为 O(n)。

2. 建立二叉搜索树，进阶的话红黑树或AVL树。
   这种情况下搜索和插入在理想情况下都是O(logn)。

3. 就此题来说的O(n)思路：
   建立三个变量，first,second,third,首先确保不是None，然后挨个放数据，最后输出结果。

这里直接用排序了。


"""
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        
        return sorted(nums, reverse=True)[2]
