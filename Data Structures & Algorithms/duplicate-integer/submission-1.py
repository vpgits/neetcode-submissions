class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasSeen = set()
        for i in range(len(nums)):
            if nums[i] not in hasSeen:
                hasSeen.add(nums[i])
            else:
                return True
        return False
        