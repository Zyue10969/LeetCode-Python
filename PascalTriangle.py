class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 这是个递归的过程
        # 第一行的是[1]
        # 第二行是[1] + [1] = [1, 1]
        # 第三行是[1] + [1 + 1] + [1] = [1, 2, 1]
        # 第四行是[1] + [1 + 2] + [2 + 1] + [1] = [1, 3, 3, 1]
        # 第五行是[1] + [1 + 3] + [3 + 3] + [3 + 1] + [1] = [1, 4, 6, 4, 1]
        row = [1]
        rows = []
        for n in range(numRows):
            rows.append(row)
            row = [1] + [row[i] + row[i + 1] for i in range(len(rows) - 1)] + [1]
        return rows
          
            
