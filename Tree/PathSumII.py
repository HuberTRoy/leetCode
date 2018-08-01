"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

PathSum 的进阶版，输出所有符合条件的路径。所以这里直接用遍历，有负数加上不是二叉搜索树应该没太多需要优化的地方。

测试用例：
https://leetcode.com/problems/path-sum-ii/description/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []
        
        def helper(prev, root, sum, path):
            if prev + root.val == sum:
                if not root.left and not root.right:
                    result.append(list(map(int, path.split(' ')[1:]))+[root.val])
                    return True
                
            if root.left:
                helper(prev + root.val, root.left, sum, path=path+" "+str(root.val))
                    # return True
            
            if root.right:
                helper(prev + root.val, root.right, sum, path=path+" "+str(root.val))
            
            return False
        
        helper(0, root, sum, "")  
        
        return result
