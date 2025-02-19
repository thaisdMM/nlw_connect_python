from abc import ABC, abstractmethod
from src.model.entities.eventos import Eventos

class EventosRepositoryInterface(ABC):

#esses método é bom pq consegue descrever tudo que tem na classe de eventos
   @abstractmethod #com esse método a classe que recebe ABC como herança é obrigatoria passar o insert
   def insert(self, event_name:str) -> None: pass
   @abstractmethod #com esse método a classe que recebe ABC como herança é obrigatoria passar o select
   def select_event(self, event_name:str) -> Eventos: pass

# classe abstrata nao pode ter o objeto abaixo, daria erro
#obj = EventosRepositoryInterface()