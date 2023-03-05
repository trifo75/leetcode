class Solution:

    
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        sortedlist = sorted( intervals + [newInterval])

        i=0
        while i < len(sortedlist) - 1:
            while sortedlist[i][1] >= sortedlist[i+1][0]:
                if sortedlist[i][1] < sortedlist[i+1][1]: 
                    sortedlist[i][1] = sortedlist[i+1][1]
                sortedlist.pop(i+1)
                if len(sortedlist) == i+1: break
                
            i+=1
            
        return sortedlist
            
                   
            
        


s = Solution()



testcases = [
    {
        'input_interval': [[0,2],[3,9]],
        'insert_interval': [6,8]
    },
    {
        'input_interval': [[1,5]],
        'insert_interval': [2,3]
    },
    {
        'input_interval': [[1,2],[3,5],[6,7],[8,10],[12,16]],
        'insert_interval': [4,8]
    },
    {
        'input_interval': [[1,3],[6,9]],
        'insert_interval': [2,5]
    },
    {
        'input_interval': [],
        'insert_interval': [5,7]
    },
    {
        'input_interval': [[1,5]],
        'insert_interval': [6,8]
    },

]

for i, testcase in enumerate(testcases):
    print("\nTeszt  {}".format(i))
    print("Bemeneti lista: {}, beszúrandó: {}"\
        .format(testcase['input_interval'],testcase['insert_interval']))

    outlist = s.insert(testcase['input_interval'],testcase['insert_interval']) 
    print(".               {}".format(outlist))
    print()





""" 
Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10]. 
"""