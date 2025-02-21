import random
from src.model.configs.connection import DBConnetionHandler
from src.model.entities.eventos_link import EventosLink
from .interfaces.eventos_link_repository import EventosLinkRepositoryInterface

class EventosLinkRepository(EventosLinkRepositoryInterface):
   def insert(self, event_id: int, subscriber_id: int) -> str:
      with DBConnetionHandler() as db:
         try: 
            link_final = ''.join(random.choices('0123456789', k=7)) #pegando a string vazia e colocando uma escolha aleatória de 7 números
            formatted_link = f'evento-{event_id}-{subscriber_id}-{link_final}'

            #cria novo evento
            new_events_link = EventosLink(
               evento_id = event_id,
               inscrito_id = subscriber_id,
               link = formatted_link
               )
   
            db.session.add(new_events_link) #adiciona o novo evento na sessao
            db.session.commit() #comita o novo evento

            return formatted_link #quando iserir o link, vai retornar o link de volta
         except Exception as exception:
            db.session.rollback() #volta ao estado anterior se der algum erro, é recomendável em caso de inserção, alteração ou deleção no banco de dados
            raise exception
         
    #busca
         
   def select_events_link(self, event_id: int, subscriber_id: int) -> EventosLink: # se olharmos de trás para frente: verifica se para um inscrito em um dado evento se existe um link.
      with DBConnetionHandler() as db:
         data  = (
            db.session
            .query(EventosLink)
            .filter(
               EventosLink.evento_id == event_id,
               EventosLink.inscrito_id == subscriber_id
               )
            .one_or_none()
         )
         return data


