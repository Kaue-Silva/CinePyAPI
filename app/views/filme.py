from datetime import datetime
from random import choice

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
        print(filme)
        return jsonify(filme)

CinepyView.register(app)
