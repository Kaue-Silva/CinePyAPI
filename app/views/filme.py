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


        return jsonify({"data":data, "cidade":cidade})

CinepyView.register(app)
