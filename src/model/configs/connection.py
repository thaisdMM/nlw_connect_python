from sqlalchemy import create_engine # para fazer uma engine de conexão

#classe para organizar a conexão com o nosso banco de dados

class DBConnetionHandler:
   def __init__(self):
      self.__connection_string = "sqlite:///schema.db"  #__ privado; esse path mostra no sqlite aonde o banco de dados está
      self.__engine = self.__create_database_engine() #engine de conexão irá ser criado logo que for declarado um objeto, pois está no método construtor

#__ privado método

   def __create_database_engine(self): #self mostra que está no contexto da class DBConnetionHandler
      engine = create_engine(self.__connection_string)
      return engine

