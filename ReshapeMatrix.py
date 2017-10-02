import numpy as np
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """     
        # 思路一：将nums先拼接成一维列表，然后每c个元素成一行
        rows = sum(nums, []) # 这一行很关键，要理解
        if len(rows) != (r * c):
            return nums
        else:
            matrix =  []
            row = []
            count_row = 0 #　一行c个数
            for num in rows:
                row.append(num)
                count_row += 1
                if count_row == c: 
                    matrix.append(row) 
                    row = []
                    count_row = 0
            return matrix
        
        # 思路二：numpy包
        try:
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums
                
