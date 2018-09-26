"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5


 给定一个已排序过的数组，将它转换为一颗高度平衡的二叉搜索树。
 
 也就是两颗子树的高度差不超过1。

 因为是排序的数组，相对来说也异常简单，可以将它看做是一颗二叉搜索树中序遍历后的结果。
 按照此结果转换回去就是了。


 每次都二分：

 [-10,-3,0,5,9]
        mid
                 5//2 = 2 mid = 2
            0
[-10, -3]      [5, 9]   2 // 2 = 1 mid = 1
    ↓             ↓
    -3            9
[-10]  []     [5]    []

为空则不进行下面的操作。

beat 98%

测试地址：
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        def makeBinarySearchTree(nums):
            mid = len(nums) // 2

            root = TreeNode(nums[mid])
            left = nums[:mid]
            right = nums[mid+1:]

            if left:
                root.left = makeBinarySearchTree(left)
            if right:
                root.right = makeBinarySearchTree(right)    
            
            return root
        
        root = makeBinarySearchTree(nums)
        return root

