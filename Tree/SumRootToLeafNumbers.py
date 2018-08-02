"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

给一只二叉树，输出所有从根到叶路径的总和。
O(n) 遍历。 字符串 -> 数字 -> 求和。

测试用例：
https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

24 ms beat 75%

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        result = []
        if not root:
            return 0
        
        def helper(root, string):
            if not root.left and not root.right:
                result.append(int(string+str(root.val)))
                return 
            
            if root.left:
                helper(root.left, string+str(root.val))

            if root.right:
                helper(root.right, string+str(root.val))
        helper(root, '')
        return sum(result)
