"""
包括生成树，二叉搜索树的前后中遍历。

二叉搜索树在比较优质的情况下搜索和插入时间都是 O(logn) 的。在极端情况下会退化为链表 O(n)。
将无序的链表塞进二叉搜索树里，按左根右中序遍历出来就是排序好的有序链表。


"""

# 生成树操作。

class TreeNode(object):

    def __init__(self , val, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right


class binarySearchTree(object):
    """
        二叉搜索树，
        它的性质是左边节点都小于根节点，右边的都大于根节点。
        而且一般来说它是不存在重复元素的。

    """

    def __init__(self, root):
        if isinstance(root, TreeNode):
            print(1)
            self.root = root
        else:
            self.root = TreeNode(root)

    def add(self, value):
        # 从顶点开始遍历，找寻其合适的位置。
        root = self.root
        while 1:
            if root.val < value:
                if root.right is None:
                    if self.search(value):
                        break
                    root.right = TreeNode(value)
                    break
                else:
                    root = root.right
                    continue

            if root.val > value:
                if root.left is None:
                    if self.search(value):
                        break
                    root.left = TreeNode(value)
                    break
                else:
                    root = root.left
                    continue

            if root.val == value:
                break

    def search(self, value):
        # 查找一个值是否存在于这颗树中。
        return self._search(self.root, value)

    def _search(self, root, value):
        if root.val == value:
            return True

        if root.right:
            if root.val < value:
                return self._search(root.right, value)

        if root.left:
            if root.val > value:
                return self._search(root.left, value)

        return False

    def delete(self):
        pass

    def prevPrint(self):
        # 根左右
        nodes = [self.root]
        result = []
        while 1:
            if not nodes:
                return result
            node = nodes.pop()
            result.append(node.val)

            if node.right:
                nodes.append(node.right)

            if node.left:
                nodes.append(node.left)

    def _middlePrint(self, root, result):
        if root.left:
            self._middlePrint(root.left, result)

        result.append(root.val)

        if root.right:
            self._middlePrint(root.right,result)

    def middlePrint(self):
        # 左根右
        result = []
        self._middlePrint(self.root, result)

        return result

    def _suffPrint(self, root, result):
        if root.left:
            self._suffPrint(root.left, result)

        if root.right:
            self._suffPrint(root.right,result)
        
        result.append(root.val)

    def suffPrint(self):
        # 左右根
        result = []
        self._suffPrint(self.root, result)

        return result


oneTree = binarySearchTree(5)

for i in range(-5, 10):
    oneTree.add(i)

print(oneTree.middlePrint())
print(oneTree.suffPrint())






