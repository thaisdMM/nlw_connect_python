from flask import Blueprint, jsonify, request

subs_route_bp = Blueprint("subs_route", __name__)

from src.http_types.http_request import HttpRequest

from src.validators.subscribers_creator_validator import subscribers_creator_validator

from src.model.repositories.subscribers_repository import SubscribersRepository

from src.controllers.subscribers.subscribers_creator import SubscribersCreator


@subs_route_bp.route("/subscriber", methods=["POST"]) #Rota de criação de inscritos
def create_new_subs():

   subscribers_creator_validator(request) #validação
   htpp_request = HttpRequest(body=request.json) #tira o body da requisição. Coleta só que é necessário da framework

   subs_repo = SubscribersRepository() #criando a lógica e junto com o repositório do banco de dados
   subs_creator = SubscribersCreator(subs_repo) #criando a lógica e junto com o repositório do banco de dados

   http_response = subs_creator.create(htpp_request) #executando a lógica 

   return jsonify(http_response.body), http_response.status_code #retornando para o usuário uma informaçao