# -*- coding: latin-1 -*-
import sqlite3

class Database():
    """Classe respons�vel por criar a base de dados se ela ainda n�o existir."""
    
    def __init__(self):
        """Construtor da classe"""
        #Conecta � base de dados
        self.conn = sqlite3.connect("petshow.db")        
        #Cria as tabelas
        self.createTables()
        
    def createTables(self):
        """Cria as tabelas necess�rias para a aplica��o."""
        try:
            #Crio um cursor para trabalhar com os dados
            cursor = self.conn.cursor()
        
            #Crio a tabela de categorias
            cursor.execute("CREATE TABLE IF NOT EXISTS Category (code INTEGER PRIMARY KEY, name TEXT)")
            
            #Crio a tabela de fornecedores
            cursor.execute("CREATE TABLE IF NOT EXISTS Producer (code INTEGER PRIMARY KEY, name TEXT, docno TEXT, phone TEXT, cellphone TEXT, address TEXT, neighborhood TEXT, city TEXT, state TEXT)")
            
            #Cria a tabela de cliente
            cursor.execute("CREATE TABLE IF NOT EXISTS Client (code INTEGER PRIMARY KEY, name TEXT, docno TEXT, phone TEXT, cellphone TEXT, address TEXT, neighborhood TEXT, city TEXT, state TEXT)")
                    
            #Cria a tabela de produtos
            cursor.execute("CREATE TABLE IF NOT EXISTS Product (code INTEGER PRIMARY KEY, name TEXT, category INTEGER, CONSTRAINT FK_Product_Category FOREIGN KEY (category) REFERENCES Category(code))")
            
            #Fa�o commit das altera��es
            self.conn.commit()
            
            #Fecho o cursor
            cursor.close()            
        except:
            # Se houver erro, envio a mensagem ao servidor como um log
            print("Erro ao criar a base de dados.")        