"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]


迭代出二叉树层级别的节点值。
直接用 BFS 即可.

下面是一个用双端列表的迭代方式实现。

用递归更好写一些。

测试地址：
https://leetcode.com/problems/binary-tree-level-order-traversal/description/

beat 92% 28ms.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []
        
        temp = deque([root])
        next_temp = deque()
        _result = []
        while 1:
            if temp:
                node = temp.popleft()
                _result.append(node.val)
                if node.left:
                    next_temp.append(node.left)
                    
                if node.right:
                    next_temp.append(node.right)
            else:
                result.append(_result)
                _result = []
                temp = next_temp
                next_temp = deque()
            
            if not temp and not next_temp:
                if _result:
                    result.append(_result)
                return result
            
        
