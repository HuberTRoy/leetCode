"""
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?

1 锁了，暂不能做。

II 的话规则：
    单数位 大于 双数位。

思路：

一开始的话想到的是排序后，取中间，然后后半部分按从大到小铺在单数位上。
                                   前半部分按从大到小从末尾的双数位开始向前铺。

这个思路一开始是可以的，不过忽略了相等的部分，因为有可能铺的时候相遇。所以注意下，相等的等上面的过程铺完之后，用于补剩下的部分。

进阶要求是：
 O(n) 时间，O(1) 空间。

排序的话 O(n log n)，不符合要求。

这个思路的关键点是找到中位数，但怎么在 O(n) 时间 O(1) 空间找到中位数呢？

下面是我的思考，没有最终实现。

1. 先找到里面最小的元素并获取出总长度。
2. 过一遍，找出 总长度 // 2 个比它大的元素，顺便记录出这里面的最大值。
3. 再过一遍，找出 比 2. 中最大值大的 元素。 
4. 再找出比它大的元素个数 - 总长度 // 2 
5. 若刚好有 总长度 // 2 个那么它就是中位数，否则它就是第 k（比它大的元素个数 - 总长度 // 2） 大个元素。
6. 缩小了范围。重复步骤...

时间复杂度非常依赖运气...

下面直接用了排序，没有达成进阶条件，待改进。

beat 
68%

测试地址：
https://leetcode.com/problems/wiggle-sort-ii/description/


"""
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        nums.sort()
        middle = nums[len(nums) // 2]
        larger = [i for i in nums[len(nums)//2:] if i != middle]
        smaller = [i for i in nums[:len(nums)//2] if i != middle]
        equal = [i for i in nums if i == middle]
        
        larger.reverse()
        smaller.reverse()
        length = len(nums)
        odd = 1
        even = length - 1 if (length-1) % 2 == 0 else length - 2
        
        for i in larger:
            # try:
            nums[odd] = i

            odd += 2
        
        for i in smaller:
            nums[even] = i
            
            even -= 2
        
        while even >= 0:
            nums[even] = equal.pop()
            even -= 2
        
        while odd < length:
            nums[odd] = equal.pop()
            odd += 2
