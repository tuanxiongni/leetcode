class Solution():
    def twoNum(self,list,target):
        dic={}
        for i,num in list:
            if target-num in dic:
                return [dic[target-num],i]
            dic[list[num]]=i
        return []

