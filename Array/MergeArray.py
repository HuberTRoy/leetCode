"""
好像是今日头条2018 秋招算法题？

有m名编辑审核文章，每个编辑独立工作，会把觉得有错误的地方通过下标标注出来：

[1, 10] 表示1-10个字符应该有问题。
现在要把多名编辑的结果合并起来：

[1, 10] [32, 45],
[5, 16] [78, 94]

那么合并后是 [1, 16] [32, 45] [78, 94]。

bug free.

Leetcode 中也有两个一样的：
https://leetcode.com/problems/merge-intervals/description/

测试通过：
beat 64%~95%...

这个更加类似:
https://leetcode.com/problems/insert-interval/description/

这个代码看 InsertInterval.py
"""

class Solution(object):
    def merge(self, _sentences):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        _sentences = sorted(_sentences, key=lambda x: x.start)

        if not _sentences:
            return []

        result = []

        head = _sentences[0].start
        tail = _sentences[0].end
        length = len(_sentences)
        for x in range(1, length):
            i = _sentences[x]
            if tail >= i.start:
                tail = max(tail, i.end)
            else:
                result.append([head, tail])
                head = i.start
                tail = i.end

        result.append([head, tail])
        return result

test = (
    [(1, 10), (32, 45)],
    [(78, 94), (5, 16)],
    [(80, 100), (200, 220), (16, 32)]
    )


def mergeArray(sentences):

    """
        这个测试数据的结构是我自己写的，所以第一步是打散数组。
        1. 根据第一个字符出现的位置进行排序。
        2. 迭代，记录i的头，记录i的末尾，末尾与下一个i的头做比较，若前者记录的大或相等则末尾替换为两者中较大的一个。
        3. 不大的情况添加到结果中，并将头尾替换为此时的数据。
        4. 最后一轮迭代在添加一次。

    """

    # 打散，相当于原题给的数据中的读入。
    _sentences = sorted([y for x in test for y in x], key=lambda x: x[0])

    if not _sentences:
        return []

    result = []

    head = _sentences[0][0]
    tail = _sentences[0][1]
    length = len(_sentences)
    for x in range(1, length):
        i = _sentences[x]
        if tail >= i[0]:
            tail = max(tail, i[1])
        else:
            result.append([head, tail])
            head = i[0]
            tail = i[1]

    result.append([head, tail])
    print(result)

mergeArray(test)

