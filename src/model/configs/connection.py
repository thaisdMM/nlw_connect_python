from sqlalchemy import create_engine # para fazer uma engine de conexão
from sqlalchemy.orm import sessionmaker

#classe para organizar a conexão com o nosso banco de dados

class DBConnetionHandler:
   def __init__(self):
      self.__connection_string = "sqlite:///schema.db"  #__ privado; esse path mostra no sqlite aonde o banco de dados está
      self.__engine = self.__create_database_engine() #engine de conexão irá ser criado logo que for declarado um objeto, pois está no método construtor
      self.session = None

#__ privado método

   def __create_database_engine(self): #self mostra que está no contexto da class DBConnetionHandler
      engine = create_engine(self.__connection_string)
      return engine
   
   def __enter__(self):
      session_make = sessionmaker(bind=self.__engine) #criando a sessão com o mecanismo de conexão que foi colocado
      self.session = session_make()
      return self
   
   def __exit__(self, exc_type, exc_val, exc_tb): #exc é exception para tratar erros
      self.session.close()




