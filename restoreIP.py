# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def restoreIpAddresses(self, s: str) -> list[str]:

        out = []
        length = len(s)

        if len(s) < 4 : raise ValueError
        
        for ip1 in range(1,4):
            
            for ip2 in range(ip1 + 1, ip1 + 4):

                for ip3 in range(ip2 + 1, ip2 + 4):

                    #if ip3 < length -3 or ip3 >= length: continue
                    if ip3 >= length -3 and ip3 < length:

                        ip = [s[0:ip1],s[ip1:ip2],s[ip2:ip3],s[ip3:]]
                        ipcheck = 0
                        for ippart in ip:
                            intippart = int(ippart)
                            if ippart == str(intippart) and intippart >=0 and intippart < 256: ipcheck +=1

                        if ipcheck == 4: out.append('.'.join(ip))
        
        return out


                    
                    

        




s = Solution()
testcases = [
    '2255511135',
    '0000',
    '101023'
]
for case in testcases:
    print("{} számsorból ez: {}".format(case,s.restoreIpAddresses(case)))
        