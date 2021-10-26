number = input("Selecione um número: ")
if (number.isnumeric()):
    number = int(number)
    if (number < 2):
        print ("Não é válido")
    else:
        for primo in range(2, number+1):
            divisor = 0
            for div in range(1, primo):
                if (primo%div == 0):
                    divisor += 1
        if (divisor < 2):
            print("primo")
        else:
            print("não é primo")
else:
    print ("Não é um número")
