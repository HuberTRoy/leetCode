"""
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

 

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
 

Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.

根据二叉树的 前序和后序遍历，返回一颗完整的二叉树。

不唯一，返回随便一个即可。

思路：
1. 二叉树的前序是 根左右。
2. 二叉树的后序是 左右根。

在前序中确定 根 ，然后在后序中找左右子树。

pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]

总根是 1

1的左右其中一个是 2，就当它是左子树好了，因为是 根 左右 所以假设的话就先假设为左子树，如果只有一边的话，左右其实无所谓。

   1
 /
2

然后在 post 中找属于 2 这个子树的节点。
找到 4 5 2，那么剩下的 6 7 3 就是与之相对的 1 的右子树了。

把 pre 分成 [2, 4, 5] [3, 6, 7]
   post 分为 [4, 5, 2] [6, 7 ,3]

这样 作为1的左右两颗子树已经出来了。
pre[left] 和 pre[right] 的 0 分别为 左右两棵子树的根。

之后就是分别把左右两边的这两个代替原来的 pre post，根也同样代替，然后递归直到没有即可。

测试链接：
https://leetcode.com/contest/weekly-contest-98/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

beat 50% 40ms.

这应该是自己的极限了。
4道题 一个半小时做 3 道题，1 easy 2 medium 0 hard.


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        
        def getLeftAndRight(pre, post):            
            # no more node.
            if not pre:
                return None
            
            # Get the index of the left root.
            index = post.index(pre[0])
            
            # post left tree
            val_children = post[:index+1]
            
            # post right tree
            val_brother = post[index+1:-1]
            
            # pre left tree
            # Get the left tree pre list 
            # if left tree post list contains 3 elements
            # then we will get equal in pre list.
            t = len(val_children)
            pre_val_children = pre[:t]
            
            # there is right tree.
            # The elements are the rest of pre list.
            pre_val_brother = pre[t:]

            left = pre[0]
            
            right = val_brother[-1] if val_brother else None

            # left, right, pre, post
            return (left, right, pre_val_children, val_children, pre_val_brother, val_brother)
            
        def construct(root, pre, post):
            x = getLeftAndRight(pre[1:], post)
            if root and x:
                if x[0] is not None:
                    root.left = TreeNode(x[0])
                if x[1] is not None:
                    root.right = TreeNode(x[1])

                if root.left:
                    construct(root.left, x[2], x[3])

                if root.right:
                    construct(root.right, x[4], x[5])
            
        allRoot = TreeNode(pre[0])
        construct(allRoot, pre, post)
        
        return allRoot
        
