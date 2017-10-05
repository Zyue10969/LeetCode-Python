# -*- coding:utf-8 -*-
def BinSearch(list, key, low, high):
    """
    list: 有序表
    key: 待查询的关键字
    low: low索引
    high: high索引
    """
    mid = (low + high) / 2
    if low > high:
        return -1
    elif key == list[mid]:
        return mid
    elif key > list[mid]:
        return BinSearch(list, key, mid + 1, high) #　递归
    elif key < list[mid]:
        return BinSearch(list, key, low, mid - 1) # 递归

if __name__ == "__main__":
    list = [4, 13, 27, 38, 49, 49, 55, 65, 76, 97]
    print(BinSearch(list, 4, 0, len(list) - 1))
    
    
    
    
