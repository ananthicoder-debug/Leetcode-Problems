class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        n, res = len(nums), []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                left, right = j + 1, n - 1
                while left < right:
                    curr = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]: left += 1
                        while left < right and nums[right] == nums[right - 1]: right -= 1
                        left, right = left + 1, right - 1
                    elif curr < target: left += 1
                    else: right -= 1
        return res
