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
            
            filme = filme.filme_dados()
            return jsonify(filme), 200
        except:
            return jsonify({"Error":"Ocorreu um Erro Inesperado"}), 500


CinepyView.register(app)
