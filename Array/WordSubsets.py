"""
We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a. 

Return a list of all universal words in A.  You can return the words in any order.

 

Example 1:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]
Example 3:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]
Example 4:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]
Example 5:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]
 

Note:

1 <= A.length, B.length <= 10000
1 <= A[i].length, B[i].length <= 10
A[i] and B[i] consist only of lowercase letters.
All words in A[i] are unique: there isn't i != j with A[i] == A[j].


如果 B 中每一个元素出现的字符均在 A 中某一个元素中出现，则视为子单词，给一个A 和 B求子单词数量。

思路：
哈希 A,
哈希 B。

B 哈希的时候要注意，有重复。

比如["ec","oc","ceo"]
只要有 c e o 各一次即可。不需要每个都判断一次。

测试地址：
https://leetcode.com/problems/word-subsets/description/

这个写法比较慢，前面的思路基本都是哈希。

"""
from collections import Counter

class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        dict_A = {i:Counter(i) for i in A}
        dict_B = {}
        
        for i in B:
            c = Counter(i)
            for j in c:
                if c.get(j) > dict_B.get(j, 0):
                    dict_B[j] = c.get(j)
                    
        result = []
        
        for i in dict_A:
            for j in dict_B:
                if dict_B[j] > dict_A[i].get(j):
                    break
            else:
                result.append(i)
                    
        return result
