"""
Input: "Hello World"
Output: 5

每个单词都会被 ' ' 分割。
所以要做的是从尾向前找第一个空格。当然Python 下用 strip(' ')分割后取[-1]是最好写出来的。
当然还要确保下尾部开始不能是' '，要找到第一个单词才行。

测试用例：
https://leetcode.com/problems/length-of-last-word/description/

"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        result = 0
        flag = False
        
        for i in s[::-1]:
            if i == ' ' and not flag:
                continue
            elif i == ' ' and flag:
                return result
            else:
                result += 1
                flag = True
                continue
                
            return result
        return result
