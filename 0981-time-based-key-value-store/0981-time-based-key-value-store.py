class TimeMap:

    def __init__(self):
        self.dict={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key]=[]
        self.dict[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res=""
        values=self.dict.get(key,[]) #this means if a key exists return the value associated with it, if no such key exists instead of giving an error return an empty list

        l=0
        r=len(values)-1
        while l<=r:
            mid = (l+r)//2
            if values[mid][1]>timestamp:
                r=mid-1
            elif values[mid][1]<=timestamp:
                l=mid+1
        if r>=0:
            res=values[r][0]   
        return res

        

       
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)