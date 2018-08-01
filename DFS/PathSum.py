"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

给一颗二叉树和一个值，找到从根到叶的所有路径的和中是否有一个与给定的值相当。

因为只要有一个就可以了，所以直接用深度优先，最差是 O(n)。

测试用例：
https://leetcode.com/problems/path-sum/description/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        def helper(prev, root, sum):
            if prev + root.val == sum:
                if not root.left and not root.right:
                    return True
                
            if root.left:
                if helper(prev + root.val, root.left, sum):
                    return True
            
            if root.right:
                if helper(prev + root.val, root.right, sum):
                    return True
            
            return False
    
        return helper(0, root, sum)
