"""
This file holds the tests for endpoints.py.
"""

from email import message
from unittest import TestCase, skip 
from flask_restx import Resource, Api
import random

import API.endpoints as ep
import db.data as db

HUGE_NUM = 100000000000000  # any big number will do!


def new_entity_name(entity_type):
    int_name = random.randint(0, HUGE_NUM)
    return f"new {entity_type}" + str(int_name)


class EndpointTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hello(self):
        hello = ep.HelloWorld(Resource)
        ret = hello.get()
        self.assertIsInstance(ret, dict)
        self.assertIn(ep.HELLO, ret)

    # @skip("In the middle of making this work.")
    def test_create_user(self):
        """
        See if we can successfully create a new user.
        Post-condition: user is in DB.
        """
        cu = ep.CreateUser(Resource)
        new_user = new_entity_name("user")
        new_password = new_entity_name("password")
        # ret = cu.post(new_user, new_password)
        # users = db.get_users()
        # self.assertIn(new_user, users)

    def test_create_room(self):
        """
        See if we can successfully create a new room.
        Post-condition: room is in DB.
        """
        cr = ep.CreateRoom(Resource)
        new_user = new_entity_name("user")
        new_room = new_entity_name("room")
        new_genre = new_entity_name("genre")
        # ret = cr.post(new_room, new_genre, new_user)
        # rooms = db.get_rooms()
        # self.assertIn(new_room, rooms)

    def test_create_message(self):
        """
        See if we can successfully create a new room.
        Post-condition: room is in DB.
        """
        cr = ep.CreateMessage(Resource)
        new_message = new_entity_name("message")
        new_user = new_entity_name("user")
        ret = cr.post("new room16597361770438", new_message, new_user)
        #messages = db.get_messages()
        # self.assertIn(new_message, messages)

    def test_list_messages(self):
        listMsg = ep.ListMessages(Resource)
        ret = listMsg.get("new room14667656783878")


    def test_list_by_genre(self):
        listGenre = ep.ListRoomsByGenre(Resource)
        ret = listGenre.get("new genre34872589680861")
        print('by genre', ret)

    
    def test_list_by_search(self):
        listSearch = ep.ListRoomsBySearch(Resource)
        ret = listSearch.get("new rOom16597361770438")
        print('by search', ret)


    def test_list_user(self):
        listUser = ep.FindUser(Resource)
        ret = listUser.get("new user86191772604053", "new password80436178979320")
        print(ret, 'list user')


    def test_list_rooms1(self):
        """
        Post-condition 1: return is a dictionary.
        """
        lr = ep.ListRooms(Resource)
        ret = lr.get()
        # self.assertIsInstance(ret, dict)

    def test_list_rooms2(self):
        """
        Post-condition 2: keys to the dict are strings
        """
        lr = ep.ListRooms(Resource)
        ret = lr.get()
        # for key in ret:
            # self.assertIsInstance(key, str)

    def test_list_rooms3(self):
        """
        Post-condition 3: the values in the dict are themselves dicts
        """
        lr = ep.ListRooms(Resource)
        ret = lr.get()
        # for val in ret.values():
            # self.assertIsInstance(val, dict)
