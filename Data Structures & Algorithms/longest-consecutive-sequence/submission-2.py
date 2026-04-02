class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums.sort()
        n = len(nums)

        i, j = 0, 1
        current = 1   # current streak
        longest = 1   # max streak

        while j < n:
            if nums[i] == nums[j]:
            # duplicate → skip
                j += 1

            elif nums[j] == nums[i] + 1:
            # consecutive → extend streak
                current += 1
                longest = max(longest, current)
                i = j
                j += 1

            else:
            # break in sequence → reset
                current = 1
                i = j
                j += 1

        return longest
        