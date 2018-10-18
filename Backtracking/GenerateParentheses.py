"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

生成有效的括号对。

关键字：
    递归

beat 
100%

测试地址：
https://leetcode.com/problems/generate-parentheses/description/
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def _generateParenthesis(x, y, parenthesis):
            if not x and not y:
                result.append(parenthesis)
                return
            
            if y > x:
                _generateParenthesis(x, y-1, parenthesis=parenthesis+')')
            
            if x:
                _generateParenthesis(x-1, y, parenthesis=parenthesis+'(')
        
        _generateParenthesis(n-1, n, '(')
        
        return result
        