class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()
        n = len(nums)
        res = list()
        visited = [False] * n
        def backtrack(m):
            if len(m) == n:
                res.append(list(m))
                return
            for i in range(n):
                if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                    continue
                visited[i] = True
                m.append(nums[i])
                backtrack(m)
                m.pop()
                visited[i] = False
        backtrack(list())
        return res

        
