from filme import EscolhaFilme

def escolha_filme(data, cidade):
    filme = EscolhaFilme(data, cidade)
    filme.pagina()
    filme.filmes_sorteio()
    filme.filme_selecionado()
    
    # filme.data_estreia()
    # filme.filtrar_filmes()
    
    filme.filme_pagina()
    filme.sinopse()
    filme.diretor()
    filme.genero()
    # filme.capa()
    filme.sair()
    
    return filme.filme_dados()

print(escolha_filme("20042022", "rio_de_janeiro"))