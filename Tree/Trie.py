"""
前缀树又叫字典树，该树会覆盖多个相同的字符以形成空间上的优势。

如：
rat 与 rain
  r
  a
t  i
   n
最终会形成这样的树。

字典树有多种实现方式，下面直接用了列表（数组）来实现。
测试用例：
https://leetcode.com/problems/implement-trie-prefix-tree/description/

使用Python 中的字典可以直接形成这种树，所以弃用这种方式，用类的思路实现了一下。

"""

class TrieNode(object):
    # __slots__ 考虑到TrieNode会大量创建，使用 __slot__来减少内存的占用。
    # 在测试的15个例子中：
    # 使用 __slots__会加快创建，平均的耗时为290ms-320ms。
    # 而不使用则在 340ms-360ms之间。
    # 创建的越多效果越明显。
    # 当然，使用字典而不是类的方式会更加更加更加高效。
    __slots__ = {'value', 'nextNodes', 'breakable'}

    def __init__(self, value, nextNode=None):
        self.value = value
        if nextNode:
            self.nextNodes = [nextNode]
        else:
            self.nextNodes = []
        self.breakable = False
    
    def addNext(self, nextNode):
        self.nextNodes.append(nextNode)
    
    def setBreakable(self, enable):
        self.breakable = enable
    
    def __eq__(self, other):
        return self.value == other

    
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = []
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        self.makeATrieNodes(word)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        for i in self.root:
            if i == word[0]:
            
                return self._search(i, word[1:])
        return False
    
    def _search(self, root, word):
        if not word:
            if root.breakable:
                return True
            return False
        if not root.nextNodes:
            return False
        
        for i in root.nextNodes:
            if i == word[0]:
                return self._search(i, word[1:])
        
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        for i in self.root:
            if i == prefix[0]:            
                return self._startWith(i, prefix[1:])
        return False
    
    def _startWith(self, root, prefix):
        if not prefix:
            return True
        
        if not root.nextNodes:
            return False
        
        for i in root.nextNodes:
            if i == prefix[0]:
                return self._startWith(i, prefix[1:])
        
        return False
        
    def makeATrieNodes(self, word):
        for j in self.root:
            if word[0] == j:
                rootWord = j
                break
        else:

            rootWord = TrieNode(word[0])
            self.root.append(rootWord)
            for i in word[1:]:
                nextNode = TrieNode(i)
                rootWord.addNext(nextNode)
                rootWord = nextNode
            rootWord.setBreakable(True)
            return
        
        # has the letter. 
        word = word[1:]
        while 1:
            if not word:
                rootWord.setBreakable(True)
                break
                
            for i in rootWord.nextNodes:
                if i == word[0]:
                    rootWord = i
                    word = word[1:]
                    break
            else:
                for i in word:
                    nextNode = TrieNode(i)
                    rootWord.addNext(nextNode)
                    rootWord = nextNode
                rootWord.setBreakable(True)
                break