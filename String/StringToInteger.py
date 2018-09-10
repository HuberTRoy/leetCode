"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.


实现一个从字符串到整数的函数。

给出的例子有这么多。

主要思路：
1. 先是去掉两边的空白。
2. 确定出首位符号（有则按有的，无则按+。）
3. 之后判断剩下个每一位是否是一个十进制数。
4. 最后判断 -2**31 < x < 2**31-1，输出。

还发现了一个Python 2 与 3 的不同之处：
在处理整数的时候：
2 中 int("-     321") 可以处理为 -321.
3 中则会报错。 

测试地址：
https://leetcode.com/problems/string-to-integer-atoi/description/

beat 95% 36ms.

"""

class Solution(object):
    def myAtoi(self, strs):
        """
        :type str: str
        :rtype: int
        """
        nums = '1234567890'
        signs = '+-'
        
        strs = strs.strip()
        
        if not strs or len(strs) == 1 and strs in signs:
            return 0

        if strs[0] in signs:
            sign = strs[0]
            strs = strs[1:]
        else:
            sign = '+'

        str_num = '0'
        x = 0
        for i in strs:
            if i == ' ' and str_num == '0':
                return 0
            if i not in nums:
                if sign == '+':
                    x = int(str_num)
                else:
                    x = -int(str_num)
                break
            else:
                str_num += i
        else:
            if sign == '+':
                x = int(str_num)
            else:
                x = -int(str_num)

        if x > 2**31-1:
            return 2**31-1
        elif x < -2**31:
            return -2**31
        else:
            return x
