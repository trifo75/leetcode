# %% h-index rendezetlen és rendezett listán

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        
        h = 0
        citations.sort(reverse=True)
        for i,cit in enumerate(citations):
            if cit > i:
                h = i + 1 
            else:
                break

        return h
        
    def hIndex_on_ordered(self, citations: list[int]) -> int:
        
        h = 0
        l = len(citations)
        while h < citations.pop():
            h += 1
        return h



sample = [3,0,6,1,5]


s = Solution()

# általános eset
print(s.hIndex(sample))

# rendezett lista esetén
sample.sort()
print(s.hIndex_on_ordered(sample))

