"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

给一组带有字符串的数组，进行变位词分类。

思路是排序的思路，排序后为同一个的放到一起。

效率就测试来看尚可。

beat 70%

测试地址：
https://leetcode.com/problems/group-anagrams/description/

"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        
        for i in strs:
            key = ''.join(sorted(i))
            
            try:
                result[key].append(i)
            except:
                result[key] = [i]
        
        return result.values()
        