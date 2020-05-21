class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        sets = set()

        ans, left, right = 0, 0, 0
        while right < n:
            while s[right] in sets:
                sets.remove(s[left])
                left += 1
            sets.add(s[right])
            right += 1
            ans = max(ans, right - left)
        return ans


s = "abcabcbb"
obj = Solution()

res = obj.lengthOfLongestSubstring(s)
print(res)