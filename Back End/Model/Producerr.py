# -*- coding: latin-1 -*-
import traceback
from Model.Database import Database

class Producer(object):
    """Classe que descreve o objeto Fornecedor"""

    def __init__(self, code = 0, name = "", docno = "", phone = "", cellphone = "", address = "", neighborhood = "", city = "", state = ""):
        """Construtor da classe"""
        if code == 0:
            self.code = nextCode()
        else:
            self.code = code
        self.name = name        
        self.docno = docno
        self.phone = phone
        self.cellphone = cellphone
        self.address = address
        self.neighborhood = neighborhood
        self.city = city
        self.state = state
        
    def insertProducer(self):
        """Insere um novo fornecedor na base de dados."""
        
        #Se o produto foi criado sem um código, providencio um novo código.
        if self.code == None or self.code <= 0:
            self.code = nextCode()
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()

            #Executo a inserção
            cursor.execute("INSERT INTO Producer (code, name, docno, phone, cellphone, address, neighborhood, city, state) VALUES (" + str(self.code) + ", '" + str(self.name) + "', " + str(docno) + ", " + str(phone) + ", " + str(cellphone) + ", " + str(address) + ", " + str(neighborhood) + ", " + str(city) + ", " + str(state) + ")")
            
            #Gravo as alterações
            database.conn.commit()
            
            #Fecho o cursor
            cursor.close()
            
            #Retorno OK 
            return str(True)
        except:
            #Capturo a mensagem de erro
            error = traceback.format_exc()
            print(error)
            return str(False)
    
    def updateProducer(self):
        """Atualiza as informações de um fornecedor."""
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()
            
            #Executo o update
            cursor.execute("UPDATE Producer SET name = '" + str(self.name) + "', docno = " + str(self.docno) +  "', phone = " + str(self.phone) +  "', cellphone = " + str(self.cellphone) +  "', address = " + str(self.address) +  "', neighborhood = " + str(self.neighborhood) +   "', city = " + str(self.city) +   "', state = " + str(self.state) + " WHERE code = " + str(self.code) + " ")
            
            #Gravo as alterações
            database.conn.commit()
            
            #Fecho o cursor
            cursor.close()
            
            #Retorno OK 
            return True
        except:
            #Capturo a mensagem de erro
            error = traceback.format_exc()
            print(error)
            return False
    
    def deleteProducer(self):
        """Exclui um produtor da base de dados."""
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()

            #Executo a exclusão
            cursor.execute("DELETE FROM Producer WHERE code = " + str(self.code) + " ")                
            
            #Gravo as alterações
            database.conn.commit()
                        
            #Fecho o cursor
            cursor.close()
            
            #Retorno OK 
            return True
        except:
            #Capturo a mensagem de erro
            error = traceback.format_exc()
            print(error)
            return False
    
    def selectProducer(self, code):
        """Retorna informações de um fornecedor"""
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()
            
            #Executo a seleção
            cursor.execute("SELECT code, name, docno, phone, cellphone, address, neighborhood, city, state FROM Producer WHERE code = " + str(code) + " ")
            
            #Preencho os dados do objeto com as informações retornadas
            for producer in cursor:
                self.code = producer[0]
                self.name = producer[1]
                self.docno = producer[2]
                self.phone = producer[3]
                self.cellphone = producer[4]
                self.address = producer[5]
                self.neighborhood = producer[6]
                self.city = producer[7]
                self.state = producer[8]
                        
            #Fecho o cursor
            cursor.close()
            
            #Retorno o objeto
            return self
        except:
            #Capturo a mensagem de erro
            error = traceback.format_exc()
            print(error)
            return False
    
    
    def selectAllProducer(self):
        """Recupera todos os fornecedores cadastrados no sistema"""        
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()
            
            #Executo o select
            cursor.execute("SELECT code, name, docno, phone, cellphone, address, neighborhood, city, state FROM Producer")
            
            #Crio uma lista para armazenar os resultados
            producers = []
            
            #Preencho os dados do objeto com as informações retornadas
            for producer in cursor:
                prod = Producer(producer[0], producer[1], producer[2], producer[3], producer[4], producer[5], producer[6], producer[7], producer[8])
                products.append(prod)

            #Fecho o cursor
            cursor.close()
            
            #Retorno a lista de objetos
            return producers
        except:
            #Capturo a mensagem de erro
            error = traceback.format_exc()
            print(error)
            return False
        
    def isNew(self):
        """Verifica se o fornecedor é novo."""
                
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()
            
            #Executo o select
            cursor.execute("SELECT COUNT(*) FROM Producer WHERE code = " + str(self.code) + " ")                
            
            #Guardo o número de registros retornado
            count = cursor.fetchone()[0]
            
            #Fecho o cursor
            cursor.close()
            
            #Retorno a lista de objetos
            return count <= 0
        except:
            #Capturo a mensagem de erro
            error = traceback.format_exc()
            print(error)
            return False
            
    def nextCode(self):
        """Verifico qual é o próximo código de fornecedor disponível."""
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()
            
            #Executo o select
            cursor.execute("SELECT MAX(code) FROM Producer")                
            
            #Guardo o número de registros retornado
            count = cursor.fetchone()[0]
            
            #Fecho o cursor
            cursor.close()
            
            #Retorno a lista de objetos
            return count + 1
        except:
            #Capturo a mensagem de erro
            error = traceback.format_exc()
            print(error)
            return 0