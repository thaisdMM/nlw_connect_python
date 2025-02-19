from src.model.configs.connection import DBConnetionHandler
from src.model.entities.eventos import Eventos
from .interfaces.eventos_repository import EventosRepositoryInterface

class EventosRepository(EventosRepositoryInterface):
   def insert(self, event_name:str) -> None:
      with DBConnetionHandler() as db:
         try:
            new_event = Eventos(nome=event_name) #cria novo evento
            db.session.add(new_event) #adiciona o novo evento na sessao
            db.session.commit() #comita o novo evento
         except Exception as exception:
            db.session.rollback() #volta ao estado anterior se der algum erro, é recomendável em caso de inserção, alteração ou deleção no banco de dados
            raise exception
         
    #busca
         
   def select_event(self, event_name:str) -> Eventos:
      with DBConnetionHandler() as db:
         data  = (
            db.session
            .query(Eventos)
            .filter(Eventos.nome == event_name)
            .one_or_none()
         )
         return data


