class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s2 in (s1 + s1):
            return True
        else:
            return False

    def isFlipedString2(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s2 in (s1 + s1)


if __name__ == '__main__':
    s1 = "waterbottle"
    s2 = "erbottlewat"
    obj = Solution()
    print(obj.isFlipedString2(s1, s2))
