"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

返回最底层最左边的一个节点的值。

思路：

使用广度优先算法：
1. 也可以用深度优先算法，不过广度优先的话所需代码更少，更好理解。
2. 广度优先：
        1             遍历1
       / \
      2   3           遍历 2 3
     /   / \
    4   5   6         遍历 4 5 6
       /
      7               遍历 7

   深度优先：
        1             遍历1
       / \
      2   3           遍历2 -> 4
     /   / \
    4   5   6         遍历 3 -> 5 -> 7，3 -> 6
       /
      7

3. 广度优先运用在此处是以「层」为概念的，遍历完一层，再遍历一层。
   由于是返回最左边，所以从右向左。
   用两个列表，一个存放本层所有节点，一个存放本层所有节点的下层所有节点。
   遍历完本层后合并存放下层的列表，如果没有节点则返回结果。
   遍历本层时遵从 right to left. 有值就保存为结果。

测试用例：

https://leetcode.com/problems/find-bottom-left-tree-value/description/

40ms beat 74%.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        waiting_for_access = [root]
        new_waiting_for_access = []
        result = root.val
        
        while 1:
            while waiting_for_access:
                node = waiting_for_access.pop()
                
                if node.right:
                    new_waiting_for_access.append(node.right)
                    result = node.right.val
                if node.left:
                    new_waiting_for_access.append(node.left)
                    result = node.left.val
            if not new_waiting_for_access:
                return result
            waiting_for_access.extend(new_waiting_for_access[::-1])
            new_waiting_for_access = []
