from collections import Counter
from typing import List

"""给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/group-anagrams
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            keys = "".join(sorted(s))
            if keys not in dic:
                dic[keys] = [s]
            else:
                dic[keys].append(s)
        return list(dic.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
obj = Solution()
res = obj.groupAnagrams(strs)
print(res)
