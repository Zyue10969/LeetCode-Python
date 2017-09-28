# -*- coding:utf-8 -*-
import itertools, collections

def fourSum(nums, target):
    # 用空间换取时间
    ret = set()
    two_sum = collections.defaultdict(list)
    for (id1, num1), (id2, num2) in itertools.combinations(enumerate(nums), 2):
        two_sum[num1 + num2].append({id1, id2})

    keys = two_sum.keys()
    for key in keys:
        if two_sum[key] and two_sum[target - key]:
            for pair1 in two_sum[key]:
                for pair2 in two_sum[target - key]:
                    if pair1.isdisjoint(pair2):
                        ret.add(tuple(sorted(nums[i] for i in pair1 | pair2)))
            del two_sum[key]
            if key != target - key:
                del two_sum[target - key]
    return list(map(list,ret))
