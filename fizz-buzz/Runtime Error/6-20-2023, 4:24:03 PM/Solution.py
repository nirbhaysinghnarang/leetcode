// https://leetcode.com/problems/fizz-buzz

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        for i in range(n+1):
            arr[i+1] = (if (i%3==0 and i%5==0) then "FizzBuzz"
                else if (i%3==0) then "Fizz" else if (i%5==0) then "Buzz" else str (i)
            )
        return arr