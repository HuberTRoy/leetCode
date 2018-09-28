"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

1 - n
3的倍数加 Fizz
5的倍数加 Buzz
3和5的倍数加 FizzBuzz

比较简单，今日的零启动。

用取模%也可以，一开始觉得取模可能效率不高就没用。

不过看结果是一样的：

beat 94%
测试链接：
https://leetcode.com/problems/fizz-buzz/description/

"""
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        result = []
        fizz_time = 0
        buzz_time = 0
        fizzbuzz_time = 0
        
        
        for i in range(1, n+1):
            fizz_time += 1
            buzz_time += 1
            fizzbuzz_time += 1
            
            if fizzbuzz_time == 15:
                result.append("FizzBuzz")
                fizzbuzz_time = 0
                fizz_time = 0
                buzz_time = 0
                continue
                
            if fizz_time == 3:
                fizz_time = 0
                result.append("Fizz")
                continue
            
            if buzz_time == 5:
                buzz_time = 0
                result.append("Buzz")
                continue
            
            result.append(str(i))
        return result
