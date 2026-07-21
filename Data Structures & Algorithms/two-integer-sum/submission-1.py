class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexLookup = {}
        for n in range(len(nums)):
            if (target - nums[n]) in indexLookup:
                return [indexLookup.get(target - nums[n]), n]
            else:
                indexLookup[nums[n]] = n
        return[]

        