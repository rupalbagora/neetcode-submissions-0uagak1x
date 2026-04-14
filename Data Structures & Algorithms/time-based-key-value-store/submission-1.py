class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))      

    def get(self, key: str, timestamp: int) -> str:
        val = self.timeMap[key]
        if not val:
            return ""

        l, r = 0, len(val) - 1
        res = ""
        while l <= r:
            mid = l + (r - l) // 2
            if val[mid][1] <= timestamp:
                res = val[mid][0]
                l = mid + 1
            else:
                r = mid - 1
            
        return res