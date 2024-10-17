from lib.busca import carregar_palavras, comparar_buscas

arquivo = 'strings01milhao.txt'
palavras = carregar_palavras(arquivo)

palavra_busca = 'zzzqa'
comparar_buscas(palavras, palavra_busca)