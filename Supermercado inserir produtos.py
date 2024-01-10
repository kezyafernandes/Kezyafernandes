#Programa para inserir dados na tabela usando Python
import sqlite3
from sqlite3 import Error
#Criar conexão com o BD
conexao=sqlite3.connect("Supermercado.db")
cursor=conexao.cursor()
 
ID=input("Digite o número de identificação do registro:")
nomedaseção=input("Digite o nome da seção:")
nomedoproduto=input("Digite o nome do produto:")
preçodoproduto=input("Digite o preço do produto:")
validadedoproduto=input("Digite a validade do produto:")
vsql="insert into Produtos(N_IDCONTATO,T_NOMEDASEÇÃO,T_NOMEDOPRODUTO,T_PREÇODOPRODUTO,T_VALIDADEDOPRODUTO)Values('"+ID+"','"+nomedaseção+"','"+nomedoproduto+"','"+preçodoproduto+"','"+validadedoproduto+"')"
 
#Inserir dados na tabela
def inserir(conexao,sql):
   try:
       c=conexao.cursor()
       c.execute(sql)
       conexao.commit()
       print("Registro inserido")
   except Error as ex:
       print(ex)
inserir(conexao,vsql)
