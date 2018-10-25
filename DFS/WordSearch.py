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


"""
2018/10/25

刷 Word Search II 时重新回顾了一下。

用这次刷II的方法重新测试，
beat
84%

测试地址：
https://leetcode.com/problems/word-search/description/

练习是有效果的。 ^_^

"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def find(board, x, y, word):
            if not word:
                return True
            
             
            if board[y][x] == word[0]:
                raw = board[y][x]
                board[y][x] = 0
                if len(word) == 1:
                    board[y][x] = raw
                    return True
            else:
                return False
                
            # up
            if y-1 >= 0 and board[y-1][x] == word[1]:
                if find(board, x, y-1, word[1:]):
                    board[y][x] = raw
                    return True
            # down
            if y+1 < len(board) and board[y+1][x] == word[1]:
                if find(board, x, y+1, word[1:]):
                    board[y][x] = raw
                    return True
                
            # left
            if x-1 >= 0 and board[y][x-1] == word[1]:
                if find(board, x-1, y, word[1:]):
                    board[y][x] = raw
                    return True
                
            # right
            if x+1 < len(board[0]) and board[y][x+1] == word[1]:
                if find(board, x+1, y, word[1:]):
                    board[y][x] = raw
                    return True
                
            board[y][x] = raw      
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if find(board, j, i, word):
                        return True

        return False

