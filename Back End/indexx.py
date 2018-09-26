# -*- coding: latin-1 -*-
import web
from Controller.CategoryController import CategoryController
from Controller.ProducerController import ProducerController
from Controller.ClientController import ClientController
from Controller.ProductController import ProductController

urls = (
    '/categories', 'CategoryController',
    '/categories/(.*)', 'CategoryController',    
    '/products', 'ProductController',
    '/products/(.*)', 'ProductController',    
    '/clients', 'ClientController',
    '/clients/(.*)', 'ClientController',    
    '/producers', 'ProducerController',
    '/producers/(.*)', 'ProducerController'
    )

app = web.application(urls, globals())
    
if __name__ == "__main__": 
    app.run()