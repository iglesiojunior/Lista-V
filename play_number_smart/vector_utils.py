import random

def producao_vetor_automatico(tamanho, min, max):
    contador = tamanho
    vetor_final = []
    while(contador != 0):
        prox_digito = random.randint(min, max)
        vetor_final.append(prox_digito)
        contador-=1
    return vetor_final

def adicionar_elemento_lista(lista: list[int], min, max):
    novo_elemento = int(input("\tInsira um novo elemento: "))
    novo_elemento_validado = validar_elemento(novo_elemento, min, max, lista)
    lista.append(novo_elemento_validado)
    
def validar_elemento(elemento, min, max, lista):
    if elemento > max or elemento < min:
        adicionar_elemento_lista(lista, min, max)
    else:
        return elemento

def substituir_valores_negativos(lista):
    valor_max = 0
    valor_min = 0
    valor_min, valor_max = my_map(int, input("\tInsira O valor mínimo e máximo permitido para substituir números negativos da lista: ").split(" ")) 
    for i in range(0, len(lista)):
        if lista[i] < 0:
            lista[i] = random.randint(valor_min, valor_max)
    return lista

def ordenar_lista(lista):
    for i in range(0, len(lista)):
        min_i = i
        for j in range(i+1, len(lista)):
            if lista[j] > lista[min_i]:
                min_i = j
        lista[i], lista[min_i] = lista[min_i], lista[i]
    print(f"\t{lista}")

def embaralhar_lista(lista):
    for i in range(0, len(lista)):
        indice_mudado = random.randint(i, len(lista)-1)
        lista[i], lista[indice_mudado] = lista[indice_mudado], lista[i]
    print("\t==============Lista de números embaralhados================")
    print(f"\t{lista}")

def my_map(funcion, interables):
    return [funcion(i) for i in interables]

def my_reduce(funcion, interables):
    reducao = 0
    for i in interables:
        reducao = funcion(i, reducao)
    return reducao