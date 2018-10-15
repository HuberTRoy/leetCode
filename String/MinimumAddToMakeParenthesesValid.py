"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

 

Example 1:

Input: "())"
Output: 1
Example 2:

Input: "((("
Output: 3
Example 3:

Input: "()"
Output: 0
Example 4:

Input: "()))(("
Output: 4
 

Note:

S.length <= 1000
S only consists of '(' and ')' characters.

给一个字符串只包含 "(" 和 ")"。

返回至少补多少个可以达成全部有效。

思路：
去除原来有效的，剩余多少个即为需要多少个。


"""
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0
        t = [S[0]]
        for i in S[1:]:
            if i == ')':
                if not t:
                    t.append(i)
                    continue
                    
                if t[-1] == '(':
                    t.pop()
                else:
                    t.append(i)
            else:
                t.append(i)
        return len(t)
        