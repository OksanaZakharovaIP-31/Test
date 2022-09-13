def check_bracket(list,first_sign,second_sign):
    kol1 = 0
    for i in list:
        if i ==second_sign:
            kol1-=1
        elif i==first_sign:
            kol1+=1
        if kol1==-1:
            return False

    return kol1==0


def chekc_string(s):
    '''Будет рассматриваться 3 вида скоробок - круглые (), фигурные {} и квадратные [], так как по заданию не было указано
    с какими именно нужно работать'''
    open_bracket = ['(','{','[']
    close_bracket=[')','}',']']
    #Создаем из строки список только со скобочками, чтобы в альнейшем было проще работать
    list = [i for i in s if i in open_bracket or i in close_bracket]
    first_check = check_bracket(list,open_bracket[0],close_bracket[0])
    second_check = check_bracket(list,open_bracket[1],close_bracket[1])
    third_check = check_bracket(list,open_bracket[2],close_bracket[2])
    if first_check and second_check and third_check:
        print("Правильная скобочная последовательность")
    else:
        print("Неправильная скобочная последовательность")
   

    


stroka = input("Введите строку\n")
chekc_string(stroka)