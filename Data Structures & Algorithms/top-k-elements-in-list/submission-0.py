class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        answer = []
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
        buckets = [[] for _ in range(len(nums)+1)]
        for num in frequency:
            buckets[frequency[num]].append(num)
        for item in reversed(buckets):
            if len(item) is not 0:
                for i in reversed(item):
                    if len(answer) < k:
                        answer.append(i)
                    else:
                        break
        return answer



        