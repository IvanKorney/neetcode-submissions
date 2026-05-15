class TimeMap:

    def __init__(self):
        self.obj = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.obj:
            self.obj[key] = []
        self.obj[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.obj:
            return ""
    
        l, r = 0, len(self.obj[key])-1
        while l <= r:
            m = (l+r)//2
            if self.obj[key][m][1] > timestamp:
                r = m - 1
            else:
                l = m + 1
            

        return "" if self.obj[key][r][1] > timestamp else self.obj[key][r][0]
        
