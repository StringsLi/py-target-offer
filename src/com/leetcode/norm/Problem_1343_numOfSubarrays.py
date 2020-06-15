"""
给你一个整数数组 arr 和两个整数 k 和 threshold 。

请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。

 

示例 1：

输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
输出：3
解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4 （threshold 的值)。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    """ 暴力法，超时"""

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        for i in range(len(arr) - k + 1):
            avg_k = sum(arr[i:i + k]) / k
            if avg_k >= threshold:
                count += 1
        return count

    """ 滑动窗口"""

    def numOfSubarrays2(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        avg_k = sum(arr[0:k]) / k
        if avg_k >= threshold:
            count += 1
        j = 0
        for i in range(k, len(arr)):
            avg_k = avg_k + (arr[i] - arr[j]) / k
            j += 1
            if avg_k >= threshold:
                count += 1
        return count


arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4

obj = Solution()
res = obj.numOfSubarrays2(arr, k, threshold)
print(res)
