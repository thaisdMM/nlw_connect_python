from src.model.configs.connection import DBConnetionHandler
from src.model.entities.eventos import Eventos

class EventosRepository:
   def insert(self, event_name:str) -> None:
      with DBConnetionHandler() as db:
         try:
            new_event = Eventos(nome=event_name) #cria novo evento
            db.session.add(new_event) #adiciona o novo evento na sessao
            db.session.commit() #comita o novo evento
         except Exception as exception:
            db.session.rollback() #volta ao estado anterior se der algum erro
            raise exception
            
