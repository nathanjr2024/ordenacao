import time

def carregar_palavras(arquivo):
    """
    Lê o arquivo e retorna uma lista de palavras.
    """
    try:
        with open(arquivo, 'r') as f:
            palavras = f.read().splitlines()  # Lê cada linha e remove o '\n'
        return palavras
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
        return []

def busca_linear(lista, alvo):
    """
    Implementa a busca linear para encontrar a palavra alvo.
    """
    for i, palavra in enumerate(lista):
        if palavra == alvo:
            return i
    return -1  # Palavra não encontrada

def busca_binaria(lista, alvo):
    """
    Implementa a busca binária para encontrar a palavra alvo.
    """
    esquerda, direita = 0, len(lista) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        palavra_meio = lista[meio]
        
        if palavra_meio == alvo:
            return meio  # Retorna o índice onde a palavra foi encontrada
        elif palavra_meio < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    
    return -1  # Palavra não encontrada

def comparar_buscas(lista, palavra_busca):
    """
    Compara os tempos de execução das buscas linear e binária.
    """
    # Busca Linear
    inicio_linear = time.time()
    resultado_linear = busca_linear(lista, palavra_busca)
    fim_linear = time.time()
    tempo_linear = fim_linear - inicio_linear

    # Busca Binária
    inicio_binaria = time.time()
    resultado_binaria = busca_binaria(lista, palavra_busca)
    fim_binaria = time.time()
    tempo_binaria = fim_binaria - inicio_binaria

    # Exibir resultados
    print(f"\nResultado da busca linear:")
    if resultado_linear != -1:
        print(f"Palavra '{palavra_busca}' encontrada no índice {resultado_linear}.")
    else:
        print(f"Palavra '{palavra_busca}' não encontrada.")
    print(f"Tempo de execução: {tempo_linear:.6f} segundos")

    print(f"\nResultado da busca binária:")
    if resultado_binaria != -1:
        print(f"Palavra '{palavra_busca}' encontrada no índice {resultado_binaria}.")
    else:
        print(f"Palavra '{palavra_busca}' não encontrada.")
    print(f"Tempo de execução: {tempo_binaria:.6f} segundos")