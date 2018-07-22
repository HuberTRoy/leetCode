"""
设计一个可以 Get Min的栈结构。

栈是一个先进后出的数据结构。

要设计这样的一个需要两个栈来完成，一个栈用于正常的存储，另一个用于只存储最小的。

这样push/pop get min都是O(1) 时间完成。

非常基础。

其实在Python中可以用类直接写min属性，不过限定了只能用栈了。

"""

# deque 是一个Python实现的双端队列。
# 由底层C代码实现。
# 使用它可以保证在左右两端进行添加和删除操作时间都是O(1)。
from collections import deque

testStack = range(10)


class Stack:
    """
        一个先进后出的栈。
    """
    def __init__(self):
        """
            这里用实例对象。
        """
        self.stored = deque()

    def __repr__(self):
        # 3.6 +
        return f'<{self.stored}>'

    def push(self, value):
        self.stored.append(value)

    def pop(self):
        return self.stored.pop()

    def get_top(self):
        """
            查看栈顶的数据但不压出。
        """
        return self.stored[-1]

    def empty(self):
        if self.stored:
            return False
        return True


class MinStack(Stack):
    """
        一个可以在O(1)时间内获取出最小值的栈。
    """
    def __init__(self):
        super().__init__()

        self.minStack = Stack()

    def push(self, value):
        super().push(value)
        if self.minStack.empty():
            self.minStack.push(value)
        else:
            if self.minStack.get_top() <= value:
                self.minStack.push(self.minStack.get_top())
            else:
                self.minStack.push(value)

    def pop(self):
        super().pop()
        self.minStack.pop()

    def get_min(self):
        """
            返回栈顶但不压出。
        """
        return self.minStack.get_top()


a = Stack()
for i in testStack:
    a.push(i)

print(a)
a.pop()
print(a)

a = MinStack()

a.push(1)
print(a.get_min()) # 1
a.push(2) 
print(a.get_min()) # 1
a.push(0)
print(a.get_min()) # 0
a.pop()
print(a.get_min()) # 1

