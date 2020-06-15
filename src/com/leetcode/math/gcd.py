import math


class GCD:

    def gcd(self, a: int, b: int) -> int:
        return a if b == 0 else self.gcd(b, a % b)


obj = GCD()
res = obj.gcd(12, 18)
res2 = math.gcd(12, 18)
print(res, res2)
