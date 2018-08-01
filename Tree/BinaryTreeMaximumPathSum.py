"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

给定一棵树：
找到一条路径，该路径所经过的节点之和是此树中最大的。

测试用例：
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
"""


"""
第一版：
此版本实现思路：
从底到顶，每次都会比对是否是最大值。
此版本的问题是输出的不是最大的路径而是所有节点中最大的相加和。
比如此树：
        5
       / \
      4   8
     /  /  \
   11  13   4
  / \        \
 7   2        1

从全部相加得出的是 55，而测试要求是48。
测试中所定义的*路径*是一条连通的线，可以 7 -> 11 -> 2，但不能 7 -> 11 -> 2 -> 4

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        '''
        :type root: TreeNode
        :rtype: int
        '''
        self.maxes = -float('inf')
        
        def helper(root):
            myValue = root.val
            
            if not root.left and not root.right:
                self.maxes = myValue if myValue > self.maxes else self.maxes
                return myValue
            
            if root.left:
                value = helper(root.left)
                if value > 0:
                    myValue += value
                if myValue < value:
                    self.maxes = value if value > self.maxes else self.maxes
                else:
                    self.maxes = myValue if myValue > self.maxes else self.maxes
            
            if root.right:
                value = helper(root.right)

                
                if value > 0:
                    myValue += value
                    
                if myValue < value:
                    self.maxes = value if value > self.maxes else self.maxes
                else:
                    self.maxes = myValue if myValue > self.maxes else self.maxes
            return myValue
    
        helper(root)
        
        return self.maxes

"""
"""
Passed! And Beat 94.66%.
第二版思路：

每一个点有两种决策：

1. 以此点为中转站的 left to right 的值，此值确定的是以此点为轴心的局部范围内是否有最大值。
   1
 /  \
2    3

2. 向上返回的值。此值确定的是以父节点为轴心的局部范围是否有最大值。
例子：
   10
 /   \
11   -20
     /  \
    15   5

在-20这个点它要向上返回的值是 15 -> -20 这一条线。
以-20为轴心的值是 15 -> -20 -> 5

1.中要进行的判断是，left + val + right, left + val, right + val, val 和 已记录的最大值哪个最大。4
2.要一直返回，返回之后的判断与1一致，2要返回的内容是 val, left + val和right + val 最大的那个。
最后叶节点比对下最大值直接返回即可。
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        '''
        :type root: TreeNode
        :rtype: int
        '''
        self.maxes = -float('inf')
        
        def helper(root):
            myValue = root.val
            if not root.left and not root.right:
                self.maxes = myValue if myValue > self.maxes else self.maxes
                return myValue
            
            valueLeft, valueRight = -float('inf'), -float('inf')
            
            if root.left:
                valueLeft = helper(root.left)
            
            if root.right:
                valueRight = helper(root.right)
            
            # judge left to right is max or not.
            
            self.maxes = max([myValue + valueLeft, myValue + valueRight, myValue + valueLeft + valueRight, myValue, self.maxes])
            
            # return to parent
            return max(myValue + max(valueLeft, valueRight), myValue)
        
        helper(root)
        return self.maxes

