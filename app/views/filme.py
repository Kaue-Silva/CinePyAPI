from datetime import datetime

from app import app
from flask import jsonify, request
from flask_classful import FlaskView, route

from ..controller.filmes.escolha_filme import escolha_filme

class CinepyView(FlaskView):
    route_base = '/api/cinepy'
    
    @route("/escolha_filme")
    def escolher_filme(self):
        cidade = request.args.get("cidade")
        data = request.args.get("data")
        data = datetime.strptime(data, "%d%m%Y")
        try: 
            filme = escolha_filme(data=data, cidade=cidade)
            return jsonify(filme), 200
        except:
            return jsonify({"Error":"Ocorreu um Erro Inesperado"}), 500

# Registrando Rota
CinepyView.register(app)
