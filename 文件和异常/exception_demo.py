print("给我两个数字，我帮你算出他们的商值")
print('你需要退出就输入 q ')

while True:
    first_number = input("\n 第一个数：")
    if first_number == 'q':
        break
    second_number = input("\n 第二个数：")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("除数不能为0")
    else:
        print(answer)