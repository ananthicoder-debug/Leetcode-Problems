class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        def getMaxSubarray(nums, length):
            stack = []
            drop = len(nums) - length
            for num in nums:
                while drop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:length]
        def merge(sub1, sub2):
            return [max(sub1, sub2).pop(0) for _ in range(len(sub1) + len(sub2))]
        max_result = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            sub1 = getMaxSubarray(nums1, i)
            sub2 = getMaxSubarray(nums2, k - i)
            candidate = merge(sub1, sub2)
            if candidate > max_result:
                max_result = candidate
        return max_result

        
