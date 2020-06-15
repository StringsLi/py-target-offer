from typing import List


def permutation(s: str) -> List[str]:
    if not s: return
    s = list(sorted(s))
    res = []

    def helper(s, tmp):
        if not s: res.append(''.join(tmp))
        for i, char in enumerate(s):
            if i > 0 and s[i] == s[i - 1]:
                continue
            helper(s[:i] + s[i + 1:], tmp + [char])

    helper(s, [])
    return res


def permuteUnique2(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    def helper(nums, temp):
        if not nums:
            res.append(temp)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            helper(nums[:i] + nums[i + 1:], temp + [nums[i]])

    helper(nums, [])
    return res


print(permutation('abc'))
print(permuteUnique2([1, 2, 2]))
