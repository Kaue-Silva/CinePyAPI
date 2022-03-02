from .selenium_filmes.filme import EscolhaFilme

def escolha_filme(data, cidade):
    filme = EscolhaFilme(data, cidade)
    filme.pagina()
    filme.titulo()
    filme.data_estreia()
    filme.filtrar_filmes()
    filme.filme_pagina()
    filme.sinopse()
    filme.diretor()
    filme.genero()
    filme.capa()
    filme.sair()
    
    return filme.filme_dados()