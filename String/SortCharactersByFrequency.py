"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

给定一个字符串，以字符出现的频率进行排序。

思路：
1. 用一个字典记录每个字符出现的频率。
2. 根据出现的频率排序。
3. 因为直接堆在一起即可，直接构建一个列表。
4. 在组合起来。

beat 95% 36ms.

测试地址:
https://leetcode.com/problems/sort-characters-by-frequency/description/

"""
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        x = {}
        
        for i in s:
            try:
                x[i] += 1
            except:
                x[i] = 1
        
        b = sorted(x, key=lambda t: x[t], reverse=True)

        return ''.join([i*x[i] for i in b])
        