from src.model.repositories.interfaces.eventos_repository import EventosRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

#interagir a class com o banco usando as interfaces
class EventsCreator:
   def __init__(self, events_repo: EventosRepositoryInterface):
      self.__events_repo = events_repo
   
   #as informações data e name ele está tirando do body do Postman
   def create(self, http_request: HttpRequest) -> HttpResponse:
      events_info = http_request.body["data"]
      event_name = events_info["name"]

      self.__check_event(event_name)
      self.__insert_event(event_name)
      return self.__format_response(event_name)

#método de verificação
   def __check_event(self, event_name: str) -> None: 
      response = self.__events_repo.select_event(event_name)
      if response: raise Exception("Event Already Exists!")

   def __insert_event(self, event_name: str) -> None:
      self.__events_repo.insert(event_name)

   def __format_response(self, event_name: str) ->HttpResponse:
      return HttpResponse(
         #body mais personalizado para ser chamado em um front-end
         body={
            "data": {
               "Type": "Event",
               "count": 1,
               "atributes":{
                  "event_name": event_name
               }
            }
         },
         status_code=201
      )
