import time
# -----------------------------------------------------------
list = [0,1]
Num1 = list[-1]
Num2 = list[-2]
NewFib = Num2 + Num1
a = len(list)
run = 1
# -----------------------------------------------------------
print("Введите n-ое число Фибоначчи: ")
MyFib = input()
# -----------------------------------------------------------
while run == 1:
    if a != MyFib:
        NewFib = Num2 + Num1
        list.append(NewFib)
        Num1 = list[-1]
        Num2 = list[-2]
        a = len(list)
        print()
        print(NewFib)
        time.sleep(0.1)
    if a == int(MyFib) + 1:
        print("Я его нашел! Число - ", list[-1])
        exit()
