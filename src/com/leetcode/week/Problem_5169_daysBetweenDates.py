import time


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        format1 = "yyyy-mm-dd"
        start = time.strptime(date1, format1)
        end = time.strptime(date2, format1)
        between = (start - end) / 3600 * 1000 * 24
        return abs(between)


if __name__ == '__main__':
    date1 = "2019-06-29"
    date2 = "2019-06-30"
    obj = Solution()
    res = obj.daysBetweenDates(date1, date2)
    print(res)
