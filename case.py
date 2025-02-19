#Esse arquivo case.py é para ilustrar o que ele quer fazer com a classe de conexão no connection.py
#métodos especiais da classe de python

#Se entrar no with, enter é executado primeiro e o exit por ultimo. 
class MinhaClasse:
   def __enter__(self):
      print("Entrei!!!")

   def __exit__(self, exc_type, exc_val, exc_tb):
      print("Saí!!!")

with MinhaClasse() as mc:
   print("Estou aqui dentro!")