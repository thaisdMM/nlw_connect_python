from sqlalchemy import func, desc #func> para contar no ranking de link; desc> ordem decrescente
from src.model.configs.connection import DBConnetionHandler
from src.model.entities.inscritos import Inscritos
from .interfaces.subscribers_repository import SubscribersRepositoryInterface


class SubscribersRepository(SubscribersRepositoryInterface):
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
         
         #busca
         
   def select_subscriber(self, email: str, evento_id: int) -> Inscritos:
      with DBConnetionHandler() as db:
         data  = (
            db.session
            .query(Inscritos)
            .filter(
               Inscritos.email == email, 
               Inscritos.evento_id == evento_id)
            .one_or_none()
         )
         return data

   #busca de quantas pessoas e quem são aqueles que se inscreveram a partir do link do inscrito

   def select_subscribers_by_link(self, link: str, event_id: int) -> list:
      with DBConnetionHandler() as db:
         data  = (
            db.session
            .query(Inscritos)
            .filter(
               Inscritos.link == link, 
               Inscritos.evento_id == event_id
            ).all()
         )
         return data
      
   #ranking de links - quem está em primeiro, segundo...; QUERY complexa

   def get_ranking(self, event_id: int) -> tuple:
      with DBConnetionHandler() as db:
         result = (
            db.session
            .query(
               Inscritos.link,
               func.count(Inscritos.id).label("total")
            )
            .filter(
               Inscritos.evento_id == event_id,
               Inscritos.link.isnot(None) #contar apenas as pessoas que entraram a partir de link: não pode ser nulo
            )
            .group_by(Inscritos.link) #agrupar por links, para contar o total
            .order_by(desc("total")) #ordem decrescente
            .all()
         )
         return result
