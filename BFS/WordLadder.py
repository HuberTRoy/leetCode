"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.


这个BFS有点...

一开始的思路就是 BFS，写法不同。

一开始的写法是每次都从 wordList 里找单词，结果是有一个case跑不通。

后来实在没思路学习 Discuss 里的内容，Discuss 里的 BFS 是每一个都生成26个新的单词，然后判断是否在 wordList 中。

这种方法可以全部跑通... 

可优化的点在于如何高效的找到存在于 _wordList 中可变换的值。

beat 66%

测试地址：
https://leetcode.com/problems/word-ladder/description/

"""
from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        if len(beginWord) == 1:
            return 2
        
        _wordList = set(wordList)
        
        result = deque([[beginWord, 1]])

        while result:
            word, length = result.popleft()
            
            if word == endWord:
                return length 

            _length = length + 1

            for i in range(len(word)):
                for c in 'qwertyuiopasdfghjklzxcvbnm':
                    new = word[:i]+c+word[i+1:]
                    
                    if new in _wordList:
                        _wordList.remove(new)
                        result.append([new, _length])
        
        return 0
