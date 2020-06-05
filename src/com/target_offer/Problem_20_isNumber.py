class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except:
            return False


if __name__ == '__main__':
    obj = Solution()
    s = "-1E-16"
    print(obj.isNumber(s))
