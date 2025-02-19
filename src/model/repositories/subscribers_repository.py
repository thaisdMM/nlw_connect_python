from src.model.configs.connection import DBConnetionHandler
from src.model.entities.inscritos import Inscritos


class SubscribersRepository:
   def insert(self, subscriber_infos:dict) -> None: #dict> dicionário (colação de elementos)
      with DBConnetionHandler() as db:
         try:
            #cria novo inscrito
            new_subscriber = Inscritos(
               nome=subscriber_infos.get("name"),
               email=subscriber_infos.get("email"),
               link=subscriber_infos.get("link"),                
               evento_id=subscriber_infos.get("evento_id"),
               ) 
            db.session.add(new_subscriber) #adiciona o novo inscrito na sessao
            db.session.commit() #comita o novo inscrito
         except Exception as exception:
            db.session.rollback() #volta ao estado anterior se der algum erro, é recomendável em caso de inserção, alteração ou deleção no banco de dados
            raise exception
         