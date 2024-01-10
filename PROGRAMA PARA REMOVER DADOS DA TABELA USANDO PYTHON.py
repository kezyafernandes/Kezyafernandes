#Programa para remover dados da tabela usando Python
import sqlite3
from sqlite3 import Error
#Criar conexão com o BD
conexao=sqlite3.connect("Agenda.db")
cursor=conexao.cursor()
 
def inserir(conexao,sql):
   try:
       c=conexao.cursor()
       c.execute(sql)
       conexao.commit()
       print("Registro inserido")
   except Error as ex:
       print(ex)
 
#Remover dados da tabela
def remover(conexao,sql):
   try:
       c=conexao.cursor()
       c.execute(sql)
       conexao.commit()
   except Error as ex:
       print(ex)
   finally:
       print("Registro removido")
           
vsql="delete from Contatos where T_EMAILCONTATO= 'LUIZ@GMAIL.COM'"
remover(conexao,vsql)
