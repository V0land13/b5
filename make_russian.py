def make_russian(chislo):
    """
    принимает на вход число, а в ответ выдает строку "x студент(а/ов)" в соответствующем склонении
    """
    if len(str(chislo)) > 2:
        chislo_rabochee = int(str(chislo)[len(str(chislo))-2] + str(chislo)[len(str(chislo))-1])
    else:
        chislo_rabochee = chislo

    str_chislo_rabochee = str(chislo_rabochee)
    print(chislo_rabochee, str_chislo_rabochee)

    if len(str_chislo_rabochee) == 1:
        if chislo_rabochee == 1:
            frase = " студент"
        elif chislo_rabochee > 4  or chislo_rabochee == 0:
            frase = " студентов"
        else:
            frase = " студента"
    if len(str_chislo_rabochee) == 2:
        if chislo_rabochee < 21:
            frase = " студентов"
        else:
            if int(str_chislo_rabochee[1]) == 1:
                frase = " студент"
            elif  int(str_chislo_rabochee[1]) > 4 or int(str_chislo_rabochee[1]) == 0:
                frase = " студентов"
            else:
                frase = " студента"
    return "{}{}".format(chislo, frase)

chislo = int(input("Введи число для формирования строки: "))
print(make_russian(chislo))