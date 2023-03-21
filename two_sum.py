from itertools import combinations
import time

class Solution:
       

    def twoSum(self, nums: list[int], target: int) -> list[int]:

        num_min = min(nums)
        num_max = max(nums)

        # Let's gather the indexes of possible values. 
        # A value is considered possible, if  target - value is  greater than num_min AND smaller than num_max
        possible_indices = [ i for i in range(len(nums)) if ((target - nums[i] >= num_min) and (target - nums[i] <= num_max)) ]

        # generating all the 2 piece combinations of the possible indices
        combs = combinations(range(len(possible_indices)), 2)

        # and check the combinations brute force
        for c in combs:
            i1 = possible_indices[c[0]]
            i2 = possible_indices[c[1]]
            if nums[i1] + nums[i2] == target: return [i1, i2]



#input = [0,4,3,0]
target, input = 19999, list(range(1,10001))
target, input = 9, [2,7,11,15]

s = Solution()

print( s.twoSum(input, target) )


