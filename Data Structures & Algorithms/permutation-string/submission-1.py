class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        oneStorage = {}
        twoStorage = {}
        if len(s1) > len(s2):
            return False
        
        for char in s1:
            if char in oneStorage:
                oneStorage[char] += 1
            else:
                oneStorage[char] = 1
        left = 0
        for index in range(len(s1)):
            if s2[index] in twoStorage:
                twoStorage[s2[index]] += 1
            else:
                twoStorage[s2[index]] = 1
        right = left + len(s1)
        while right < len(s2):
            if oneStorage == twoStorage:
                return True
            if s2[right] in twoStorage:
                twoStorage[s2[right]] += 1
            else:
                twoStorage[s2[right]] = 1
            right += 1
            if twoStorage[s2[left]] > 1:
                twoStorage[s2[left]] -= 1
            else:
                twoStorage.pop(s2[left])
            left += 1
        return oneStorage == twoStorage


        