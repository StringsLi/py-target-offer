class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    obj = Solution()
    print(obj.reverseLeftWords(s, k))
