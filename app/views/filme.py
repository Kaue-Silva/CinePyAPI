from datetime import datetime

from app import app
from flask import jsonify, request
from flask_classful import FlaskView, route

from ..controller.filme import EscolhaFilme


class CinepyView(FlaskView):
    route_base = '/api/cinepy'
    
    @route("/escolha_filme")
    def escolha_filme(self):
        # Obtendo parametros da Url
        cidade = request.args.get("cidade")
        data = request.args.get("data")
        # Convertendo data para tipo Data
        data = datetime.strptime(data, "%d%m%Y")
        try:
            # Executando Consulta
            filme = EscolhaFilme(data, cidade)
            # Acessando Pagina
            filme.pagina()
            # Obtendo Titulos dos Filmes
            filme.titulo()
            # Obtendo Todas as Datas de Estreia
            filme.data_estreia()
            # Filtrar os Filmes por Data e Selecionar Filme Aleatoriamente
            filme.filtrar_filmes()
            # Acessando Pagina do Filme
            filme.filme_pagina()
            # Obtendo Sinopse
            filme.sinopse()
            # Obtendo Diretor do Filme
            filme.diretor()
            # Obtendo Genero do Filme
            filme.genero()
            # Obtendo Capa e Convertendo em BASE64
            filme.capa()
            # Fechando Navegador
            filme.sair()
            
            # Obtendo todos os Dados Coletados
            filme = filme.filme_dados()
            # Retornando Dados como Json
            return jsonify(filme), 200
        except:
            # Tratamento de Erro
            return jsonify({"Error":"Ocorreu um Erro Inesperado"}), 500

# Registrando Rota
CinepyView.register(app)
