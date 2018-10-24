"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself 
             according to the LCA definition.
Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.


给定一颗 BST，找到两个子节点的最小公共祖先。
用普通的树的方法也是可以的，不过可以做个剪枝优化。

因为 BST 我们知道每个节点的左右子节点的范围。

1. 如果处于 root 左右，那么直接返回即可。
2. 如果都小于，那么去找左子树。
3. 如果都大，那么去找右子树。

在寻找过程中，
4. 只要有一个命中了，那么直接返回当前节点即可。因为剩下的那个节点只有可能在它的子树中，如果不在它的子树中也不会执行到这一步。

beat 99%

测试地址：
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

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

        if p.val == root.val or q.val == root.val:
            return root
        
        if p.val < root.val and q.val > root.val:
            return root
        elif p.val > root.val and q.val < root.val:
            return root
        
        if p.val > root.val and q.val > root.val:
            
            return self.lowestCommonAncestor(root.right, p, q)
        
        else:
            return self.lowestCommonAncestor(root.left, p, q)
        