from flask import Blueprint, render_template, url_for, redirect, request, jsonify
from config import *
from flask_socketio import join_room


chat = Blueprint("chat", __name__)



@chat.route('/', methods=['GET','POST'])
def chatss():
    # name = request.args.get('name')
    # room = request.args.get('room')

    return render_template('chat.html')



@chat.route('/chat1',methods=['GET', 'POST'])
def chat1():
    name = request.args.get('name')
    room = request.args.get('room')

    return render_template('chat1.html', name=name,room=room) 


@socketio.on('join_room')
def handle_join_room_event(data):
    # print(data)
    join_room(data['room'])
    socketio.emit('join_room_announcement', data)


@socketio.on('send_message')
def handle_send_message(data):
    print("message data", data['username'], data['room'], data['message'])
    f = open("demofile2.txt", "a")
    f.write(f"{data['username']}, {data['room']}, {data['message']}\n")
    f.close()

    #open and read the file after the appending:
    # f = open("demofile2.txt", "r")
    # print(f.readline().replace("\n","").split(','))
    
    socketio.emit('receive_message', data, room=data['room'])


@chat.route('/read')
def chatread():
    f = open("demofile2.txt", "r")
    a = f.readlines()
    for i in range(len(a)):
        print(a[i][0])
    return " done"