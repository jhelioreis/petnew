# -*- coding: latin-1 -*-
import traceback
from Model.Database import Database

class Client(object):
    """Classe que descreve o objeto Cliente"""

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
        
    def insertClient(self):
        """Insere um novo Cliente na base de dados."""
        
        #Se o produto foi criado sem um c�digo, providencio um novo c�digo.
        if self.code == None or self.code <= 0:
            self.code = nextCode()
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()

            #Executo a inser��o
            cursor.execute("INSERT INTO Client (code, name, docno, phone, cellphone, address, neighborhood, city, state) VALUES (" + str(self.code) + ", '" + str(self.name) + "', " + str(docno) + ", " + str(phone) + ", " + str(cellphone) + ", " + str(address) + ", " + str(neighborhood) + ", " + str(city) + ", " + str(state) + ")")
            
            #Gravo as altera��es
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
    
    def updateClient(self):
        """Atualiza as informa��es de um Cliente."""
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()
            
            #Executo o update
            cursor.execute("UPDATE Client SET name = '" + str(self.name) + "', docno = " + str(self.docno) +  "', phone = " + str(self.phone) +  "', cellphone = " + str(self.cellphone) +  "', address = " + str(self.address) +  "', neighborhood = " + str(self.neighborhood) +   "', city = " + str(self.city) +   "', state = " + str(self.state) + " WHERE code = " + str(self.code) + " ")
            
            #Gravo as altera��es
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
    
    def deleteClient(self):
        """Exclui um cliente da base de dados."""
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()

            #Executo a exclus�o
            cursor.execute("DELETE FROM Client WHERE code = " + str(self.code) + " ")                
            
            #Gravo as altera��es
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
    
    def selectClient(self, code):
        """Retorna informa��es de um Cliente"""
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()
            
            #Executo a sele��o
            cursor.execute("SELECT code, name, docno, phone, cellphone, address, neighborhood, city, state FROM Client WHERE code = " + str(code) + " ")
            
            #Preencho os dados do objeto com as informa��es retornadas
            for client in cursor:
                self.code = client[0]
                self.name = client[1]
                self.docno = client[2]
                self.phone = client[3]
                self.cellphone = client[4]
                self.address = client[5]
                self.neighborhood = client[6]
                self.city = client[7]
                self.state = client[8]
                        
            #Fecho o cursor
            cursor.close()
            
            #Retorno o objeto
            return self
        except:
            #Capturo a mensagem de erro
            error = traceback.format_exc()
            print(error)
            return False
    
    
    def selectAllClients(self):
        """Recupera todos os Clientes cadastrados no sistema"""        
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()
            
            #Executo o select
            cursor.execute("SELECT code, name, docno, phone, cellphone, address, neighborhood, city, state FROM Client")
            
            #Crio uma lista para armazenar os resultados
            clients = []
            
            #Preencho os dados do objeto com as informa��es retornadas
            for client in cursor:
                prod = Client(client[0], client[1], client[2], client[3], client[4], client[5], client[6], client[7], client[8])
                products.append(prod)

            #Fecho o cursor
            cursor.close()
            
            #Retorno a lista de objetos
            return clients
        except:
            #Capturo a mensagem de erro
            error = traceback.format_exc()
            print(error)
            return False
        
    def isNew(self):
        """Verifica se o Cliente � novo."""
                
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()
            
            #Executo o select
            cursor.execute("SELECT COUNT(*) FROM Client WHERE code = " + str(self.code) + " ")                
            
            #Guardo o n�mero de registros retornado
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
        """Verifico qual � o pr�ximo c�digo de Cliente dispon�vel."""
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()
            
            #Executo o select
            cursor.execute("SELECT MAX(code) FROM Client")                
            
            #Guardo o n�mero de registros retornado
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