"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

与 IsomorphicString 一样，此题来自于做完IsomorphicString的相关推荐。

思路：
直接 one line 的思路：
转换成列表，然后一致。判断下字符位数的不同。

同样的思路换成这个题就能跑20ms..
beat 99%.

"""
class Solution(object):
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern = list(pattern)
        string = string.split(' ')
        if len(pattern) != len(string):
            return False
        temp = len(set(zip(pattern, string)))
        return temp == len(set(pattern)) and temp == len(set(string))
