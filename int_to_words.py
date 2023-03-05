"""
Convert a non-negative integer num to its English words representation.
 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

Constraints:

0 <= num <= 231 - 1
"""

# %%
class Solution:
    words = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred'
        }

    magnitudes = {
        1000000000: 'billion',
        1000000:    'million',
        1000:       'thousand',
        1:          ''
        }

    out_list = []

    def triad_to_words_wrong(self,num: int) -> str:
        """convert triad nums to string ( 0 - 999)"""

        # input should be between 0 and 999 inclusive
        if (num > 999) or (num < 0):
            raise ValueError

        out = ''

        # when ZERO, return empty string (add nothing to out)
        if num == 0:
            pass
        elif (num >= 1) and (num <= 20):
            out = self.words[num]
        elif (num > 20):
            if num >= 100:
                out = ' '.join((self.words[num // 100],self.words[100]))
                num = num % 100
                if num > 0:
                    out +=' '

            if num == 0:
                pass
            else:
                if num % 10 == 0:
                    out += self.words[num]
                else:
                    out += self.words[num - num % 10] + ' ' + self.words[num % 10]

        pass
        return out

    def triad_to_words(self,num: int) -> str:

        # check constraints
        num = int(num)
        if (num < 0) or (num>999):
            raise ValueError

        # get digits
        d1 = num // 100
        num = num % 100
        d2 = num // 10
        d3 = num % 10

        outlist = []
        if d1 > 0:
            outlist.append(self.words[d1])
            outlist.append(self.words[100])

        if 0 < num <= 20:
            outlist.append(self.words[num])
        else:
            if d2 > 0:
                outlist.append(self.words[d2 * 10])
            if d3 > 0:
                outlist.append(self.words[d3])

        return ' '.join(outlist)






    def numberToWords(self, num: int) -> str:
        
        # check input constraints
        num = int(num)        
        #if (num <= 0) or (num >= (2 ** 31 -1)):
        #    raise ValueError

        # reset output string
        out = ''

        # If zero...
        if num == 0:

            return self.words[num].rstrip().lstrip().title()

        # walk magnitudes
        for mag in list(self.magnitudes.keys()):
            if num >= mag:
                # separate triad for the actual magnitude
                triad = (num // mag) % 1000
                if triad > 0:
                    out += ' ' + self.triad_to_words(triad) + ' ' + self.magnitudes[mag]
                
        return out.lstrip().rstrip().title()


s = Solution()
testcase = 1000000
print('X>' + s.numberToWords(testcase) + '<X')

#for testcase in range(999):
#    print(s.triad_to_words(testcase))


# %%
