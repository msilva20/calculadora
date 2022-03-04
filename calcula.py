
while True:
    numero_1 = input('Digite um número: ')
    operador = input('Digite um operador matemático: ')
    numero_2 = input('Digite outro número: ')

    if not numero_1.isdigit() and not numero_2.isdigit():
        print('Digite um número válido...')
        continue
        

    numero_1 = int(numero_1)
    numero_2 = int(numero_2)

    if operador == '+':
        print(numero_1 + numero_2)
        break 
    elif operador == '-':
        print(numero_1 - numero_2)
        break
    elif operador == '*':
        print(numero_1 * numero_2)
        break
    elif operador == '/':
        print(numero_1 / numero_2)
        break
    else:
        print('Por favor digite um operador válido!')
        continue
