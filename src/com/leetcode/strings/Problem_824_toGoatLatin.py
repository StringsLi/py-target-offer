class Solution:
    def toGoatLatin(self, S: str) -> str:
        S_arr = S.split(" ")
        count = 1
        res = ""
        for word in S_arr:
            if word[0] in "aeiou":
                res += word + "ma" + count * 'a' + " "
            else:
                ans = word[1:] + word[0] + "ma" + count * 'a' + " "
                res += ans
            count += 1
        return res.strip(" ")


if __name__ == '__main__':
    obj = Solution()
    S = "I speak Goat Latin"
    print(obj.toGoatLatin(S))
