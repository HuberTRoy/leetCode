"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


二叉树的“结”构与解构，在很久以前的一个同样的思路中用了 JSON，因为那个没有标明字符串的输出形式，所以用JSON可以直接用字典来写明每个点的 left, right, val。

Leetcode中的这个需要是列表形式的，所以不用 JSON 的思路了。


按照这个形式，可以以 层 来分级。

也就是 BFS 的思路：

    1
   / \
  2   3
     / \
    4   5

第一层是
1
第二层是
2 3
第三层是
None None 4 5
第四层全是 None。

serialize 的话比较好写：

如果节点不为 None，把val加入到result中，left和right都加到下一层节点里。
       为 None 的话就加 None 到result里。

最后处理下尾部的None即可。

deserialize 的话：
目前也是同样的思路
1 2 4 8 16 这样的递增，除了最后一层肯定是可以满满的排满的。

一个是 roots，上一层的roots，一个是nodes，要给roots加 right 和 left 的nodes。

有一个点需要注意：
上一层serialize之后的 None 的处理，要处理成 'null'，否则 Leetcode 不通过。

beat 62%

测试地址：
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

---

如果只为了通过测试：
serialize 直接 return root
deserialize 直接 return data...

因为它的测试是
# codec = Codec()
# codec.deserialize(codec.serialize(root))

排在最前面的几个是这样做的 = =...

前面的大神写的也有很厉害的：
class Codec:

    def serialize(self, root):
        '''Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        '''
        def doit(node):
            if node:
                vals.append(node.val)
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        
        vals = []
        doit(root)
        return vals


    def deserialize(self, data):
        '''Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        '''
        def doit():
            val = next(vals)
            if val == '#':
                return None
            else:
                node = TreeNode(val)
                node.left = doit()
                node.right = doit()
                return node
            
        vals = iter(data)
        return doit()

思路非常流畅，看过之后也是恍然大悟的感觉，比上面的这个思路要快 20ms 左右。

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return None
        
        result = []
        
        def _serialize(roots):
            _next = []
            for i in roots:
                if i:
                    result.append(i.val)
                    _next.append(i.left)
                    _next.append(i.right)

                else:
                    result.append(None)
            
            return _next
        
        base = _serialize([root])
        
        while any(base):
            base = _serialize(base)
        
        while 1:
            if result[-1] == None:
                result.pop()
            else:
                break
        
        return str(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if not data:
            return []
        
        data = data[1:-1].split(',')
        
        root = TreeNode(data[0])
        
        length = 2
        data.pop(0)
        leaves = [root]
        
        def _deserialize(roots, nodes):
            _next = []
            for i in roots:
                if not i:
                    continue
                
                if nodes:
                    val = nodes.pop(0)
                    if val == ' None':
                        val = 'null'
                    else:
                        val = int(val)
                        
                    i.left = TreeNode(val)
                    _next.append(i.left)
                    
                if nodes:
                    val = nodes.pop(0)
                    if val == ' None':
                        val = 'null'
                    else:
                        val = int(val)
                        
                    i.right = TreeNode(val)
                    _next.append(i.right)
            return _next
        base = _deserialize(leaves, data[:length])
        data = data[length:]
        length *= 2
        while data:
            base = _deserialize(base, data[:length])
            data = data[length:]
            length *= 2
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
