"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]


与 Binary tree order traversal 非常相似，不同的是这个是一层 左->右，一层 右->左。

同样的思路，加一个标记，若是RIGHT的层就倒过来。

beat 99.94%.
24ms

测试地址：
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
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
        LEFT = True
        RIGHT = False
        currentDirection = LEFT
        
        while 1:
            if temp:
                node = temp.popleft()
                _result.append(node.val)
                

                if node.left:
                    next_temp.append(node.left)
                    
                if node.right:
                    next_temp.append(node.right)


            else:
                if currentDirection == LEFT:
                    result.append(_result)
                    currentDirection = RIGHT
                else:
                    _result.reverse()
                    result.append(_result)
                    currentDirection = LEFT
                _result = []
                temp = next_temp
                next_temp = deque()

            
            if not temp and not next_temp:
                if _result:
                    if currentDirection == LEFT:
                        result.append(_result)
                        currentDirection = RIGHT
                    else:
                        _result.reverse()
                        result.append(_result)

                return result
