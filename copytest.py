import copy as co
a='zhangxiaoming'
b=a
c=co.copy(a)
d=co.deepcopy(a)
a=123

print(a,b,c,d)
print(id(a),id(b),id(c),id(d))

a=[1,2,3]
b=a
print(a)
b[0]=9
print(a)
a=[1,2,3,4]
b=co.copy(a)
print(a)
b[0]=9
print(a)
a = [1,2,3]
b = co.copy(a)
print(a)
b[0] = 9
print(a)