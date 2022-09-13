# функция для проверки натуральности числа
def simple_number(num):
    counter = 0 #счетчик количества делителей
    for i in range(1,num+1):
        if num%i==0:
            counter+=1
    return counter==2


n = int(input("Введите число\n"))
for i in range(1,n):
    if simple_number(i):
        print(i)
