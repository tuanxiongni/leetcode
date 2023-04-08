def number(self,n):
    count=0
    while n&0xFFFFFFFF!=0:
        count+=1
        n=n&(n-1)
    return  count