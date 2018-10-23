"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.
Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.


给一颗二叉树，找出某两个子节点的最小公共祖先。
思路：

用递归：
   1. 用递归找到符合条件的子节点。 找到后的子节点会返回为一个具体的 TreeNode，找不到的话则是 None。
   2. 之后判断 是不是两个都找到了，最先知道两个都找到的点即为最小公共祖先。
   3. q为p子节点，或p为q子节点的情况：
         由于是唯一的，所以出现这种情况一定有一边返回是None，所以返回不是None的一边即可。

普通的二叉树要递归的话是这样：

# do something

if root.right:
    right = recursive(root.right)
if root.left:
    left = recursive(root.left)

# do something

按照上面的思路加工一下即可。

测试地址：
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root.val == p.val or root.val == q.val:
            return root
        
        right = None
        left = None
        
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        
        if right and left:
            return root
        
        if right:
            return right
        
        if left:
            return left
