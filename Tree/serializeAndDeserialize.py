"""
Given the root to a binary tree, implement serialize(root), 
which serializes the tree into a string, and deserialize(s), 
which deserializes the string back into the tree.

给定一颗二叉树，
serialize(root) 方法可以将此树弄成字符串，
deserialize()则可以将转换成的字符串还原为树。

这个要求让我想到翻译的一章Json，里有一个序列化自定义对象。

序列化的时候，弄出它的 __class__，__dict__。

在这里，root 是字符串，不用做特殊处理，left和right要么是None，要么是Node。

但在Python的魔法方法中，有一种更好用的方式，思路还是Json，也要用到Json。

因为是要转换为字符串，直接定义 __str__方法，返回 
"{{'val': {}, 'left': {}, 'right': {}}}".format(self.val, self.left, self.right)"
这样只要调用一次 str，剩下的如果left和right是Node，则也会调用同样的 __str__方法，最终形成一个嵌套字典。
标准的Json，要转换下引号。

在解包的时候，用Json处理一下，然后循环，如果left/right是字典，就写成Node，直到left或right是None。
这一步用递归比较容易。同时也要更改下Node，在构造left的时候，如果是字典，就要用Node封装，如果是Node或者None，则不管。


遇到的问题：
在转换为Json的过程中，
```
    def _serialize(self):

        return {"val": self.val, "left": self.left or self.left._serialize(), "right": self.right or self.right._serialize()}

    def serialize(self):
        # 会提示不是可序列化的目标。
        # self._serialize()
        # 返回的是个Dict.
        return json.dumps(self._serialize())
```
Ok, a silly wrong. The statement `or` will return the first if the first is True or return the second when the first is False.
So, if self.left is not None it will return <class.__main__.Node ....> but not self.left._serialize().
The key of the question is I rewrite the `__str__` and `__repr__`，
so it will show the same output of `_serialize()` when I printed it...

To solve it just replace `or` to `and`. `and` statement will return the second when the first is True.

"""
import json


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        if isinstance(left, Node) or left == None:
            self.left = left
        else:
            self.left = self.construct(left)

        if isinstance(right, Node) or right == None:
            self.right = right
        else:
            self.right = self.construct(right)

    def __str__(self):

        return '{{"val": "{}", "left": {}, "right": {}}}'.format(self.val, self.left, self.right)

    def __repr__(self):

        return str(self)

    def _serialize(self):

        return {"val": self.val, "left": self.left and self.left._serialize(), "right": self.right and self.right._serialize()}

    def construct(self, constructDict):
        return Node(**constructDict)

    def serialize(self):

        return json.dumps(self._serialize())


def deserialize(string):
    constructDict = json.loads(string)

    def construct(treeDict):

        return Node(treeDict.get('val'), treeDict.get('left'), treeDict.get('right'))

    return construct(constructDict)


# test
node = Node('root', Node('left', Node('left.left')), Node('right'))
print(node.serialize())
assert deserialize(node.serialize()).left.left.val == 'left.left'
