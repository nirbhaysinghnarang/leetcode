// https://leetcode.com/problems/fizz-buzz

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        for i in range(n):
            num = i+1
            if not (num%3 or num%5):
                arr.append("FizzBuzz")
            elif not num%3:
                arr.append("Fizz")
            elif not num%5:
                arr.append("Buzz")
            else:
                arr.append(str(num))
        return arr