# 1) Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.

# Criando um vetor vazio com tamanho 20
vetor = [0] * 20

# Realizando a leitura dos 20 números
for i in range(20):
    vetor[i] = int(input("Digite um número: "))

# Escrevendo os números lidos na ordem inversa
for i in range(19, -1, -1):
    print(vetor[i])
