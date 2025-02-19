from src.model.configs.base import Base
from sqlalchemy import Column, String, Integer

class Eventos(Base):
   __tablename__ = "Eventos" #classe eventos está relacionada a tabela de enventos no banco de dados

   id = Column(Integer, primary_key=True, autoincrement=True)
   nome = Column(String, nullable=False)
