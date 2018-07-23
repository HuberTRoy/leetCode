"""
In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:
Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

测试用例：
https://leetcode.com/problems/replace-words/description/

思路：
第一个思路是直接迭代，然后用in查看是否在某个单词中，是的话就直接替换。
这样做有违要求，successor是root+followed。不能是 xxx+root+followed.

当然即使不违反题目要求也基本是不行的，这样做的时间复杂度会变为 O(m*n)其中的n为字典中字符串的总长度。in这个操作符应该是将每个字符都一一对应一遍。

第二个思路是用正则。直接排序后全替换一遍，易写，但效率非常低。与上一个一致。不过提供了一种小思路。

第三种是根据前缀，学习到前缀树 `Trie`。

前缀树用来保存一系列字符串，增加这些字符串公共部分的复用率，达到快速检索的目的。
参考：
https://segmentfault.com/a/1190000008877595

不过，在这里题目直接将字典给了出来，也无需再构建前缀树。
使用前缀树的目的是进行高效的检索。

比如
"the cattle was rattled by the battery"
字典是 
["cat", "bat", "rat", "rain"]
那么前缀树的构成是
    c    b     r
    a    a     a  
    t    t   t   i
                 n 

在这种思路下，我们在搜索the的时候也是要先匹配t是否在第一层中，然后再逐个向下匹配。

既然已经给了字典，直接利用字符串索引即可。

1. 将原句根据' '分离。
2. 迭代分离后的句子，然后迭代字典。
3. 将字典的第一个字符与迭代的句子的第一个字符相比较，如果相同则进入判断，判断成功则结束此次字典迭代进入下一个单词。
4. 判断的逻辑，将字典中的此单词与此单词传入，迭代字典中的此单词，逐个字符比较相同则不断比较，一直到字典中的此单词耗尽或此单词耗尽。


"""


class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        
        def judge(dict_word, word):
            for i in dict_word:
                if not word:
                    return False
                if i == word[0]:
                    word = word[1:]
                    continue
                return False
            return True
        
        dicts = sorted(dict, key=len)
        sentence = sentence.split(' ')
        for i, d in enumerate(sentence):
            for j in dicts:
                if d[0] == j[0]:
                    if judge(j[1:], d[1:]):
                        sentence[i] = j
                        break
                        
        return ' '.join(sentence)

#         最开始的正则思路，用\s保证一定是root+followed的形式。
#         sentence = ' ' + sentence
#         for i in dicts:
#             sentence = re.sub(r'\s{}\w*'.format(i), ' '+i, sentence)
        
#         return sentence[1:]
