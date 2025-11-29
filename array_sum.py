#Nós podemos gerar sequências de números através da função range(). Por exemplo, range(10) irá gerar números de 0 até 9 (10 números). 
# A função range() também nos permite definir o começo da nossa sequência, o fim e os passos que serão dados como por exemplo range(começo,fim,passos), 
# caso não venhamos a definir os passos, o padrão é que seja de 1 em 1.

lista = []
resposta = 's'
while resposta == 's':
    valor = input('digite o valor que quer adicionar na lista')
    lista.append(valor)
    resposta = input('deseja adicionar um valor na lista? (s/n)')


def sum_lista(lista):
    sum = 0
    for l in lista:
        sum += int(l)
    print(f'a soma é {sum} pangaré')
    return sum

sum_lista(lista)


