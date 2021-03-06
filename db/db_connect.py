"""
This file contains some common MongoDB code.
"""
# from email import message
import os
import json
import pymongo as pm
from pymongo.server_api import ServerApi
import bson.json_util as bsutil


# all of these will eventually be put in the env:
user_nm = "oscarivan"
cloud_svc = "nfthome.jucs3.mongodb.net"
passwd = os.environ.get("MONGO_PASSWD", '')
cloud_mdb = "mongodb+srv"
db_params = "retryWrites=true&w=majority"

db_nm = 'chatDB'
if os.environ.get("TEST_MODE", ''):
    db_nm = "test_chatDB"

REMOTE = "0"
LOCAL = "1"

client = None


def get_client():
    """
    This provides a uniform way to get the client across all uses.
    Returns a mongo client object... maybe we shouldn't?
    Also set global client variable.
    """
    global client
    if os.environ.get("LOCAL_MONGO", REMOTE) == LOCAL:
        print("Connecting to Mongo locally.")
        client = pm.MongoClient()
    else:
        print("Connecting to Mongo remotely.")
        client = pm.MongoClient(f"mongodb+srv://oscarivan:{passwd}@"
                                + f"{cloud_svc}/{db_nm}?"
                                + "retryWrites=true&w=majority",
                                server_api=ServerApi('1'))
    return client


def fetch_one(collect_nm, filters={}):
    """
    Fetch one record that meets filters.
    """
    room = []
    ans = client[db_nm][collect_nm].find_one(filters)
    room.append(json.loads(bsutil.dumps(ans)))
    return room


def del_one(collect_nm, filters={}):
    """
    Fetch one record that meets filters.
    """
    return client[db_nm][collect_nm].delete_one(filters)


def fetch_all(collect_nm):
    all_docs = []
    for doc in client[db_nm][collect_nm].find():
        print('doc()', type(doc), doc)
        all_docs.append(json.loads(bsutil.dumps(doc)))
    return all_docs


def fetch_one_combo(collect_nm, filters={}):
    user = []
    ans = client[db_nm][collect_nm].find_one(filters)
    user.append(json.loads(bsutil.dumps(ans)))
    return user


def insert_doc(collect_nm, doc):
    client[db_nm][collect_nm].insert_one(doc)


def insert_msg(collect_nm, room_Name,
               messages, chatterName):
    client[db_nm][collect_nm].update_one({"roomName": room_Name},
                                         {'$push':
                                         {"messages":
                                          [chatterName, messages]}})


def fetch_all_msg(collect_nm, room_Name):
    '''
    print('fetch_all_msg',client[db_nm][collect_nm].find())
    ans = client[db_nm][collect_nm].find_one(
                                         {"roomName": room_Name})
    print('ans',ans)
    print('client[db_nm][collect_nm]   ------->    ',
          client[db_nm][collect_nm])
    print('client[db_nm][collect_nm].find()   -------> ',
          client[db_nm][collect_nm].find())
    '''
    print('main', room_Name)
    allMsgs = []
    for doc in client[db_nm][collect_nm].find():
        print('docMsg\n', doc)
        print(doc['roomName'])
        if(doc['roomName'] == room_Name):
            allMsgs = doc['messages']
    print('allMsgs', allMsgs)
    return allMsgs


def fetch_all_by_genre(collect_nm, genre):
    allRooms_by_genre = []
    for doc in client[db_nm][collect_nm].find():
        if(doc['genre'] == genre):
            allRooms_by_genre.append(json.loads(bsutil.dumps(doc)))
    return allRooms_by_genre
