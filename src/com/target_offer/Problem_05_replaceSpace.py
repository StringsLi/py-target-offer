class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")


if __name__ == '__main__':
    s = "We are happy."
    obj = Solution()
    print(obj.replaceSpace(s))
