import math
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        #思路：如果B in A * k, 那么k的最小值= len(B) / len(A)的上整数
        #需要判断k和k+1哪个包含B
        k = int(math.ceil(float(len(B)) / len(A))) 
        for i in range(2):
            if B in A * (k + i): # k+i必须是int型
                return k + i
        return -1
