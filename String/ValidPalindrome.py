"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

忽略特殊字符，空白，大小写。判断是否为回文字符串，空的话也为有效的。

关键字: re.

测试地址：
https://leetcode.com/problems/valid-palindrome/description/

"""
import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if not s:
            return True
        
        s = s.lower()
        x = ''.join(re.findall(r'[a-z0-9]{1}', s))
        
        return x == x[::-1]
        