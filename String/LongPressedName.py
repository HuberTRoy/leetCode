"""
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
 

Note:

name.length <= 1000
typed.length <= 1000
The characters of name and typed are lowercase letters.

判断 typed 里 是否存在 name，保证顺序的。

思路：
typed 和 name 各一个指针，命中了就一起走，没命中就typed走。最后判断指针是否指向了name尾。

测试地址：
https://leetcode.com/contest/weekly-contest-107/problems/long-pressed-name/

"""
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        x = 0
        y = 0
        
        x_length = len(name)
        y_length = len(typed)
        
        while x < x_length and y < y_length:
            
            if typed[y] == name[x]:
                y += 1
                x += 1
            else:
                y += 1
        
        if x == x_length:
            return True
        return False
