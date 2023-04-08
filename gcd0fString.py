class Solution(Object):
    def gcdofstring(self,str1,str2):
        l1,l2=len(str1),len(str2)
        def gcd(l1,l2):
            return l1 if l2%l1==0 else gcd(l1,l1%l2)
        candidate=gcd(l1,l2)
        if str1[0:candidate]*(l1//candidate)==str1 and str1[0:candidate]*(l2//candidate)==str2:
            return str1[0:candidate]
        else:
            return ""