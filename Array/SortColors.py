"""

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?


给一个放置了颜色的数组，里面包含三种颜色分别为 红 白 蓝，用 0 1 2 表示，它们在数组中是无序的，现在要把它们进行排序。

要求是：
原数组排序。

进阶条件是：
1. one-pass.
2. 使用常数空间。O（1）空间。

直接.sort排序是作弊行为。

进阶条件里给出一个直接的方法：

过一遍，分别记录出 0 1 2 的个数，然后按个数将它们分别替换。

这样做虽然是 O(1) 空间，不过不是 one-pass。

自己的思路：

由于只有三种要排序的，以1为中心点，那么出现0放到最左边即可，出现2放到最右边即可。

那么设置一个指针。从 0 开始，若为0则将它从原数组弹出，然后放到0的位置，若是2则放到末尾。若是1则不变。

1. 出现0和1的情况都将index向前推进1，2的话则不推进。

这样做是one-pass,O(1)，符合进阶条件。缺点是 insert和pop都是 O(n) 时间复杂度的算法。使用deque会快一些，现在也可以。


beat:
64%

测试地址：
https://leetcode.com/problems/sort-colors/description/

"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        index = 0
        times = 0
        length = len(nums)
        
        for i in range(length):
            if nums[index] == 0:
                x = nums.pop(index)
                nums.insert(0, x)
                index += 1
            elif nums[index] == 2:
                x = nums.pop(index)
                nums.append(x)
            else:
                index += 1
