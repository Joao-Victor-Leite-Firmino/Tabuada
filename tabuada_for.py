tabuada = int(input(f'Digite um número para exibir a tabuada: '))
print(f'Tabuada do número {tabuada}')
for valor in range (1,11,1):
    print(f' {str(tabuada)} x {str(valor)} = {str(tabuada*valor)}')