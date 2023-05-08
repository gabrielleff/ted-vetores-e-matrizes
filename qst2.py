# 2) Faça um algoritmo para ler 10 números e armazenar em um vetor VET, verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram.

# Criando um vetor vazio com tamanho 10
vetor = [0] * 10

# Realizando a leitura dos 10 números
for i in range(10):
    vetor[i] = int(input("Digite um número: "))

# Criando um conjunto vazio para armazenar os números únicos
numeros_unicos = set()

# Criando um dicionário para armazenar as posições dos números repetidos
posicoes_repetidas = {}

# Percorrendo o vetor e verificando se há números repetidos
for i in range(len(vetor)):
    if vetor[i] in numeros_unicos:
        if vetor[i] in posicoes_repetidas:
            posicoes_repetidas[vetor[i]].append(i)
        else:
            posicoes_repetidas[vetor[i]] = [i]
    else:
        numeros_unicos.add(vetor[i])

# Escrevendo os números repetidos e suas posições
if not posicoes_repetidas:
    print("Não há números repetidos no vetor.")
else:
    for numero, posicoes in posicoes_repetidas.items():
        print("O número", numero, "se repete nas posições:", posicoes)