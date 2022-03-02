"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""

# from email import message
import os

import db.db_connect as dbc

DEMO_HOME = os.environ["NFT_HOME"]

# names of our collections
ROOMS = "rooms"
USERS = "users"
MESSAGES = "messages"

# field names in our DB:
USER_NM = "userName"
PASSWORD_NM = "password"
ROOM_NM = "roomName"
GENRE_NM = "genre"
NUM_USERS = "num_users"
MESSAGES_NM = "messages"

OK = 0
NOT_FOUND = 1
DUPLICATE = 2


client = dbc.get_client()
if client is None:
    print("Failed to connect to MongoDB.")
    exit(1)


def get_rooms():
    """
    A function to return a dictionary of all rooms.
    """
    return dbc.fetch_all(ROOMS)


def room_exists(roomname):
    """
    See if a room with roomname is in the db.
    Returns True of False.
    """
    rec = dbc.fetch_one(ROOMS, filters={ROOM_NM: roomname})
    print(f"{rec=}")
    return rec is not None


def del_room(roomname):
    """
    Delete roomname from the db.
    """
    if not room_exists(roomname):
        return NOT_FOUND
    else:
        dbc.del_one(ROOMS, filters={ROOM_NM: roomname})
        return OK


def add_room(roomname, genre):
    """
    Add a room to the room database.
    """
    print(f"{roomname=}")
    if room_exists(roomname):
        return DUPLICATE
    else:
        dbc.insert_doc(ROOMS, {ROOM_NM: roomname, GENRE_NM: genre,
                               NUM_USERS: 0, MESSAGES_NM: []})
        return OK


def user_exists(username):
    """
    See if a user with username is in the db.
    Returns True of False.
    """
    rec = dbc.fetch_one(USERS, filters={USER_NM: username})
    print(f"{rec=}")
    return rec is not None


def get_users():
    """
    A function to return a dictionary of all users.
    """
    return dbc.fetch_all(USERS)


def add_user(username, password):
    """
    Add a user to the user database.
    Until we are using a real DB, we have a potential
    race condition here.
    """
    if user_exists(username):
        return DUPLICATE
    else:
        dbc.insert_doc(USERS, {USER_NM: username,
                               PASSWORD_NM: password, MESSAGES_NM: []})
        return OK


def del_user(username):
    """
    Delete username from the db.
    """
    if not user_exists(username):
        return NOT_FOUND
    else:
        dbc.del_one(USERS, filters={USER_NM: username})
        return OK


def add_message(chatname, messages):
    """
    Add a message to the database.
    Until we are using a real DB, we have a potential
    race condition here.
    """
    # dbc.insert_doc(MESSAGES, {MESSAGES_NM: messages})
    dbc.insert_msg(ROOMS, chatname, messages)
    return OK


def get_messages(chatname):
    """
    A function to return a dictionary of all users.
    """
    return dbc.fetch_all_msg(ROOMS, chatname)
