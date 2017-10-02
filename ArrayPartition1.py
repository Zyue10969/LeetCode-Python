class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路: 将相邻的两个数进行组合，才能获得min(ai, bi)之和的最大值
        #　算法分析:
        # 对于任意组合,有ai <= bi
        # 定义　Smin = min(a1, b1) + min(a2, b2) + ... + min(an, bn) = a1 + a2 + ... + an
        # 定义   Sn  = (a1 + b1) + (a2 + b2) + ... + (an + bn)
        # 定义   di  = |ai - bi|, 由于ai <= bi，则di = bi - a1 ==> bi = ai + di
        # 定义   Sd  = d1 + d2 + ... + dn 
        #  则有 Sn = (a1 + a1 + d1) + (a2 + a2 + d2) + ... + (an + an + dn)
        #          = 2 * (a1 + a2 + ... + an) + （d1 + d2 + ... + dn)
        #          = 2 * Smin + Sd
        #  ==>  Smin = (Sn - Sd) / 2
        # 由于给定数组nums，有 Sn = (a1 + b1) + (a2 + b2) + ... +(an + bn)是个定值
        # 为了获得Smin的最大值，要使Sd最小
        # 所以这个问题就是在数组中找到使di（ai和bi之间的距离）的和尽可能小的对。
        # 显然，相邻元素的这些距离之和是最小的。
        return sum(sorted(nums)[::2])
