

# 906. Super Palindromes
import math
import timeit

class Solution:

    def get_next_palindrome(self, snum: str) -> str:

        out = self.get_next_palindrome_parts(snum)
        return ''.join(out)


    def get_next_palindrome_parts(self, snum: str):
        # get the first palindrome number after the provided one
        numlen = len(snum)
        halflen = numlen // 2

        # for 1 digit numbers, return themselves as a single digit is always palindrome
        if numlen == 1: return snum, '', ''

        # for longer nums, we split in half and check
        # the first half is the same as the second half reversed
        # this way the middle digit is left out for odd length numbers

        firsthalf = snum[:halflen]
        secondhalf = snum[-halflen:]

        if numlen % 2:
            # with odd number of digits we have a middle digit
            middle = snum[halflen]
            if int(secondhalf) > int(firsthalf[::-1]):
                snum = str(int(firsthalf + middle) +1)
                snum += snum[:halflen][::-1]
                return snum[:halflen], snum[halflen], snum[:halflen][::-1]
            else:
                return firsthalf[:halflen], middle, firsthalf[::-1]
        else:
            # with even number of digits there is no middle character
            if int(secondhalf) > int(firsthalf[::-1]):
                firsthalf = str( int(firsthalf) + 1)
            return  firsthalf, '', firsthalf[::-1]


    def is_palindrome(self, snum: str) -> bool:
        # just test if the input is palindrome by
        # reversing the first half to the end
        # this way it doesn't matter if we have a 
        # middle character or not

        numlen = len(snum)
        halflen = numlen // 2
        if numlen == 1: return True

        return snum[:halflen] == snum[-halflen:][::-1]

    
    def superpalindromesInRange(self, left: str, right: str) -> int:

        l = int(left)
        r = int(right)

        count = 0

        # get the starting number which is the sqrt of 'left' number.
        # if it is not int, then step to the next int upwards
        l_root = math.sqrt(l)
        if l_root > math.floor(l_root):
            l_root = math.trunc(l_root) + 1
        else:
            l_root = math.trunc(l_root)
            
        # step to the first root palindrome    
        rootpalindrome = self.get_next_palindrome(str(l_root))
        l = int(rootpalindrome) ** 2

        while  l <= r:

            if self.is_palindrome(str(l)):
                count += 1

            rootpalindrome = self.get_next_palindrome(str(int(rootpalindrome)+1))
            l = int(rootpalindrome) ** 2

        return count




testcases = [
    (4,1000),
    (5,1000),
    (500,900),
    (9357639525,2353857225354),
]


s = Solution()


for c in testcases:
    print("Testcase input: ",c)
    print("Output: ",end='')
    
    starttime = timeit.default_timer()
    print(s.superpalindromesInRange(c[0],c[1]), end=' ')
    endtime = timeit.default_timer()
    print("    time: {} secs".format(endtime-starttime))

