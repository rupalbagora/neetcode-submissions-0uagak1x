class Solution:
    def isFreqSame(self,freq1,freq2):
        for i in range(26):
            if freq1[i]!=freq2[i]:
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq=[0]*26
        for ch in s1:
            freq[ord(ch)-ord('a')]+=1
        wind_size=len(s1)
        for i in range(len(s2)):
            wind_freq=[0]*26
            wind_idx=0
            idx=i
            while wind_idx<wind_size and idx<len(s2):
                wind_freq[ord(s2[idx])-ord('a')]+=1
                wind_idx+=1
                idx+=1
            if self.isFreqSame(freq,wind_freq):
                return True
        return False