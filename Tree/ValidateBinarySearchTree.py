"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.


验证是否为有效的 二叉搜索树。

二叉搜索树的定义是：
右边的小于父节点，左边的大于父节点，对于每一个节点都是同样的规则。

思路：
直接中序遍历，中序遍历的二叉搜索树会以排序好的形式返回，返回的同时判断是否比上一个要大，若小于或相等，那么就表示这不是一颗二叉搜索树。

递归..O(n) 时间复杂度。

测试链接：
https://leetcode.com/problems/validate-binary-search-tree/description/

beat 100% 36ms.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
    
        self.prev = -float('inf')
            
        def inOrderTraversal(root):

            if root.left:
                if inOrderTraversal(root.left) == -1:
                    return -1

            if root.val <= self.prev:
                return -1
            
            self.prev = root.val

            if root.right:
                if inOrderTraversal(root.right) == -1:
                    return -1
        if inOrderTraversal(root) == -1:
            return False
        return True
