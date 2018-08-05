"""

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.

给两个列表，求加起来的索引是最小的重合部分，若有多个相同的则输出多个相同的，无顺序要求。

思路：

直接判断的话是 O(mn)，利用哈希表（字典）来减少查询时间。

可优化部分：
第二次不用哈希表，用两个变量，一个代表当前的最小值，一个代表所存数据，不断替换，追加。

测试用例：
https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

"""

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        list1_dict = {value:index for index, value in enumerate(list1)}
        commonInterest = {}
        for index, value in enumerate(list2):
            if list1_dict.get(value) is not None:
                try:
                    commonInterest[index + list1_dict.get(value)].append(value)
                except KeyError:
                    commonInterest[index + list1_dict.get(value)] = [value]

        return commonInterest[min(commonInterest)]

