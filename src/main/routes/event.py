from flask import Blueprint, jsonify

#agregador de rotas de eventos, assim se tiver mais de uma rota aqui todas rodariam no server.py

event_route_bp = Blueprint("event_route", __name__)

@event_route_bp.route("/event", methods=["POST"]) #Rota de criação de eventos
def create_new_event():
   return jsonify({"estou": "aqui" }), 201