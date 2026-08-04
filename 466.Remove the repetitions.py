class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        n = len(s2)
        d = [[0, 0] for _ in range(n)]
        for i in range(n):
            j = i
            cnt = 0
            for c in s1:
                if c == s2[j]:
                    j += 1
                    if j == n:
                        cnt += 1
                        j = 0
            d[i] = [cnt, j]
        ans = 0
        j = 0
        for _ in range(n1):
            ans += d[j][0]
            j = d[j][1]
        return ans // n2
