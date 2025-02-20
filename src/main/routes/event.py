from flask import Blueprint, jsonify, request

#agregador de rotas de eventos, assim se tiver mais de uma rota aqui todas rodariam no server.py

event_route_bp = Blueprint("event_route", __name__)

from src.validators.events_creator_validator import events_creator_validator

from src.http_types.http_response import HttpResponse 
from src.http_types.http_request import HttpRequest

from src.controllers.events.events_creator import EventsCreator
from src.model.repositories.eventos_repository import EventosRepository

@event_route_bp.route("/event", methods=["POST"]) #Rota de criação de eventos
def create_new_event():

   events_creator_validator(request) #validação
   htpp_request = HttpRequest(body=request.json) #tira o body da requisição. Coleta só que é necessário da framework

   eventos_repo = EventosRepository()
   events_creator = EventsCreator(eventos_repo)

   response = events_creator.create(htpp_request)

   http_response = HttpResponse(body={"estou": "aqui" }, status_code=201) #lógica

   return jsonify(http_response.body), http_response.status_code #sempre vai querer esse retorno em todas as rotas