import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ""
        nums = [str(i) for i in range(1, n + 1)]
        fact = math.factorial(n - 1)
        k -= 1
        for i in range(n - 1, -1, -1):
            idx = k // fact
            res += nums.pop(idx)
            k %= fact
            if i > 0:
                fact //= i
        return res

        
