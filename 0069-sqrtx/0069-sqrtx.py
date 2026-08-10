class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        a1 = x
        a2=0
        while True:
            a2 = 0.5*(a1+(x/a1))
            if abs( a1 - a2 ) < 0.001:
                break
            a1 = a2
        return int(a2)