"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.


判断左子树是否与右子树互为镜像。

思路：
遍历左子树，把结果放入队列中。
按照相反的左右遍历右子树，同时让压出队列顶的一项作对比。
不匹配或队列中没有足够的数据都可判为False.

效率 O(n)
beat 100%.

测试地址：
https://leetcode.com/problems/symmetric-tree/description/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        left = root.left
        right = root.right
        
        left_node = [left]
        right_node = [right]
        
        left_node_value = []
        
        while left_node:
            # if left_node:
            _left = left_node.pop()
            if _left:
                left_node_value.append(_left.val)        
            else:
                left_node_value.append(None)

            if _left:
                left_node.append(_left.right)
                left_node.append(_left.left)
        
        left_node_value.reverse()
        
        while right_node:
            _right = right_node.pop()
            
            if left_node_value:
                left_value = left_node_value.pop()
            else:
                return False
            
            if _right:
                if left_value != _right.val:
                    return False
            else:
                if left_value != None:
                    return False

            if _right:
                right_node.append(_right.left)
                right_node.append(_right.right)
        return True
