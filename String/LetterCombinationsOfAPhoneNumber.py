"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.


图看链接：
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/


老式手机键盘一样，返回所有的组合。

使用的递归思路：
迭代每一个组合，返回所有的组合...
应该容易理解。时间复杂度上应该只有 O(xn)的解法。

测试链接：
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

beat 100% 20ms。
应该会有浮动吧，一次通过，不测第二次了。


"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        maps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        
        def reduce_abc(strs, currentStr=""):
            if not strs:
                return currentStr
            else:
                for i in maps[strs[0]]:
                    x = reduce_abc(strs[1:], currentStr=currentStr+i)
                    if x:
                        result.append(x)
        reduce_abc(digits)
        return result
