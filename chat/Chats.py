from flask import Blueprint, render_template, url_for, redirect, request, jsonify
from config import *
from flask_socketio import join_room
from queries.globalQuery import *


chat = Blueprint("chat", __name__)





@socketio.on('join_room')
def handle_join_room_event(data):
    # print(data)
    join_room(data['room'])
    socketio.emit('join_room_announcement', data)


@socketio.on('send_message')
def handle_send_message(data):
    print("message data", data['message'], data['room'], data['username'], data['date'])
    
    save_chat(data['message'], data['room'], data['username'], data['date'], data['emp_id_fk'])
        
    socketio.emit('receive_message', data, room=data['room'])


# @chat.route('/read')
# def chatread():
#     f = open("demofile2.txt", "r")
#     a = f.readlines()
#     for i in range(len(a)):
#         print(a[i][0])
#     return " done"