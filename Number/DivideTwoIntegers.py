"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

除以某数，其结果要尽可能趋向0的，且为整数。

直接用Python 中的地板除 // 即可。

判断两个数的符号是否相同和处理 2**31-1 和 -2**31 即可。

测试链接：
https://leetcode.com/problems/divide-two-integers/description/

beat 100% 28ms.

这个题没什么意思...应该作为第二天的零启动任务来做，但已经做了，换一个零启动任务吧。

"""
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        x = abs(dividend) // abs(divisor)
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            
            if -x < -2**31:
                return -2**31 
            return -x
        
        if x > 2**31-1:
            return 2**31-1
        return x

