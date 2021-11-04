# Chatbot server

## Requirements

- List chat rooms by creating a list room endpoint that returns all the chat rooms
- Create a user by using the username endpoint the user is able to set a username to enter the chat room
- Allow user to enter chat room
- Greet the user 
- Keep track of users
- Answer user questions
- Recognize user has left
- Allow the users to create a room by creating a create room endpoint
- private dms by creating dm endpoint to allow users for 1 to 1 msging

## Create 
- Users are able to create a username for themseleves to access the chat rooms using username endpoint
- Users are able to create a chat room with a topic of there choice by using the create endpoint 

## Read
- Users are able to read the data in json file in order to get the chat rooms that have been created or already up by using the list room endpoints

## Update
- Users are able to update the chat rooms found in the json file using the create room endpoint that creates there chatroom with zero users

## Delete 
- There are no options for the user to delete anything so far.
- It would be cool if a user is able to close a chat room 

## Design

- Use flask_restx to build an API server
- Multiple clients possible -- TBD
- Handle each major requirement with an API endpoint
- Use Test-Driven-Development (TDD) to make sure we have testing.
- Use Swagger for initial interaction with server.
- Use Swagger, pydoc and good docstrings for documentation.

