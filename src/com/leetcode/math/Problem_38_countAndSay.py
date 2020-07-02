class Solution:
    def countAndSay(self, n: int) -> str:
        a = ['1']
        for i in range(n - 1):
            b = 1
            a.append('')
            aa = []
            for j in range(len(a) - 1):
                if a[j] == a[j + 1]:
                    b += 1
                else:
                    aa.append(str(b))
                    aa.append(str(a[j]))
                    b = 1
            a = aa
        return ''.join(a)


if __name__ == '__main__':
    obj = Solution()
    print(obj.countAndSay(4))
