from classes import db

local = db.DB("./data/") #Instanciando a aplicação

local.mkDb("Loja") # Criando um db

local.useDb("Loja") #use db

local.mkData("Produtos")


