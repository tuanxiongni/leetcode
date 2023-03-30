# list=[1,2,3,'str']
# index= list.index('str')
# print(index)
# list.insert(1,3)
# print(list)
# list.append("app")
# print(list)
# list.extend([1,2,3])
# print(list)
# del list[0]
# print(list)
# list.pop(1)
# print(list)
# list.remove(3)
# print(list)
# list
#
# #while循环遍历
# def whi(str):
#     i=0
#     while i<len(str):
#         index=str[i]
#         i=i+1
#         print(index)
# whi("123456")
#
# #for 循环
# def fo(str):
#     for i in str:
#         print(i)
# fo('12345')
#定义列表，将偶数存入 新的列表，使用while和for
class Num():
    def whilenum(self,str):
        int=0
        oushu=[]
        while int<len(str):
            if str[int]%2==0:
                oushu.append(str[int])

            int = int + 1

        return  oushu
    def fornum(self,str):
        oushu=[]
        for i in str:
            if i%2==0:
                oushu.append(i)
            else:
                continue
        return  oushu
if __name__ == '__main__':
    num=Num()
    list=[0,1,2,3,4,5,6,7,8,9,10]
    print(num.whilenum(list))
    print(num.fornum(list))