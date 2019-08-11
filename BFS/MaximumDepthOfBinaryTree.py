"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

找到二叉树的最大深度。

思路：

按层进行广度优先搜索即可。

beat 99% 32ms.

测试地址：
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

"""
class Solution:
    
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 
        
