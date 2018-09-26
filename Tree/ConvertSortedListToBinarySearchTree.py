"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5


 这次给的是一个排序过的链表，链表和数组有所不同，链表的话无法使用索引，或者说使用索引所需要的时间是 O(n) 并非  O(1)。
 当然可以把链表转换成一个数组然后按照数组的方法去解，这样不会出错，时间复杂度上也是同样的，就是空间复杂度上要高一些。
 
 我自己的话没想到其他的思路：
 在Discuss里看到一个 Java 的思路，觉得非常棒：

 前面我们分析过这其实就是个中序遍历的结果，按照这个思路，如果能按照中序遍历逆推回去，即可得到一颗完整的高度平衡的二叉搜索树。

 这个思路也是这样的，在做二叉树的中序遍历时用递归一般这样写：
 ```
 if root.left:
    recursive(root.left)
 root.val
 if root.right:
    recursive(root.right)
 
 ```
 如果我们能找到left的头，并一直持续到right的尾，即可得到一颗二叉搜索树，这棵树可能并不会与原来的相同。

 如：
  中序结果是：
  [-1, 1, 2, 3]
  这颗树可能是：
       1
    /   \
 -1      2
          \
           3

也可以是：
         2
       /  \
     1     3
   /
-1
 那就按原来的数组中的方法：
 如果要从中序遍历的结果生成二叉树，首先需要获取的是 mid 中位，找到它的根。剩下的也是不断找到根。
 [-10,-3,0,5,9]
 1. 第一步先找一下链表的长度。
 2. 第二步则给函数说左有几个，右有几个。
 
 左边有几个的话很简单：
 直接 length // 2即可，地板除的话会舍弃。 比如如果有4个数据。 4//2之后左边的还剩下 两个 [0,1]

 右边的话：
 需要原来的长度 减去左边的长度 再减去 这个的根得知。

 这样不断递归至 size 为 0 即为左子树的头，与右子树的尾。
 [-10,-3,0,5,9]

 1.  size = 5
     left = 5//2 = 2  [-10,-3]
     right = 5 - left - 1 = 5 - 2 - 1 = 2 [5, 9]

 2.  size = 1.left = 2
     left = 2//1 = 1 [-10]
     right = 2 - left - 1 = 2 - 1 -1 = 0 []

 3.  size = 2.left = 1
     left = 1 // 2 = 0
     right = 1 - 0 - 1 = 0
 这一步开始返回链表的第一个值 -10 作为 2 里左节点的val.之后返回到2
 2. 则把自己的节点值覆盖为链表中下一个值 -3。 之后返回到1.
 1. 则把自己的节点值覆盖为链表中的下一个值 0。 之后开始right的递归。同样的操作。
 ---
 4.  size = 1.right = 2
     left = 2//1 = 1 [5]
     right = 2 - left - 1 = 2 -1 -1 =0 []
 5.  size = 4.left = 1
     left = 1 // 2 = 0 []
     right = 1- 0 -1 = 0 []
 ...

关键词：
中序遍历，左右子树节点的个数。

beat 99%

测试地址:
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        size = 0
        
        self.c_head = head
        
        while head:
            size += 1
            head = head.next
        
        def makeBSTByInorder(size):
            if not size:
                return 
            
            root = TreeNode(None)
            
            root.left = makeBSTByInorder(size//2)
            root.val = self.c_head.val
            self.c_head = self.c_head.next
            root.right = makeBSTByInorder(size-size//2-1)
            
            return root
        
        return makeBSTByInorder(size)
