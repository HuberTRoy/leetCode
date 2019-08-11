"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

取出二叉搜索树中第 k 小的数据。
就这一条来看用 inorder 即可。

进阶条件是如果这颗树经常进行 插入/删除操作如何去优化它呢？
以下是思考：

一颗相对平衡的 BST 的优势在于：可以在 O(log n) 时间内查找/插入/删除某些数据。

就查找这一个条件来说构建一个 排序过的数组是可以达到 O(log n) 的需求的。 但是插入和删除对于数组来说都是 O（n）级别的。

Discuss里有讨论说可以记录 第 k ，第 k-1 个。若插入的比 k 大那么不变，否则k就变为 k-1，然后在重新计算 k - 1。这样也是部分优化。
待解决。

非进阶的：
beat 78% 48ms。

测试地址：
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/



"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def find_data(self, root: TreeNode):

        if root is None:
            return
        Solution.find_data(self,root.left)
        self.data.append(root.val)
        Solution.find_data(self,root.right)
        return
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.data = []
        Solution.find_data(self, root)
        return self.data[k-1]
