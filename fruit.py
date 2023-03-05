# 904. Fruit into baskets
import timeit

from collections import defaultdict
class Solution:

    def totalFruit(self, fruits: list[int]) -> int:

        #preprocessing...

        # empty input string should return 0
        if len(fruits) == 0: return 0
        # only one tree should return 1 or 2 fruits
        if len(fruits) <= 2: return len(fruits)

        # get a list of fruit types and get all possible combinations
        # of two kinds
        typelist = list(set(fruits))

        # if we have only one ot two types of fruits, we can
        # get fruit from all trees
        if len(typelist) <=2: return len(fruits)


        # in all other cases we process stuff


        buckets = list()

        max = 0


        # we are collecting all the positions where a new bucket should be opened
        # * there is a new type of fruit which is NOT in the last 2 types
        # * the "buckets" list have to be trimmed to the last 2 items
        for i,fruit in enumerate(fruits):
            buckets.append(defaultdict(lambda: 0))

            # we increase the num of current fruits in every buckets
            for j, bucket in reversed(list(enumerate(buckets))):
                bucket[fruit] +=1

            # we drop last bucket if its contents are aready collected in some other bucket
            lastbucket = buckets[-1]
            lastbucketkeys = sorted(list(lastbucket.keys()))
            for j, bucket in reversed(list(enumerate(buckets[:-1]))):
                if sorted(list(bucket.keys())) == lastbucketkeys:
                    buckets.remove(lastbucket)
                    break

            # if the third type of fruit appears in the bucket ( len > 2 ), then 
            # collected fruits are counted and the bucket is removed
            for j, bucket in reversed(list(enumerate(buckets))):
                if len(bucket) > 2:
                    curr = sum(list(bucket.values())[:2]) # sum of the first 2 value in the dict
                    if curr > max: max = curr
                    buckets.pop(j)

        # checking remaining buckets
        for i, bucket in enumerate(buckets):
            curr = sum(list(dict(bucket).values())[:2])
            if curr > max: max = curr
           

        return max


    def totalFruit_best(self, fruits: list[int]) -> int:
        count=0
        first=fruits[0]
        second=None
        nowmax=0
        result=0
        flag=False
        for i in fruits:
            if(flag):
                if(i == second):
                    count+=1
                    nowmax+=1
                elif(i==first):
                    nowmax+=1
                    count=1
                    first=second
                    second=i
                else:
                    if(nowmax>result):
                        result=nowmax
                    nowmax=count+1
                    count=1
                    first=second
                    second=i
            else:
                if(i==first):
                    count+=1
                    nowmax+=1
                else:
                    flag=True
                    count=1
                    nowmax+=1
                    second=i
        if(nowmax>result):
            result=nowmax
        return result



testcases = [
    [1,0,1,4,1,4,1,2,3],
    [3,3,3,1,2,1,1,2,3,3,4],
    [1,2,1],
    [0,1,2,2],
    [1,2,3,2,2],
    [0,1,3]*100000 ,
    [1]*100000,
    [0,1]*20000,
]


s = Solution()

for c in testcases:
    print("Testcase input: ",end='')
    if len(c) > 10:
        print(c[:10],"...")
    else:
        print(c)
    print("Output: ",end='')
    
    starttime = timeit.default_timer()
    print(s.totalFruit(c), end=' ')
    endtime = timeit.default_timer()
    print("time: {} secs".format(endtime-starttime))


#print("TimeIt session")
#out = s.totalFruit([0,1]*100000 + [5,6])

#print( "Time diff is ", timeit.default_timer() -starttime )