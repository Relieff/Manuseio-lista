geral = []
peso = []
nome = []
pesadas = []
leves = []
maior = menor = 0

while True:
    nome.append(str(input('Digite a nome: ')))
    print()
    peso.append(int(input('Digite o peso: ')))
    print()
    resp = str(input('Deseja parar? \n ----> [S/N] ')).upper().strip()[0]
    if resp == 'S':
        print('Você escolheu parar.')
        print('Fim.')
        print('-'*20)
        break
    else:
        print('Certo, você escolheu continuar.')
        print()
        
geral.append(peso+nome)
total = len(nome)   # len() da lista [nome] para saber quantos elementos tem.

if total == 0:
    maior = menor = geral   #Se o numero de elementos da lista [nome] for igual a 0.
#O maior passa é igual ao menor que é igual a lista [geral].
else:
    maior = max(peso)
    menor = min(peso)
    pesadas = [nome[i] for i in range(len(peso)) if peso[i] == maior]
    leves = [nome[i] for i in range(len(peso)) if peso[i] == menor]

print(f'O total de pessoas cadrastradas foi de: {total} sendo elas: {nome}')
print(f'O maior peso foi de {maior}Kg sendo as pessoas {pesadas} e o menor peso foi de {menor}Kg sendo as pessoas {leves}')
print('Fim do teste.')
print('-'*20)