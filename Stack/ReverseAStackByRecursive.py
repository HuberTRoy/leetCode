"""
只能用递归不能用其他数据结构来逆序一个栈。

可以用另一个新栈的话比较容易。

"""


from GetMinStack import Stack


def reverseStack(stacks):
    new_stack = Stack()

    def helper(stacks):
        if stacks.empty():
            return 

        new_stack.push(stacks.pop())

        helper(stacks)

    helper(stacks)

    return new_stack

# 测试用例。
a = range(10)

b = Stack()

for i in a:
    b.push(i)

# 不用assert了。
print(b)

print(reverseStack(b))


