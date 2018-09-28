"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

判断 s 与 t 是否为变位词。

思路是排序 s 和 t，若相等则确定是变位词。

直接用 sorted 了。
效率 O(nlogn)

beat 61%.

前面都是用的 dict 的思路，dict 查询是 O(1) 总体也就是 O(n) 了。

dict 的思路基本是记录每个单词出现的次数，到0就剔除，最后若不剩余的话则表示是变位词，不写了，没有难点。

测试地址：
https://leetcode.com/problems/valid-anagram/description/


"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if sorted(s) == sorted(t):
            return True
        return False
        