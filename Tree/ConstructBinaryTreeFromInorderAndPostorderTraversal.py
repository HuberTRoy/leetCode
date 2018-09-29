"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7


这个的思路与之前的大同小异。

inorder:

左 根 右

postorder:

左 右 根

postorder 中找根，
inorder 中找左右。

下面是一个递归实现。

left_inorder
left_postorder
和
right_inorder
right_postorder
的处理。

一开始全部中规中矩的定义清晰，然后root.left, root.right。

完成所有测试大概需要 200ms 左右。

后面发现并不需要：

postoder 是 左 右 根。
根完了就是右，所以直接可以postorder.pop()，然后先进行 right 的查找，相当于 right_postorder 带了一些另一颗树的东西，不过无关紧要。

都是些优化的步骤。 

测试地址：
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        def makeTree(inorder, 
                     postorder):
            if not inorder or not postorder:
                return None
            
            root = TreeNode(postorder.pop())
            index = inorder.index(root.val)
            
            # left_inorder = inorder[:inorder.index(root.val)]
            # left_postorder = postorder[:len(left_inorder)]
            
            # right_inorder = inorder[len(left_inorder)+1:]
            # right_postorder = postorder[len(left_postorder):-1]
            
            
            root.right = makeTree(inorder[index+1:], postorder)
            root.left = makeTree(inorder[:index], postorder)
            
            return root
        
        return makeTree(inorder, postorder)
