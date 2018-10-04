"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

删除给定数组的重复的数字，在原数组上操作。

这个从后向前，判断是否重复，若重复将下标加入要删除的列表中。
最后迭代这个要删除的列表，然后将所有下标删除。因为是从后向前所以不会打乱顺序。

beat 56%

测试地址：
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 
        
        length = len(nums)-1
        
        one = nums[length]
        
        remove_index = []
        
        for i in range(length-1, -1, -1):
            if one == nums[i]:
                remove_index.append(i)
                continue
            one = nums[i]
        
        for i in remove_index:
            nums.pop(i)
