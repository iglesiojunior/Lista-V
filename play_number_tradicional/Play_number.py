import vector_features

def mostrar_menu():
    menu = """
   \t============Play Numbers==============
   \t1 - Inicializar Vetor Numérico
   \t2 - Mostrar todos os Valores
   \t3 - Resetar Valor
   \t4 - Ver Quantidade de itens no vetor
   \t5 - Ver Menor e Maior valores e suas posições
   \t6 - Somatório dos Valores
   \t7 - Média dos valores
   \t8 - Mostrar Valores Positivos e Negativos
   \t9 - Mostrar Valores Negativos e Suas Quantidades
   \t10 - Atualizar todos os valores
   \t11 - Adicionar Novos Valores
   \t12 - Remover itens por Valor Exato
   \t13 - Remover por Posição
   \t14 - Editar valor específico por Posição
   \t15 - Salvar valores em arquivo
   \t
   \t0 - Sair do programa
   \t=======================================
    """
    print(menu)
    opcao = int(input("\t>>>"))
    return opcao

def main():
    nova_opcao = mostrar_menu()
    while(nova_opcao != 0):
        if(nova_opcao == 1):
            vetor_resultante = vector_features.inicialização_vetor_num()
            print("\tArquivo Carregado com sucesso!!")
            nova_opcao = mostrar_menu()
        if(nova_opcao == 2):
            vector_features.mostrar_valores_vetor(vetor_resultante)
            nova_opcao = mostrar_menu()
        if(nova_opcao == 3):
            pass
        if(nova_opcao == 4):
            vector_features.mostrar_tamanho_arquivo(vetor_resultante)
            nova_opcao = mostrar_menu()
        if (nova_opcao == 5):
            valores_min_max = vector_features.verificar_valor_min_e_max(vetor_resultante)
            print(f"""
\t=====================================================
\tMaior número: {valores_min_max[0]} posição na lista: {valores_min_max[2]}
\tMenor número: {valores_min_max[1]} posição na lista: {valores_min_max[3]}
\t=====================================================
                  """)
            nova_opcao = mostrar_menu()
        if (nova_opcao == 6):
            resultado_somatorio = vector_features.somar_valores_vetores(vetor_resultante)
            print(f"""
\t=======================================
\tA somatório da lista atual é de: {resultado_somatorio}
\t=======================================
                  """)
            nova_opcao = mostrar_menu()
        if (nova_opcao == 7):
            resultado_somatorio = vector_features.somar_valores_vetores(vetor_resultante)
            media = resultado_somatorio/len(vetor_resultante)
            print(f"""
\t=================================================
\tA média dos valores da lista atual é de: {media}
\t=================================================
                  """)
            nova_opcao = mostrar_menu()
        if (nova_opcao == 8):
            vector_features.mostrar_valores_positivos_negativos(vetor_resultante)
            nova_opcao = mostrar_menu()
        if (nova_opcao == 9):
            vector_features.mostrar_valores_negativos_qtd(vetor_resultante)
            nova_opcao = mostrar_menu()
        if (nova_opcao == 10):
            vector_features.atualizar_valores_lista(vetor_resultante)
            nova_opcao = mostrar_menu()
        if(nova_opcao == 11):
            vector_features.adicionar_novos_valores_lista(vetor_resultante)
            nova_opcao = mostrar_menu()
        if(nova_opcao == 12):
            vector_features.remover_valores_valor_exato(vetor_resultante)
            nova_opcao = mostrar_menu()
        if(nova_opcao == 13):
            vector_features.remover_valor_indice(vetor_resultante)
            nova_opcao = mostrar_menu()
        if (nova_opcao == 14):
            vector_features.editar_posicao_especifico_posicao(vetor_resultante)
        if(nova_opcao == 15):
            vector_features.salvar_arquivo(vetor_resultante)
            nova_opcao = mostrar_menu()
    vector_features.salvar_arquivo(vetor_resultante)
            
main()