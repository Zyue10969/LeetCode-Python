class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #　给定一个数组，这个数组代表一个数字，数字的最高位存在数组最前面，数字的最低位存在数组的最后面（符合书写习惯），
        # 输出该数字加1得到的数组
        # 例如 input:[9,9] output:[1,0,0]
        # 思路：从低位开始遍历数组，若该位加一（这个1包含了进位的1和最开始的加的1）不产生进位的话，将该位加一返回结果即可；
        # 若产生进位，则将该位置设为0,继续遍历即可
        # 需要注意的是第[0]位，即最高位，如果最高位产生进位，则将该位设为０，并新开一个数组: [1],然后[1].extend(digits)即可
        for i in range(len(digits) - 1, -1, -1):
            if i == 0:
                if digits[i] == 9:
                    digits[i] = 0
                    result = [1]
                    result.extend(digits)
                    return result
            if digits[i] < 9:
                digits[i] += 1
                return digits
            if digits[i] == 9:
                digits[i] = 0
