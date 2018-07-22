"""
使用栈来实现队列。
队列是一个先进先出的数据结构，栈则是一个先进后出的数据结构。

当然在 Python 中可以直接使用 Queue 队列，deque 双端队列。

不过还是要学习思考下如何用栈来实现。

用栈实现有两个难点：
栈只能是先进后出。所以要想实现的话务必需要另一个栈。
将当前栈里所有的数据压入另一个栈然后另一个栈里的先进后出就会变成原本的先进先出了。

难点1： 何时将数据压入栈2？
难点2：压入栈2后如果又有新的数据追加进来呢？

第一个问题我想到的是在栈2为空，且栈1数据为两个及以上时。
第二个问题我想到的是如果栈2有数据，则在栈1追加。
这时pop()，直到条件为难点1时清空栈1，压入栈2。


1. push 时，如果两个都没有数据则直接压入栈2.
2. push 时，如果栈2有数据则压入栈1.
3. pop 时，如果栈2有数据则 pop 栈2.
4. pop 栈2之后若栈2为空，则pop栈1，直至空。

测试用例：
https://leetcode.com/problems/implement-queue-using-stacks/

"""

# 要使用3遍以上时再抽象到一个单独的类中。

from GetMinStack import Stack


class Queue:

    def __init__(self):
        self.stack_one = Stack()
        self.stack_two = Stack()

    def push(self, value):
        if self.stack_two.empty():
            self.stack_two.push(value)
        else:
            self.stack_one.push(value)

    def pop(self):

        pop_result = self.stack_two.pop()
        if self.stack_two.empty():
            while 1:
                if self.stack_one.empty():
                    break

                self.stack_two.push(self.stack_one.pop())

        return pop_result

    def peek(self):

        return self.stack_two.get_top()


queue = Queue()

queue.push(1)
queue.push(2)
queue.push(3)

print(queue.pop())
queue.push(4)
print(queue.pop())
print(queue.pop())
print(queue.pop())



