"""
We have a string S of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.

Example 1:

Input: S = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: 
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.
Note:

1 <= S.length = shifts.length <= 20000
0 <= shifts[i] <= 10 ^ 9


给一个字符串，不断经过转换，得出最终字符串。

每一轮的转换都是对这之前的所有字符串而言的。

思路：
1.
 从后向前，得到索引 % 26.

2. 
 转换字符到 ascii，相加然后处理超过的量。

测试地址：
https://leetcode.com/contest/weekly-contest-88/problems/shifting-letters/

"""
class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        
        letters = "abcdefghijklmnopqrstuvwxyz"
        
        new_s = []
        old_index = 0
        for i, j in zip(S[::-1], shifts[::-1]):
            index = letters.index(i)
            
            new_index = (index+j+old_index)%26
            
            new_s.append(letters[new_index])
            old_index += j
        return ''.join(new_s[::-1])
        