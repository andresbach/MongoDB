# mydb.get_collection('mytable').find_one({"author": "Duke"})
# mydb.get_collection('mytable').find_one({"author": "blah"})

# base de dato > Colecciones > Documentos

from pymongo import MongoClient
from bson.objectid import ObjectId
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
        "incription" : datetime.datetime.utcnow(),
		'action_'+str(804): 5
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
mydb.persons.insert_many(nuevas_personas)

# esto es para que me entregue todo lo que esta en la coleccion. Poniendo 0 anula en el resultado
def devuelve_todos():
	for x in persons.find():
	#for x in persons.find({},{"_id":0, "name": 1, "account": 1}):
		print(x)
# ObjectId necesito primero el modulo, luego lo puedo usar para buscar
#id = persons.find_one({'_id': ObjectId("5b9abbdf7be477231f253c7d")})

# parametro es el que busca el valor, luego aCambiar es lo que voy a modificar por newValue. E.g.
# actualiza('account', '0x6f46cf5569aefa1acc1009290c8e043747172d89', 'action_804', persons.find_one({'account': '0x6f46cf5569aefa1acc1009290c8e043747172d89'})['action_804']+1)
def actualiza(searchParam, searchVal, toChange, newValue):
	#temp = persons.find_one({searchParam: searchVal})
	#temp[toChange] = newValue
	#persons.save(temp)
	#persons.replace_one(temp)
	persons.update_one({searchParam: searchVal},{'$set': {toChange: newValue}})
