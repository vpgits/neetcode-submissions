class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}
        for word in strs:
            counts = [0] * 26
            for letter in word:
                index = ord(letter) - ord("a")
                counts[index] += 1
            hashedCounts = tuple(counts)
            if hashedCounts in tracker:
                tracker[hashedCounts].append(word)
            else:
                tracker[hashedCounts] = [word]
        return list(tracker.values())
            

        