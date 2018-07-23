"""

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

给定一个2D数组，找到是否该字符串存在于其中。

首先进行了一次失败的尝试....

没读第二行，直接用二叉树做搜索，理想情况下就是O(nlogn)。

发现没通过，要 「相邻」 的字符才可以。

那这可以用DFS深度优先。找到合适的点就一直深入下去，如果找到了就返回True。
如果没找到就找其他相邻的还有没有，没有就False有就继续寻找下去，直到word耗尽。

测试用例：
https://leetcode.com/problems/word-search/description/
"""

'''python 
class TreeNode(object):

    def __init__(self, val, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right
        self.count = 1
        
class binarySearchTree(object):
    """
        二叉搜索树，
        它的性质是左边节点都小于根节点，右边的都大于根节点。
        而且一般来说它是不存在重复元素的。

    """

    def __init__(self, root):
        if isinstance(root, TreeNode):
            self.root = root
        else:
            self.root = TreeNode(root)

    def add(self, value):
        # 从顶点开始遍历，找寻其合适的位置。
        root = self.root
        if self.searchAndAddOne(value):
            return
        
        while 1:
            if root.val < value:
                if root.right is None:
                    # if self.search(value):
                    #     break
                    root.right = TreeNode(value)
                    break
                else:
                    root = root.right
                    continue

            if root.val > value:
                if root.left is None:
                    # if self.search(value):
                    #     break
                    root.left = TreeNode(value)
                    break
                else:
                    root = root.left
                    continue

            if root.val == value:
                root.count += 1
                break
                
    def searchAndAddOne(self, value):
        # 查找一个值是否存在于这颗树中,如果存在则计数+1
        return self._search(self.root, value, add=True)

    def searchAndReduceOne(self, value):

        return self._search(self.root, value, reduce=True)
    
    def _search(self, root, value, add=False, reduce=False):
        if root.val == value:
            if add:
                root.count += 1
            if reduce:
                print(root.count, root.val)
                if root.count > 0:
                    root.count -= 1
                else:
                    return False
            return True

        if root.right:
            if root.val < value:
                return self._search(root.right, value, add=add, reduce=reduce)

        if root.left:
            if root.val > value:
                return self._search(root.left, value, add=add, reduce=reduce)

        return False
        
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        myTree = binarySearchTree(TreeNode('-'))
        for i in board:
            for j in i:
                myTree.add(j)
        
        for i in word:
            if not myTree.searchAndReduceOne(i):
                return False
        return True

a = Solution()

print(a.exist([['A']*2], "AAA"))
'''

"""
这一个的思路是从第一个开始，寻找其上下左右，如果有合适的则进入那个继续寻找，直到找到合适的或耗尽。
此版本TTL.

多次失败的尝试后，终于找到快速的方法。

思路仍然是DFS。之前写的时候，使用了deepcopy，每次都会生成一个全新的地图，这样做的坏处是每次生成一个新的地图都会耗费大量时间和空间。
经过测试，一个大点的地图（最下面的那个例子）生成100次会花费大约400ms。

改进后的思路是不在生成新的地图，只在原地图上捣鼓。

思路是这样：
如果此点与word中第一个相同，则将其覆盖。之后进行上下左右移动，有一个命中就会一直判断，如果全不命中就会收回。再从上一个点开始判断。
覆盖的原因是如果不替换那么可能形成环。但一个字符只允许使用一次。
```
FRANCE

0   1   2   3   4   5   6
"F" "Y" "C" "E" "N" "R" "D"
list
0   1   2   3   4   5   6
"K" "L" "N" "F" "I" "N" "U"
list
0   1   2   3   4   5   6
"A" "A" "A" "R" "A" "H" "R"
list
0   1   2   3   4   5   6
"N" "D" "K" "L" "P" "N" "E"
list
0   1   2   3   4   5   6
"A" "L" "A" "N" "S" "A" "P"
list
0   1   2   3   4   5   6
"O" "O" "G" "O" "T" "P" "N"
list
0   1   2   3   4   5   6
"H" "P" "O" "L" "A" "N" "O"

```
第一个 F 0, 0处命中，然后继续上下左右找有没有R命中的。结果没有。那么被替换的F就会还原。
第二个 F 2, 3处命中，然后继续上x，下命中，则替换掉然后继续判断。直到A处判断了FRA但断开了，
这时会还原A，但R的左边还有A同样进行判断但之后也断开了。到R上下左右都没有则还原回F，上下左右又没有则还原到初始。



"""
import copy
import pdb

class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i, d in enumerate(board):
            for i2, d2 in enumerate(d):
                if d2 == word[0]:
                    if self.search(board, i2, i, word):
                        return True
        return False

    def search(self, board, x, y, word):
        """
            
        """
        if not word:
            return True
        # if x == len(board[0][0]) and y == len(board):
        #     return False
        if board[y][x] != word[0]:
            return False

        if board[y][x] == word[0]:
            word = word[1:]
        temp_data = board[y][x]
        board[y][x] = '#'


        # if not word:
            # return True
        
        # up
        if y-1 >= 0:
            if board[y-1][x] != '#':
                if self.search(board, x, y-1, word): # u
                    return True
        # down
        if y+1 < len(board):
            if board[y+1][x] != '#':
                if self.search(board, x, y+1, word): #d
                    return True
        # left
        if x-1 >= 0:
            if board[y][x-1] != '#':
                if self.search(board, x-1, y, word): #l
                    return True
        
        # right
        if x+1 < len(board[0]):
            if board[y][x+1] != '#':
                if self.search(board, x+1, y, word): # r
                    return True
        board[y][x] = temp_data
        return False
        # return 
        # if not word:
        #     return True
        # # up
        # if y-1 >= 0:
        #     if board[y-1][x] == word[0]:

        #         temp_board = board
        #         # temp_board = copy.deepcopy(board)
        #         temp_board[y-1][x] = '#'
        #         if self.search(temp_board, x, y-1, word[1:]):
        #             return True
        # # down
        # if y+1 < len(board):
        #     if board[y+1][x] == word[0]:
        #         temp_board = board
        #         # 
        #         # temp_board = copy.deepcopy(board)
        #         temp_board[y+1][x] = '#'
        #         if self.search(temp_board, x, y+1, word[1:]):
        #             return True
        # # left
        # if x-1 >= 0:
        #     if board[y][x-1] == word[0]:
        #         temp_board = board

        #         # temp_board = copy.deepcopy(board)
        #         temp_board[y][x-1] = '#'
        #         if self.search(temp_board, x-1, y, word[1:]):
        #             return True
        # # right
        # if x+1 < len(board[0]):
        #     if board[y][x+1] == word[0]:
        #         temp_board = board
        #         # temp_board = copy.deepcopy(board)
                
        #         temp_board[y][x+1] = '#'
        #         if self.search(temp_board, x+1, y, word[1:]):
        #             return True

        # return False



"""
改进一下，还是用DFS，不过这次不会在预先去寻找入口。
结果更慢。
"""

# class Solution(object):
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#         return self.search(board, 0, 0, word)


#     def search(self, board, x, y, word):
#         """
            
#         """
#         # return 
#         if not word:
#             return True
#         # if x == len(board[0][0]) and y == len(board):
#         #     return False

#         if board[y][x] == word[0]:
#             word = word[1:]
        
#         board[y][x] = '#'


#         # if not word:
#             # return True
        
#         # up
#         if y-1 >= 0:
#             if board[y-1][x] != '#':
#                 temp_board = copy.deepcopy(board)
#                 if self.search(temp_board, x, y-1, word):
#                     return True
#         # down
#         if y+1 < len(board):
#             if board[y+1][x] != '#':
#                 temp_board = copy.deepcopy(board)
#                 if self.search(temp_board, x, y+1, word):
#                     return True
#         # left
#         if x-1 >= 0:
#             if board[y][x-1] != '#':
#                 temp_board = copy.deepcopy(board)
#                 if self.search(temp_board, x-1, y, word):
#                     return True
#         # right
#         if x+1 < len(board[0]):
#             if board[y][x+1] != '#':
#                 temp_board = copy.deepcopy(board)
#                 if self.search(temp_board, x+1, y, word):
#                     return True

#         return False

a = Solution()
print(a.exist(
[["F","Y","C","E","N","R","D"],["K","L","N","F","I","N","U"],["A","A","A","R","A","H","R"],["N","D","K","L","P","N","E"],["A","L","A","N","S","A","P"],["O","O","G","O","T","P","N"],["H","P","O","L","A","N","O"]]
,"FRANCE"))

print(a.exist(
[["v","p","y","i","s","w","k","m","d","r","p","u","e","t","j","w","r","o","e","r","z","x","n","c","h","e","n","p","h","f","q","e","x","p","m","p","n","x","d","s","q","v","m","u","q","x","q","h","n","w","b","o","u","o","q","d","s","f","s","b","n","l","g","k","c","u","b","p","t","h","j","j","c","v","d","s","u","w","c","h","s","d","v","o","r","o","u"],["l","v","o","n","i","z","t","u","b","p","w","s","j","d","b","s","h","y","y","b","u","w","d","b","q","g","z","f","z","p","b","l","k","p","y","v","p","t","p","s","i","l","n","r","q","q","m","x","p","k","b","j","g","e","n","w","l","o","d","k","f","e","x","p","u","v","m","l","q","c","d","b","p","s","s","g","j","e","f","a","q","g","l","y","l","y","v"],["y","o","a","k","t","h","i","l","d","f","x","o","w","z","t","x","p","m","r","x","x","y","e","x","o","n","i","n","a","j","k","y","x","m","i","t","t","s","e","w","y","b","m","u","d","g","t","u","u","m","t","r","k","x","o","b","k","y","q","k","h","c","k","h","o","v","a","k","n","e","g","l","h","v","h","m","b","c","g","x","p","z","q","b","z","e","e"],["l","e","u","y","m","y","i","t","n","d","v","x","t","b","f","g","k","c","o","x","d","s","d","c","j","f","s","l","g","y","p","r","d","m","p","r","k","a","m","z","f","h","y","y","k","g","f","u","i","v","r","o","p","x","q","z","e","l","m","k","j","d","d","o","r","v","h","c","v","t","d","a","c","c","b","m","i","i","h","s","f","a","g","u","x","z","v"],["d","m","h","n","v","n","t","m","e","o","t","g","j","p","k","l","t","o","m","g","y","w","p","s","b","r","z","y","r","a","t","u","m","d","i","j","q","b","x","u","r","r","d","a","i","p","n","b","d","a","j","d","y","a","v","a","s","w","y","j","w","t","d","k","w","n","u","m","q","r","j","h","k","m","h","u","b","x","w","g","x","f","j","x","g","e","x"],["a","d","x","j","z","t","o","k","p","c","g","e","s","z","p","a","k","b","j","e","c","g","c","i","f","k","t","f","s","z","e","s","c","e","b","e","x","p","o","o","t","w","u","o","v","j","q","h","k","b","o","o","k","q","y","p","a","r","w","s","r","b","m","v","f","p","z","c","h","p","q","a","l","n","o","j","w","e","q","h","g","g","v","q","x","w","h"],["z","n","e","u","g","h","g","e","m","w","d","q","d","t","i","f","g","v","u","p","s","a","i","b","i","o","y","a","n","u","i","n","k","o","j","q","x","p","u","j","n","a","b","s","v","j","y","b","h","u","t","z","w","b","a","f","r","a","f","f","v","p","u","f","f","d","x","c","u","u","n","k","u","o","e","p","a","e","s","h","y","l","g","v","o","i","c"],["i","k","j","p","f","z","j","m","e","o","k","j","k","e","w","w","a","n","b","r","n","f","l","u","e","x","c","b","n","m","f","x","w","o","m","e","n","x","q","u","n","a","d","y","g","b","u","i","o","x","z","d","d","l","x","j","k","b","m","z","p","r","x","o","f","l","s","v","l","i","r","y","l","w","y","r","x","v","a","o","s","b","r","v","m","r","g"],["y","u","s","y","k","j","x","y","r","i","q","o","t","a","f","u","l","b","s","f","a","n","h","o","g","i","i","d","v","z","k","t","t","c","t","f","o","q","f","f","b","v","v","w","y","a","q","j","d","j","q","d","w","x","u","e","g","c","i","d","d","s","y","y","w","s","e","k","k","l","r","l","h","m","k","h","o","a","s","t","l","j","x","i","g","t","o"],["o","v","w","r","a","q","q","a","n","k","e","z","w","s","r","k","z","f","u","i","w","u","a","p","g","j","m","q","s","h","e","g","e","d","a","e","v","q","f","k","c","l","k","y","d","d","i","e","i","c","m","e","z","p","u","h","y","i","x","s","s","d","z","w","i","z","b","e","r","i","o","v","v","a","v","b","d","e","f","o","i","u","u","j","j","q","q"],["j","b","n","c","t","t","d","p","b","e","s","h","x","c","y","s","y","y","n","z","e","t","g","s","e","a","m","n","l","f","e","x","g","t","z","z","m","e","o","q","i","j","x","f","l","v","z","j","w","m","k","a","g","r","s","m","t","g","z","h","l","d","e","r","x","f","s","l","l","j","b","t","s","z","a","d","w","z","p","s","l","b","s","t","u","m","f"],["o","v","h","x","g","k","d","a","j","i","s","x","t","b","y","o","v","z","o","b","w","n","q","q","a","t","j","w","o","v","d","e","q","k","b","z","x","e","b","i","o","v","f","j","z","g","z","u","f","n","v","d","c","n","u","e","h","f","c","v","a","g","b","t","s","e","u","r","k","v","c","y","q","h","j","r","p","i","m","v","x","j","a","b","x","u","f"],["g","z","k","d","c","q","e","x","k","i","r","e","s","o","g","s","g","n","d","y","d","l","m","a","k","v","c","l","u","z","s","c","a","c","f","e","u","l","b","h","v","u","l","p","i","r","h","r","g","m","r","l","z","d","n","j","a","q","w","x","p","p","z","r","t","f","w","q","s","x","x","o","u","i","d","e","b","n","v","h","z","m","v","z","r","i","k"],["s","a","h","r","r","y","q","j","r","x","f","h","q","e","g","g","y","q","j","d","r","y","a","b","y","n","w","z","g","g","j","a","h","s","r","a","q","i","j","k","h","o","t","x","v","a","d","t","q","p","y","i","n","z","l","n","m","h","m","u","p","y","v","y","q","o","z","h","y","i","r","g","z","m","f","u","m","j","p","d","a","o","n","n","n","a","b"],["b","j","p","v","y","n","s","x","e","j","w","n","h","g","g","n","f","s","t","b","f","e","r","k","e","f","z","t","u","z","u","v","i","m","s","i","z","l","f","f","u","d","s","d","k","y","t","r","t","o","t","y","s","m","k","y","t","l","r","n","m","o","i","w","a","a","e","b","n","m","h","j","r","z","n","b","a","g","v","t","u","q","t","o","c","f","o"],["v","q","h","k","c","x","s","a","x","u","e","b","k","s","i","t","k","j","i","n","j","q","i","e","m","y","x","c","a","c","q","x","u","y","h","y","v","b","y","v","w","f","w","i","x","g","d","h","p","m","v","b","e","d","f","r","e","f","v","e","h","m","e","e","m","l","c","j","p","b","g","n","g","e","v","f","k","y","n","c","m","i","d","r","n","k","k"],["r","p","f","y","z","t","c","d","h","p","f","t","e","i","z","r","q","g","o","w","s","n","j","u","b","t","z","s","i","m","e","a","b","m","a","a","f","c","d","p","t","l","i","y","v","h","r","m","p","g","k","i","v","v","e","w","o","e","r","w","q","x","y","t","j","y","u","r","c","z","g","w","m","o","w","k","x","p","y","n","v","i","v","s","d","z","r"],["t","f","i","r","x","h","s","r","r","q","n","k","v","o","q","r","d","g","p","n","d","e","l","s","c","v","p","w","y","r","n","t","w","x","k","w","f","e","p","y","v","e","i","s","u","a","l","x","g","a","m","j","g","x","e","i","s","t","h","s","k","u","n","j","s","y","h","z","c","w","z","z","c","h","r","w","h","c","u","p","e","g","a","l","g","e","v"],["a","y","c","v","k","z","i","t","t","i","a","s","n","y","t","o","a","a","g","x","j","k","t","y","r","b","y","e","h","f","z","k","f","e","f","p","d","p","l","w","y","l","q","l","m","j","z","m","l","h","l","w","u","e","w","n","g","w","r","p","b","s","z","g","y","g","y","b","w","j","z","w","w","r","j","i","c","k","x","p","u","i","l","o","n","h","d"],["v","e","u","k","f","o","m","o","n","u","m","q","q","v","q","o","r","j","x","c","m","i","z","b","c","h","p","s","w","w","x","r","c","t","e","k","h","q","y","u","k","m","n","d","j","d","r","c","o","r","e","c","b","d","g","f","l","v","z","j","t","w","b","w","p","f","g","y","x","g","v","h","s","i","m","d","l","e","f","b","x","k","e","a","n","k","f"],["a","h","e","k","a","c","n","w","t","s","e","r","p","m","m","y","e","u","l","j","h","r","p","j","o","z","p","o","o","b","v","r","i","b","d","i","d","q","h","y","k","n","p","b","a","c","z","g","y","m","q","i","d","f","r","t","g","i","j","u","j","g","n","r","h","q","b","m","i","i","k","s","w","c","v","w","g","x","c","e","j","s","m","p","z","f","k"],["f","n","w","a","w","c","n","p","k","g","r","y","o","b","j","j","x","n","e","v","t","b","a","x","n","u","m","e","u","r","o","z","h","k","b","f","n","r","v","z","x","o","x","n","p","i","w","p","v","d","m","o","g","m","o","t","h","a","x","d","t","o","c","c","y","g","i","n","x","f","m","w","v","m","l","k","w","i","b","u","n","o","k","t","c","y","p"],["j","a","o","m","w","c","r","y","d","z","i","q","w","p","f","u","k","r","f","x","p","p","y","j","c","o","u","y","r","u","n","c","x","b","r","v","e","i","t","h","h","e","z","f","t","e","b","g","x","g","d","n","w","d","w","a","s","s","y","l","n","l","n","m","p","e","h","v","o","c","e","x","g","d","e","c","i","f","i","h","m","l","u","k","q","t","k"],["i","l","j","t","a","w","j","m","n","n","v","i","c","y","m","b","g","s","g","i","c","l","s","j","x","f","e","j","w","z","u","g","k","f","a","n","d","j","b","r","y","x","b","c","x","o","e","d","g","k","o","i","x","g","t","x","m","z","g","k","y","c","q","l","j","s","y","p","d","b","g","c","y","h","e","v","x","k","b","f","w","p","p","u","x","j","r"],["l","i","z","v","h","c","o","u","n","g","s","c","k","t","i","m","u","s","s","r","r","d","u","x","b","j","m","v","j","x","o","u","g","o","s","p","s","g","l","f","m","d","k","w","y","u","k","u","m","d","m","e","i","g","d","j","s","r","h","b","p","x","x","x","n","p","o","f","v","z","n","k","e","x","g","c","t","r","z","g","w","n","m","g","t","r","r"],["n","i","y","q","x","y","q","u","l","f","k","t","d","j","i","n","n","h","v","s","a","o","r","g","k","e","u","q","z","l","i","p","w","i","f","t","g","x","q","u","d","a","n","i","m","v","x","z","c","s","r","c","h","i","l","r","o","h","k","o","v","u","d","r","e","k","m","n","i","e","h","n","h","u","v","t","p","s","s","t","k","m","v","t","w","i","n"],["l","q","x","b","n","t","e","e","z","q","s","m","y","x","v","l","e","p","i","x","g","c","r","b","n","d","z","i","c","h","v","p","z","u","q","m","n","w","s","p","m","l","b","n","i","x","y","m","o","j","l","x","l","c","y","y","i","x","j","k","h","e","b","g","z","r","t","o","p","l","d","b","y","h","o","g","g","p","s","u","y","f","t","j","i","s","k"],["s","r","t","c","y","z","f","f","y","w","a","n","n","n","s","o","m","z","f","s","h","w","n","e","w","s","x","f","c","p","r","u","h","m","y","f","m","d","m","k","b","m","z","o","a","s","f","o","t","m","g","b","i","v","f","e","q","e","l","s","u","d","n","d","r","n","k","d","r","z","q","u","l","p","j","n","j","q","d","f","c","m","i","m","h","p","q"],["x","t","d","s","p","i","h","u","a","u","f","d","n","g","v","i","t","l","t","j","w","j","m","d","l","y","l","x","i","c","p","f","w","s","z","l","b","g","g","d","d","n","i","q","v","e","a","o","r","t","x","p","c","k","t","p","i","g","m","s","j","b","a","f","w","z","s","z","i","a","e","l","p","m","d","k","q","e","z","j","z","w","z","c","i","u","r"],["t","a","g","l","j","j","l","q","h","l","l","g","t","l","k","g","d","z","j","n","r","p","m","b","p","l","a","t","t","w","m","m","w","s","a","i","e","l","a","l","y","l","u","r","z","g","z","c","f","l","p","x","a","e","y","r","p","a","k","k","w","z","z","u","t","z","c","x","m","d","j","l","q","f","e","p","l","e","t","r","p","j","o","r","p","o","j"],["g","o","v","q","m","u","r","g","o","s","l","n","f","q","y","q","g","d","u","y","p","a","r","i","p","c","w","h","r","k","s","z","a","n","s","o","k","j","u","y","e","f","n","j","x","m","b","e","r","x","e","g","y","x","o","p","a","m","y","t","y","q","t","a","e","l","o","q","w","j","q","a","q","d","l","o","p","o","u","h","m","a","p","m","x","g","d"],["z","u","c","t","t","u","o","t","y","b","k","o","z","t","e","c","l","k","n","b","b","e","v","k","q","v","a","e","v","i","j","u","c","l","n","v","i","d","r","g","g","b","x","g","w","d","i","j","p","x","l","r","b","i","b","t","e","d","z","b","l","j","v","o","w","l","l","e","o","e","n","v","f","m","d","d","r","l","n","h","i","y","y","k","g","z","f"],["m","f","f","n","q","o","j","g","k","w","s","p","k","y","e","h","e","q","k","j","h","v","w","o","g","w","o","s","f","q","x","r","v","c","h","n","q","s","u","d","o","o","u","a","m","y","i","s","q","u","c","z","q","a","o","y","x","e","s","c","u","p","v","p","u","c","f","m","w","z","p","m","n","l","n","b","j","x","u","b","r","y","b","j","y","r","h"],["v","v","z","z","s","r","v","h","l","z","o","x","y","n","p","k","c","a","x","e","m","w","a","n","o","a","o","x","y","f","h","w","d","i","x","v","z","s","e","k","u","t","k","s","g","z","e","l","z","e","r","l","a","r","z","o","r","p","m","r","x","v","p","a","d","n","x","d","h","b","p","d","u","z","x","d","y","c","o","a","g","f","l","g","y","m","v"],["r","c","j","k","z","g","a","b","j","p","y","o","y","z","e","c","w","f","z","b","e","b","p","e","j","w","r","q","w","e","n","n","i","y","z","h","e","b","k","n","q","i","c","r","j","i","t","f","n","u","g","t","y","x","z","h","v","r","z","r","x","m","g","f","m","i","o","q","j","y","g","a","g","k","t","p","s","o","x","f","i","f","z","i","f","y","s"],["a","r","r","u","o","g","c","t","u","k","h","l","w","h","t","y","n","d","r","f","v","f","e","a","p","j","b","y","o","c","s","r","t","l","n","k","r","r","f","m","c","p","z","y","w","s","w","m","v","p","r","s","u","x","s","j","g","w","j","x","a","b","q","t","n","d","f","g","u","l","u","y","a","v","y","y","n","w","k","k","l","d","c","h","a","x","t"],["j","v","c","g","v","g","y","q","v","d","w","b","z","j","y","a","j","t","y","j","j","x","u","v","k","x","a","s","y","x","n","h","u","p","p","p","x","p","f","s","s","d","w","r","m","u","r","x","p","s","h","y","r","b","w","b","a","w","v","a","v","i","j","p","a","y","g","x","p","n","s","h","r","o","b","f","i","u","d","x","o","m","y","h","n","u","l"],["p","q","g","q","l","r","z","c","t","a","i","s","p","v","k","z","m","y","c","s","g","y","x","g","p","j","e","w","y","a","h","n","q","o","d","d","h","d","f","a","f","n","s","u","k","d","v","z","d","x","r","k","y","q","s","n","z","w","j","z","w","r","m","o","h","s","t","q","x","a","q","c","n","k","w","z","p","u","y","t","r","r","f","p","h","x","c"],["i","v","o","h","t","f","w","j","o","o","c","e","l","c","w","n","r","g","l","q","y","f","r","t","z","i","y","o","s","x","t","c","u","j","k","n","o","g","w","e","u","a","i","h","e","e","u","v","m","f","n","k","l","g","f","k","p","f","a","j","c","v","l","y","g","x","l","u","d","j","y","z","l","i","g","p","m","c","m","z","i","c","l","v","i","t","h"],["z","y","j","i","d","f","w","b","l","t","p","i","z","y","i","y","m","r","h","d","f","j","q","g","t","u","u","o","c","n","v","e","l","f","o","o","m","k","s","z","g","h","h","f","h","s","f","t","l","m","x","s","y","p","z","r","j","t","g","n","g","d","r","t","k","g","i","w","s","a","w","y","j","f","f","q","z","l","k","k","z","j","d","z","a","e","r"],["j","z","z","w","f","c","q","y","n","y","i","l","q","k","h","r","t","p","y","k","o","j","w","b","l","h","g","k","h","k","d","s","j","c","q","q","h","g","q","w","e","b","h","x","n","r","q","h","i","o","t","w","a","r","z","n","a","f","z","h","r","d","b","c","h","r","u","o","y","n","m","e","o","w","d","b","p","t","k","x","k","d","v","k","w","v","z"],["w","c","y","d","u","b","g","y","j","y","t","z","w","g","o","c","w","k","g","z","z","z","k","y","l","n","t","x","m","q","w","i","t","v","o","p","y","u","p","h","s","i","j","q","q","x","t","o","h","b","o","i","c","y","g","o","n","b","l","z","u","i","i","p","f","y","e","d","s","v","l","n","g","w","d","w","t","y","n","c","z","b","k","c","z","s","q"],["o","v","d","o","p","n","y","g","s","w","m","w","q","i","j","d","o","f","h","m","a","h","z","c","h","c","o","l","d","g","b","s","d","g","i","v","u","i","b","m","e","o","i","w","y","t","a","m","a","j","a","a","q","a","c","z","e","q","k","i","y","n","a","c","u","k","z","o","s","a","c","y","q","n","u","o","g","w","c","h","h","d","h","a","d","m","z"],["h","c","m","r","d","z","r","f","v","d","e","l","v","g","o","t","x","d","q","n","j","m","q","s","u","t","c","u","y","o","v","h","s","h","z","v","j","s","c","e","w","i","q","t","r","g","n","q","j","f","d","u","r","v","p","n","o","r","j","o","h","h","w","b","o","v","z","z","p","b","e","l","m","w","f","d","e","u","t","n","z","y","j","s","u","y","i"],["i","r","t","z","y","a","v","c","r","s","b","q","h","e","w","v","q","s","c","v","w","y","o","l","z","n","v","t","h","v","b","r","n","x","q","n","x","n","p","o","f","s","h","p","z","d","m","p","y","q","l","w","o","b","i","n","q","f","i","z","c","m","t","p","j","j","f","g","z","u","x","e","p","g","v","o","j","j","f","j","z","s","g","p","u","q","e"],["m","x","n","m","z","z","f","p","i","q","u","q","p","q","p","w","h","v","t","x","h","d","d","s","c","v","y","s","r","q","w","e","n","l","s","p","k","x","g","u","p","a","l","f","s","a","d","c","y","w","z","f","z","c","x","e","a","y","y","r","o","w","x","e","i","p","t","u","o","z","p","e","b","a","l","v","c","o","x","a","k","z","h","m","d","h","s"],["d","f","q","x","v","m","w","b","w","o","w","r","c","x","g","i","y","i","t","w","k","h","v","n","u","u","u","g","a","b","y","d","i","q","c","g","e","z","h","d","n","g","u","r","d","c","a","c","k","v","a","w","f","v","j","z","s","g","h","s","h","h","x","s","z","a","y","d","b","h","g","q","n","c","h","r","e","j","v","q","f","v","p","k","s","a","l"],["k","g","u","e","o","b","c","i","a","e","g","f","f","p","m","v","d","q","e","w","x","o","r","p","v","o","e","h","i","f","s","v","l","m","z","b","p","d","j","r","h","r","w","o","h","k","j","m","b","q","i","y","e","b","p","b","p","u","i","z","b","c","u","o","q","u","s","f","x","b","y","h","v","u","v","e","h","h","q","k","x","a","k","d","b","z","e"],["s","t","m","r","w","o","m","l","e","i","d","l","h","g","j","o","d","f","m","h","o","t","x","y","s","x","i","v","a","i","z","s","d","n","m","c","d","y","p","j","i","s","u","p","a","f","g","g","m","s","n","b","n","n","b","f","m","m","a","n","u","b","h","z","o","t","d","t","t","s","c","b","m","w","r","p","d","x","v","p","r","i","s","e","x","w","j"],["k","i","l","z","e","o","i","d","e","e","j","x","x","b","z","b","o","x","u","d","a","t","y","r","k","i","m","q","g","i","z","s","q","m","t","u","a","b","x","e","f","g","d","f","k","c","g","y","z","c","d","b","v","d","s","h","n","e","x","v","m","y","n","c","k","i","w","m","m","w","s","t","e","v","y","o","z","g","o","y","i","t","z","f","w","t","m"],["m","y","j","h","m","h","x","p","t","f","n","h","r","j","z","n","q","w","l","g","v","u","x","v","e","q","w","k","p","q","y","b","q","i","i","c","r","f","t","n","n","h","u","g","s","u","t","k","s","h","r","q","b","o","l","f","g","k","r","v","a","q","y","s","a","h","w","r","o","s","g","d","b","b","m","v","x","f","g","p","m","z","f","p","p","t","x"],["v","d","q","t","f","g","r","x","g","a","v","a","p","n","g","u","o","j","g","k","g","o","s","y","a","r","f","s","g","y","r","b","b","h","u","i","o","m","h","w","o","d","y","d","s","h","a","j","q","g","t","x","u","l","x","x","e","c","r","k","b","i","n","e","p","k","n","f","w","u","e","m","z","e","s","s","l","s","b","c","y","w","b","v","j","y","u"],["n","a","l","z","b","v","m","i","m","w","v","u","u","r","y","h","t","c","z","l","o","r","o","s","r","k","t","o","v","r","i","i","t","v","j","x","q","v","f","d","u","c","x","o","v","x","x","o","b","w","b","r","p","p","j","j","b","e","x","w","x","i","g","r","d","p","o","w","n","v","b","h","x","a","v","s","z","t","j","a","r","k","u","h","a","d","q"],["d","k","p","a","h","x","i","y","d","a","o","b","n","j","c","u","g","c","p","b","b","k","m","d","c","w","x","l","y","d","d","c","n","s","e","u","s","o","v","x","o","j","y","b","v","a","v","b","e","n","e","h","z","s","m","d","p","k","o","p","p","t","t","c","m","x","y","g","o","v","d","c","h","b","g","c","d","d","f","j","s","k","q","s","c","c","x"]]
,"oojdhcftcgbsbeu"))


