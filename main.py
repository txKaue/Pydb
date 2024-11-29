from classes import db

db.mkDb("Loja") # equivalente ao create db ""

db = db.useDb("loja") # equivalente ao use database

db.rmDb(db) # equivalente ao drop db


#db.mkData("Loja", "Usuarios") #use database + create table
