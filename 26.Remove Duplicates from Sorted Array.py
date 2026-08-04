class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        o=len(nums)
        uni=set(nums)
        nums[:] = sorted(list(uni))
        h=len(uni)
        return h
