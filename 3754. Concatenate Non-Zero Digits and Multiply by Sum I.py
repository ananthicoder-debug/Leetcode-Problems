class Solution:
    def sumAndMultiply(self, n: int) -> int:
        d=str(n)
        m=d.replace("0","")
        o=len(m)
        if(o==0):
            return 0
        l=g=int(m)
        b=0
        for i in range(o):
            h=l%10
            b=b+h
            l=l//10
        k=g*b
        return k
