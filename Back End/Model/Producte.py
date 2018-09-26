# -*- coding: latin-1 -*-
import traceback
from Model.Database import Database
from Model.Category import Category

class Product(object):
    """Classe que descreve o objeto Produto"""

    def __init__(self, code = 0, name = "", category = None):
        """Construtor da classe"""
        if code == 0:
            self.code = nextCode()
        else:
            self.code = code
        self.name = name        
        self.category = category
        
    def insertProduct(self):
        """Insere um novo produto na base de dados."""
        
        #Se o produto foi criado sem um código, providencio um novo código.
        if self.code == None or self.code <= 0:
            self.code = nextCode()
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()

            #Executo a inserção
            cursor.execute("INSERT INTO Product (code, name, category) VALUES (" + str(self.code) + ", '" + str(self.name) + "', " + str(self.category.code) + ")")
            
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
    
    def updateProduct(self):
        """Atualiza as informações de um produto."""
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()
            
            #Executo o update
            cursor.execute("UPDATE Product SET name = '" + str(self.name) + "', category = " + str(self.category.code) + " WHERE code = " + str(self.code) + " ")
            
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
    
    def deleteProduct(self):
        """Exclui um produto da base de dados."""
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()

            #Executo a exclusão
            cursor.execute("DELETE FROM Product WHERE code = " + str(self.code) + " ")                
            
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
    
    def selectProduct(self, code):
        """Retorna informações de um produto"""
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()
            
            #Executo a seleção
            cursor.execute("SELECT code, name, category FROM Product WHERE code = " + str(code) + " ")
            
            #Preencho os dados do objeto com as informações retornadas
            for product in cursor:
                self.code = product[0]
                self.name = product[1]
                self.category = Category().selectCategory(product[2])
                        
            #Fecho o cursor
            cursor.close()
            
            #Retorno o objeto
            return self
        except:
            #Capturo a mensagem de erro
            error = traceback.format_exc()
            print(error)
            return False
    
    
    def selectAllProducts(self):
        """Recupera todos os produtos cadastrados no sistema"""        
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()
            
            #Executo o select
            cursor.execute("SELECT code, name, category FROM Product")
            
            #Crio uma lista para armazenar os resultados
            products = []
            
            #Preencho os dados do objeto com as informações retornadas
            for product in cursor:
                prod = Product(product[0], product[1], Category().selectCategory(product[2]))
                products.append(prod)

            #Fecho o cursor
            cursor.close()
            
            #Retorno a lista de objetos
            return products
        except:
            #Capturo a mensagem de erro
            error = traceback.format_exc()
            print(error)
            return False
        
    def isNew(self):
        """Verifica se o produto é novo."""
                
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()
            
            #Executo o select
            cursor.execute("SELECT COUNT(*) FROM Product WHERE code = " + str(self.code) + " ")                
            
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
        """Verifico qual é o próximo código de produto disponível."""
        
        #Instancio a classe banco
        database = Database()
        
        try:
            #Crio um cursor para acessar o banco de dados
            cursor = database.conn.cursor()
            
            #Executo o select
            cursor.execute("SELECT MAX(code) FROM Product")                
            
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