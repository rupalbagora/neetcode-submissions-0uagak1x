class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        for i in strs:
            val = "".join(sorted(i))
            if val not in temp:
                temp[val] = []
            temp[val].append(i)

        return (list(temp.values()))