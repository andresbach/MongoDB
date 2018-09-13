# mydb.get_collection('mytable').find_one({"author": "Duke"})
# mydb.get_collection('mytable').find_one({"author": "blah"})

# base de dato > Colecciones > Documentos

from pymongo import MongoClient
import datetime

# me conecta al servicio de mongo que por default esta ahi
client = MongoClient('mongodb://localhost:27017/')
# esto crea la base de datos que luego contenga a las colecciones
mydb = client['pruebaDB']

# vacio las colecciones "persons" de mi base pruebaDB (por si la tenia antes usada)
mydb.persons.drop()

# armo un post cualquiera sobre personas y sus caracteristicas
persona = {
        "name": "Juan Topo",
        "title" : "Historiador",
        "tags" : ["WWII", "Peronismo", "Alunizaje"],
		"account" : "0x6f46cf5569aefa1acc1009290c8e043747172d89",
		"birthday" : datetime.datetime(1995,3,20),
		# "date": datetime.datetime(2016, 8, 11, 12, 30, 40, 330740)}
        "incription" : datetime.datetime.utcnow()
        }

# acceso directo a esa coleccion particular de la base de datos
persons = mydb.persons
# para insertar solo un documento uso
persons_id = persons.insert_one(persona)

# me devuelve donde esta guardado
print(persons_id)
# con eso puedo ver dentro de mi base de datos (pruebaDB) cuales son las colecciones dentro
print(mydb.list_collection_names())

# agrego a dos personas juntas al mismo tiempo usando tupla
nuevas_personas = [{
					"name": "Maria Juana",
					"title" : "Bailarina",
					"tags" : ["Clasica", "Contemporanea"],
					"account" : "0xfe9e8709d3215310075d67e3ed32a380ccf451c8",
					"birthday" : datetime.datetime(1997,2,12),
					"incription" : datetime.datetime.utcnow()
					},
					{
					"name": "Juan Pablo",
					"title" : "Programador",
					"tags" : ["C++", "SQL", "Python", "Solidity"],
					"account" : "0xe853c56864a2ebe4576a807d26fdc4a0ada51919",
					"birthday" : datetime.datetime(1985,1,1),
					"incription" : datetime.datetime.utcnow()
					}
					]

# las ingreso con el insert de many
mydb.posts.insert_many(new_posts)
