"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

给一颗二叉树，返回从右边看能看到的第一个。

思路BFS，返回最后的一个即可。

beat 94%。

测试地址：
https://leetcode.com/problems/binary-tree-right-side-view/description/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        result = [root.val]
        
        current = [root]
        next_nodes = []
        
        while current or next_nodes:
            for i in current:
                if i.left:
                    next_nodes.append(i.left)
                if i.right:
                    next_nodes.append(i.right)
            if next_nodes:

                result.append(next_nodes[-1].val)
            current = next_nodes
            next_nodes = []
        
        return result
        