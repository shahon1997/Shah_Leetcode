class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = ["" for i in range(n)]
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                answer[i-1] = "FizzBuzz"
            elif i % 3 == 0:
                answer[i-1] = "Fizz"
            elif i % 5 == 0:
                answer[i-1] = "Buzz"
            else:
                answer[i-1] = str(i)
        return answer
