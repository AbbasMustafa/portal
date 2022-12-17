from flask import Blueprint, render_template, url_for, redirect, request, jsonify
from config import *
from flask_socketio import join_room
from queries.globalQuery import *


chat = Blueprint("chat", __name__)



@socketio.on('join_room')
def handle_join_room_event(data):
    try:
        join_room(data['room'])
        socketio.emit('join_room_announcement', data)
    except Exception as e:
        print(e)
        return jsonify({"message":"error occur joining chat room"})


@socketio.on('send_message')
def handle_send_message(data):
    try:
    
        save_chat(data['message'], data['room'], data['username'], data['date'], data['emp_id_fk'])
        
        socketio.emit('receive_message', data, room=data['room'])

    except Exception as e:
        print(e)
        return jsonify({"message":"error occur while sending or saving chat"})
