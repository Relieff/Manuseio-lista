#for valor in range(0, 4):
numero = (int(input('Digite um valor:')), int(input('Digite um valor:')), int(input('Digite um valor:')),int(input('Digite um valor:')))

pos = numero.index(3)
rept = numero.count(9)

print(f'Você digitou os números {numero}')
print(f'O número 9 repetiu {rept} vezes')

if 3 in numero:
    print(f'O primeiro valor 3 digitado está na posição {pos} ')
else:
    print('O valor 3 não foi digitado')

print('Os valores pares digitados foram:', end='')

for n in numero:
    if n % 2 == 0:
        print(n, end=' ')
