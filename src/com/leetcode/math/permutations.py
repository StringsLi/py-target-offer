import itertools


def permute(nums):
    return list(itertools.permutations(nums))


nums = [1, 2, 3]
ret = permute(nums)
print(ret)
