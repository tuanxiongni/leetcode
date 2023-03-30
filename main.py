# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    def sum(a,b):
        if a>b:
            return a
        else:
            return b
    print(sum(3,5))
    print_hi('PyCharm')
    def strcat(str1,str2):
        print(f"my first name is {str1},my second name is {str2}")
    strcat('ni','tuanxiong')

def stock():
    name='比亚迪'
    stock_price=19
    stock_code='0030003'
    stock_price_rate=1.2
    growth_days=7
    finally_price=stock_price*stock_price_rate**growth_days
    print(f'公司{name},代码{stock_code},当前股价{stock_price}')
    print('每日增长率%f,经过%d天的增长股价为%2f'%(stock_price_rate,growth_days,finally_price))
stock()
def inp():
    inp=input("请输入你的输入")
    print(f'你的输入为{inp}')
inp()

def su(num):
    if num==2 or num==1:
        return 1
    return su(num-1)+su(num-2)
print(su(9))
def fib2(q):
    if q == 1 or q == 2:
        return 1
    return fib2(q-1)+fib2(q-2)
print(fib2(9))
def total(num):
    total=0
    for i in range(1,num):
        total+=i
    return total
print(total(9))
