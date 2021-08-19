a = float(input('Escolha um número:'))
b = float(input('Escolha mais um número:'))

while True:
    print("""
[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir
[5] Mudar os números
[6] Sair
""")
    c = int(input('O que deseja fazer:'))

    if c == 1:
        print(f'{a} + {b} = {a+b}')
        per = input('Deseja continuar?:')
        if per == 'n':
            break
    elif c == 2:
        print(f'{a} - {b} = {a-b}')
        per = input('Deseja continuar?:')
        if per == 'n':
            break
    elif c == 3:
        print(f'{a} x {b} = {a*b}')
        per = input('Deseja continuar?:')
        if per == 'n':
            break
    elif c == 4:
        print(f'{a} ÷ {b} = {a/b}')
        per = input('Deseja continuar?:')
        if per == 'n':
            break
    elif c == 5:
        a = float(input('Escolha um número:'))
        b = float(input('Escolha mais um número:'))
    elif c == 6:
        break
