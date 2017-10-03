from copy import deepcopy
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        len_r = len(M)
        len_c = len(M[0]) if len_r else 0
        res = deepcopy(M) #　这里用深拷贝，不用赋值
        for r in range(len_r):
            for c in range(len_c):
                neighbors = [M[x][y]
                            for x in (r-1, r, r+1)
                            for y in (c-1, c, c+1)
                            if 0 <= x < len_r
                            and 0 <= y < len_c]
                res[r][c] = sum(neighbors) / len(neighbors)
        return res
