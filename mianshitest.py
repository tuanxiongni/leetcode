def hebing(list1,list2):
    return list(zip(list1,list2))
list1=['x','y','z']
list2=[1,2,3]
print(hebing(list1,list2))

def dict(dic:dict):
    return list(dic.keys())
dic={'a':10,'b':20,'c':30}
print(dict(dic))
def dict2(dic:dict):
    return list(dic.values())
print(dict2(dic))

def appendic(dic,key,value):
    dic[key]=value
    return dic
key ,value='me',25
print(appendic(dic,key,value))
def isindic(dic,key):
    if key in dic.keys():
        print('yes')
    else:
        print("no")
key='alin'
isindic(dic,key)