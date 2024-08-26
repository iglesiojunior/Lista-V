import vector_utils
import os

caminho_atual = os.getcwd()
arquivos_atuais = os.listdir(caminho_atual)

def verificar_estado_arquivo(nome_arquivo):
    nova_tentativa = nome_arquivo
    if nome_arquivo not in arquivos_atuais:
        print(" O arquivo foi digitado incorretamente, tente novamente!")
        nova_tentativa = inicialização_vetor_num()
        verificar_estado_arquivo(nova_tentativa)
    else:
        return  nova_tentativa

def inicialização_vetor_num():
    menu_secundario = """
    \t================================
    \t1 - Vetor com dados automáticos
    \t2 - Definir vetores
    \t3 - Ler arquivo
    \t================================
    """
    print(menu_secundario)
    opcao = int(input("\t>>>"))
    if(opcao == 1):
        tamanho = 0
        valor_min = 0
        valor_max = 0
        tamanho, valor_min, valor_max = vector_utils.my_map(int, input("\tInsira o tamanho e os valores min e max do vetor desejado:").split(" "))
        vetor_automatico = vector_utils.producao_vetor_automatico(tamanho, valor_min, valor_max)
        print(f"\t{vetor_automatico}")
        return vetor_automatico
    elif(opcao == 2):
        tamanho = 0
        valor_min = 0
        valor_max = 0
        tamanho, valor_min, valor_max = vector_utils.my_map(int, input("\tInsira o tamanho e os valores min e max do vetor desejado:").split(" "))
        vetor_manual = []
        vector_utils.adicionar_elemento_lista(vetor_manual, valor_min, valor_max)
        while(tamanho != 0):
            vector_utils.adicionar_elemento_lista(vetor_manual, valor_min, valor_max)
            tamanho-=1
        print(f"\t{vetor_manual}")
        return vetor_manual
    elif(opcao == 3):
        print("\tOs arquivos atuais do diretório atual são:")
        for arquivo in arquivos_atuais:
            if "txt" in arquivo:
                print(f"\t{arquivo}")
        selecao_arquivo = input("\tInsira o nome do programa que você deseja: ")
        arquivo_validado = verificar_estado_arquivo(selecao_arquivo)
        print(arquivo_validado)
        return arquivo_validado
    
def mostrar_valores_vetor(nome_vetor):
    print("""
    \t==========================================
    \tEstes são os valores do respectivo vetor:
    """)
    for valor in nome_vetor:
        print(f"\t{valor}")
    print("\t==========================================")

def mostrar_tamanho_arquivo(lista):
    print(f"\tO tamanho da lista atual é de: {len(lista)}")
    
def verificar_valor_min_e_max(lista):
    maior_numero = 0
    position_max_num = 0
    menor_numero = 0
    position_min_num = 0    
    for numero in range(0, len(lista)):
        for concorrentes in range(1, len(lista)):
            if lista[numero] > lista[concorrentes]:
                maior_numero = lista[numero]
                position_max_num = numero
                menor_numero = lista[concorrentes]
                position_min_num = concorrentes
            elif lista[numero] < lista[concorrentes]:
                maior_numero = lista[concorrentes]
                position_max_num = concorrentes
                menor_numero = lista[numero]
                position_min_num = numero
    return [maior_numero, menor_numero, position_max_num, position_min_num]

def mostrar_valores_positivos_negativos(lista):
    print("\t==============Valores Positivos:===============")
    for i in range(0, len(lista)):
        if lista[i] > 0:
            print(f"\t{lista[i]}")
    print("\t==============Valores Negativos:===============")
    for i in range(0, len(lista)):
        if lista[i] < 0:
            print(f"\t{lista[i]}")

def mostrar_valores_negativos_qtd(lista):
    print("\t==============Valores Negativos:===============")
    qtd_valores_negativos = 0
    for i in range(0, len(lista)):
        if lista[i] < 0:
            print(f"\t{lista[i]}")
            qtd_valores_negativos += 1
    print(f"\tA quantidade de números negativos na lista atual é de: {qtd_valores_negativos}")
    
def atualizar_valores_lista(lista):
    menu = """
    \t===================================================
    \t1 - Multiplicar todos valores
    \t2 - Elevar todos os valores
    \t3 - Reduzir a uma fração
    \t4 - Substituir valores negativos por num aleatório
    \t5 - Ordenar valores
    \t6 - Embaralhar valores
    \t
    \t0 - Voltar ao menu principal
    \t===================================================
    """
    print(menu)
    option = int(input("\t>>>"))
    if(option == 1):
        multiplicador = int(input("\tInsira o número que será o multiplicador dos itens da lista:"))
        lista_atualizada = vector_utils.my_map(lambda x : x*multiplicador, lista)
        print(f"\t{lista_atualizada}")
        return lista_atualizada
    if (option == 2):
        elevador = int(input("\tInsira o número que será o multiplicador dos itens da lista:"))
        lista_atualizada = vector_utils.my_map(lambda x : x**elevador, lista)
        print(f"\t{lista_atualizada}")
        return lista_atualizada
    if (option == 3):
        numerador = 0
        denominador = 0
        numerador, denominador = vector_utils.my_map(int, input("\tInsira a fração desejada separada por /(ex: 6/12)").split("/"))
        lista_atualizada = vector_utils.my_map(lambda x : x*(numerador/denominador), lista)
        print(f"\t{lista_atualizada}")
        return lista_atualizada
    if(option == 4):
        lista_atualizada = vector_utils.substituir_valores_negativos(lista)
        return lista_atualizada
    if (option == 5):
        lista_atualizada = vector_utils.ordenar_lista(lista)
        return lista_atualizada
    if (option == 6):
        lista_atualizada = vector_utils.embaralhar_lista(lista)
    
def adicionar_novos_valores_lista(lista: list):
    qtd_elemento = int(input("\tInsira a quantidade de elementos que deseja inserir na lista: "))
    while(qtd_elemento != 0):
        novo_elemento = int(input("\tInsira o novo elemento na lista: "))
        lista.append(novo_elemento)
        qtd_elemento-=1

def remover_valores_valor_exato(lista: list):
    qts_numero_desejado = int(input("Insira a qtd de números que você deseja remover: "))
    while(qts_numero_desejado != 0):
        elemento_selecionado = int(input("\tInsira o número que você deseja excluir: "))
        for i in range(0, len(lista)):
            if lista[i] == elemento_selecionado:
                del lista[i]
                break
            if elemento_selecionado not in lista:
                print("O Valor selecionado não foi encontrado!")
                remover_valores_valor_exato(lista)
            print(f"terminei a volta {i}")
        qts_numero_desejado-=1

def editar_posicao_especifico_posicao(lista):
    pass

def remover_valor_indice(lista):
    qtd_numeros_remover = int(input("\tInsira a quantidade de números que você deseja remover: "))
    while(qtd_numeros_remover != 0):
        posicao_elemento = int(input("Insira a posição do número desejado"))
        if posicao_elemento <= (len(lista)-1):
            del lista[posicao_elemento]
        else:
            continue
    
def salvar_arquivo(lista):
    with open("Resultado_listas.txt", "x") as arquivo_destino:
        for i in range(0, len(lista)):
            arquivo_destino.write(f"{lista[i]}\n")