#arquivo para gerenciar as informações dos inscritos

from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.model.repositories.interfaces.subscribers_repository import SubscribersRepositoryInterface

class SubscriberManager:
   def __init__(self, subscribers_repo: SubscribersRepositoryInterface):
      self.__subscribers_repo = subscribers_repo

   def get_subscribers_by_link(self, http_request: HttpRequest) -> HttpResponse:
      link = http_request.param["link"] #pegar dos parâmetros de url
      event_id = http_request.param["event_id"]
      subs = self.__subscribers_repo.select_subscribers_by_link(link, event_id)
      return self.__format_subs_by_link(subs)

#pega todos que foram inscritos a partir de um certo link e formata eles para retornar nome e email
   def __format_subs_by_link(self, subs: list) -> HttpResponse:
      formatted_subscriber = []
      for sub in subs: #para cada inscrito na lista de inscritos
         formatted_subscriber.append(
            {
               "nome": sub.nome,
               "email": sub.email,
            }
         )
      return HttpResponse(
         body={
            "data": {
               "Type": "Subscriber",
               "count": len(formatted_subscriber),
               "subscribers": formatted_subscriber
            }
         }
      )
