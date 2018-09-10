"""

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


翻转一个整数。

我直接用了转成字符串，然后取反然后转成整数的方法。
效率过得去。
beat 45%.

测试地址：
https://leetcode.com/problems/reverse-integer/description/

"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # str_x = str(x)
        if x < 0:
            x = -int(str(abs(x))[::-1])
        else:
            x = int(str(abs(x))[::-1])
        
        if x > 2**31 or x < -2**31:
            return 0
        return x
