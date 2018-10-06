"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

整数列表 -> 字符串 -> 整数 -> +1 ->字符串 -> 整数列表。

有点无脑，效率也可。

beat 63% 24ms.
测试地址：
https://leetcode.com/problems/plus-one/description/

"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        return list(map(int, list(str(int(''.join(map(str, digits)))+1))))