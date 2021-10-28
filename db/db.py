"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""
import json
ROOMS_DB = "/Users/oscarramirez/Desktop/sweJOL/db/rooms.json"


def get_rooms():
    """
    A function to return all chat rooms.
    """
    try:
        with open(ROOMS_DB) as file:
            return json.loads(file.read())
    except FileNotFoundError:
        return None
    '''
    return {"Software Engineering": {"num_users": 90},
                "AI": {"num_users": 90, "decr": "Discuss AI"}, }
                '''
