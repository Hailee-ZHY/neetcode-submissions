class TimeMap:

    def __init__(self):
        self.holder = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.holder[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        content = self.holder[key] if key in self.holder else []

        # if content[0][0] > timestamp:
        #     return ""

        l, r = 0, len(content)-1
        res = ""
        while l <= r :
            m = (l+r)//2
            if content[m][0] > timestamp:
                r = m-1
            else:
                res = content[m][1]
                l = m+1
        return res
        



        
