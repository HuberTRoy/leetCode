"""
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following operations:

CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains complete, and returns the value of the parent of the inserted TreeNode;
CBTInserter.get_root() will return the head node of the tree.
 

Example 1:

Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]
Example 2:

Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]
 

Note:

The initial given tree is complete and contains between 1 and 1000 nodes.
CBTInserter.insert is called at most 10000 times per test case.
Every value of a given or inserted node is between 0 and 5000.

一只完全二叉树是除最后一层外，每一层的节点都是满的，而且尽量靠左。

实现一个 CBTInserter，这个东西会初始化一颗二叉树，并支持以下操作：
1. CBTInserter(TreeNode root) 初始化这个结构。
2. CBTInserter.insert (int v) 会插入v到这个结构中，并且返回它的父节点。
3. CBTInserter.get_root() 返回树的根节点。

思路：
初始化思路：

根据 BFS 的路线：
    一个root，一个当前节点的集合，一个下一层节点的集合。
    初始化问题，初始化时只给了一颗完整的树，要自己找出当前节点的集合和下一层节点的集合，
    直接用了 BFS 层级遍历然后依次调用 insert 了。
    这样初始化是 O（n）之后都是 O（1）。


insert 思路：
    使用 list + reverse 代替的先进先出queue了。
    选当前节点最先插入的一个，然后判断 left 和 right，插入right后把它从当前层里删除，
    若当前层不存在节点就替换为_next_nodes。

    这样插入是 O(1) 的。

get_root：
    return self.root。

contest，还没有beat。

run time 52ms.

测试地址：
https://leetcode.com/contest/weekly-contest-105/problems/complete-binary-tree-inserter/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self._root = root
        self.root = TreeNode(root.val)
        self.current_node = [self.root]
        self._next_node = []
        self.get_init_nodes()

    def get_init_nodes(self):
        result = []
        
        current_nodes = [self._root]
        _next_node = []
        
        while current_nodes or _next_node:
            for i in current_nodes:
                if i.left:
                    result.append(i.left.val)
                    _next_node.append(i.left)
        
                if i.right:
                    result.append(i.right.val)
                    _next_node.append(i.right)
            
            current_nodes = _next_node
            _next_node = []

        for i in result:
            self.insert(i)
        
    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        
        node = self.current_node[-1]
        if not node.left:
            node.left = TreeNode(v)
            parent = node
            self._next_node.append(node.left)

        elif not node.right:
            node.right = TreeNode(v)
            parent = node
            self._next_node.append(node.right)
            self.current_node.pop()
            
        if not self.current_node:
            self._next_node.reverse()
            self.current_node = self._next_node
            self._next_node = []
        
        return parent.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
