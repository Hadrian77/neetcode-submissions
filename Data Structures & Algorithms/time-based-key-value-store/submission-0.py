class TimeMap:

    def __init__(self):
        self.cache = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key in self.cache:
            self.cache[key].append((value,timestamp))
        else:
            self.cache[key] = [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:


        if key in self.cache:
            values = self.cache[key]
            l = 0;
            r = len(values) -1
            currentIndex = -1

            while l <= r:
                mid = (l + r)//2

                if values[mid][1] <= timestamp:
                    l = mid + 1
                    currentIndex = mid
                else:
                    r = mid - 1 

            if currentIndex == -1:
                return ""
            else:
                return values[currentIndex][0]
        else:
            return ""
        
