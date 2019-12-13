# message = input('告诉我一些信息，我将会给你答复\n')
# print('你输入了：' + message)

sandwich_orders = ['奶油三明治', '蜂蜜三明治', '白糖三明治','自制三明治']
finished_sandwich = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('做出了：'+sandwich)
    finished_sandwich.append(sandwich)

for sandwich in finished_sandwich:
    print(sandwich)

sandwich_orders = ['pastrami','奶油三明治', '蜂蜜三明治', 'pastrami',
                   '白糖三明治','pastrami','自制三明治','pastrami']


print('pastrami 卖完了')
print(sandwich_orders)
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
for sandwich in sandwich_orders:
    print(sandwich)



