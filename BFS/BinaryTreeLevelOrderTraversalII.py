"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]


无难度..做了1的话直接把返回结果倒置即可。

beat 94%
28ms 

测试地址：
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
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
                return result[::-1]
