#Programa para atualizar dados da tabela usando Python
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
 
#Atualizar dados da tabela
def atualizar(conexao,sql):
   try:
       c=conexao.cursor()
       c.execute(sql)
       conexao.commit()
   except Error as ex:
       print(ex)
   finally:
       print("Registro atualizado")
           
vsql="update Contatos set T_NOMECONTATO='Karine' where N_IDCONTATO=1"
atualizar(conexao,vsql)
