class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # 题干中需要注意的有两点：第一，nums1和nums2这两个数组中的元素都是已经排好顺序的（默认应该是从小到大排序）；
        # 第二，nums1数组的位数是大于等于n＋m的
        # 思路：维护三个指针，ind1指向nums1的尾部，ind2指向nums2的尾部, total_ind指向合并后nums1的尾部
        # 从后往前遍历nums1, nums2，比较尾部元素的大小，较大值放到nums1[total_ind]位置
        # 然后total_ind，和较大值指针前移一位
        # 最后，如果nums2还剩有元素，取出来赋值到nums1对应位置即可
        #　为什么会有最后一步，因为无论是nums1还是nums2剩下的元素一定比nums[m : m + n]元素小，如果大的话，肯定已经赋值过去了
        #　如果是nums1有剩余，保持不变
        # 如果是nums2有剩余，需要移动到nums1中
        
        # 这里要利用好nums1, nums2已经排序这个特点
 
        ind1 = m - 1
        ind2 = n - 1
        total_ind = m + n - 1
        while ind1 >= 0 and ind2 >= 0:
            if nums1[ind1] > nums2[ind2]:
                nums1[total_ind] = nums1[ind1]
                total_ind -= 1
                ind1 -= 1
            else:
                nums1[total_ind] = nums2[ind2]
                total_ind -= 1
                ind2 -= 1
        
        while ind2 >= 0:
            nums1[total_ind] = nums2[ind2]
            ind2 -= 1
            total_ind -= 1
            
