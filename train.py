def bind(tup,set):
    return list(tup)+list(set)

tuple=(1,2,3)
set={4,5,6}
print(f'连接元组和集合{bind(tuple,set)}')
def add(list):
    list.insert(0,7)
    list.append(0)
    return list
list=[1,2,3,4,5,6]
print(add(list))

def rever(list):
    return list[::-1]
def rever2(lit:list):
    return lit.reverse()
list=[1,2,3,4,5,6]
print(rever(list))
print(rever2(list))

def indexoflist(list):
    return list[::-1],list.index(5)
list=[0,1,2,3,4,5,6,7]
print(indexoflist(list))

def coun(list):
    for i in list:
        return list.count(i)
list=[True,False,1,0,2]
print(coun(list))

def delnum(list:list,x):
    if x in list:
        list.remove(x)
    return list
lis=[True,False,1,0,'x',2,True]
x='x'
print(delnum(lis,x))

def jishu(num:list)->list:
    return num[::2] ,num[1::2]
number=[True,False,1,0,'x',2,True]
print(jishu(number))

def sor(list):
    return list.sort(),list.sort(reverse=True)
sortnum=[3,0,4,1,2,5,4,6]
print(sor(sortnum))

def medium(list):
    for i in range(0,len(list)):
        if list[i]>5:
            list[i]=1
        else:
            list[i]=0
    return list
a=[1,2,3,4,5,6,7,8,9]
print(medium(a))
def everyelement(list):
    for i in list:
        print(i)
        print(list.index(i))
a=['x','y','z']
everyelement(a)

def jishu_oushu(list):
    jishu=[]
    oushu=[]
    for i in list:
        if i%2==0:
            oushu.append(i)
        else:
            jishu.append(i)
    return jishu,oushu
a=[1,2,3,4,5,6,7,8,9,10]
print(jishu_oushu(a))
a=[[6,5],[3,7],[2,8]]
print(a)
b=sorted(a,key=(lambda  x:x[0]))
print(b)
c=sorted(a,key=lambda x:x[-1])
print(c)

def inse(list1,list2):
    print(list1.insert(3,list2))
list1=[1,4,7,2,5,8]
list2=['x','y','z']
inse(list1,list2)

def gernum():
    return list(range(5,50))
a = {'Alice':20,'Beth':18,'Cecil':21}
print(list(a))



