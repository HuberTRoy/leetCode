"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.



所有单词的共同的前缀。
没什么技巧，从每个单词的第一个开始对比就好了。
Python 中有一个 zip 可以做这些事情。

beat 90%

测试地址：
https://leetcode.com/problems/longest-common-prefix/description/

今日的零启动任务。

"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        
        for i in zip(*strs):
            a = i[0]
            for j in i[1:]:
                if j != a:
                    return result
            else:
                result += a
        
        return result

