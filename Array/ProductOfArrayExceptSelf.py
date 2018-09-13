"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

给一个数组，返回数组中除了这一位的数其他数的乘积。

不能用除的，且时间复杂度需要为 O（n）。

进阶条件 空间复杂度为常数级别。

一刷进阶条件没达成。

基本思路是，一左一右两个存储位置的新列表。

从左到右过一遍，从右到左过一遍。算出每个数左边和右边的乘积。

最后输出每个位置的左*右。

效率是 O(n)，没用除。但空间是 O(2n)。

beat 57% ~ 80% (在 2 中需要把 range 变为 xrange).
前面那几个的思路也是同样的。多测几次应该也能beat 100%...

哎哎？突然想到，output 的数组不算在额外空间里的话，
可以直接把output数组作为 left。然后right的时候直接替换就好了啊。

没错，这样就是 O(1) 了，进阶达成。

beat 98%。

测试链接：
https://leetcode.com/problems/product-of-array-except-self/description/

"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1]
        for i in range(len(nums)-1):
            output.append(output[-1] * nums[i])
        
        right = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = right * output[i]
            right *= nums[i]
            
        return output

        # left = [1]
        # right = [1]
        
        
        # for i in range(len(nums)-1):
        #     left.append(left[-1] * nums[i])
                
        # for i in range(len(nums)-1, 0, -1):
        #     right.append(right[-1] * nums[i])
        
        # length = len(left)
        
        # return [left[i] * right[length-1-i] for i in range(length)]
