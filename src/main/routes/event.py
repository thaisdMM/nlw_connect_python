from flask import Blueprint, jsonify

#agregador de rotas de eventos, assim se tiver mais de uma rota aqui todas rodariam no server.py

event_route_bp = Blueprint("event_route", __name__)

from src.http_types.http_response import HttpResponse 

@event_route_bp.route("/event", methods=["POST"]) #Rota de criação de eventos
def create_new_event():

   http_response = HttpResponse(body={"estou": "aqui" }, status_code=201) #lógica

   return jsonify(http_response.body), http_response.status_code #sempre vai querer esse retorno em todas as rotas