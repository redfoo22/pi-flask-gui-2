from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
import threading
import time
import urllib3

urllib3.disable_warnings()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins='*')
#app.config['host'] = '0.0.0.0'
logText = 0



# @socketio.on('log')
# def handleMessage(data):

#     print('log: ' + data)
#     # send(msg, broadcast=True)
@socketio.on('log')
def handleLog(dataLog):
    print('from log',dataLog)
    socketio.emit('log', dataLog['num'], broadcast=True)

@socketio.on('upBtn')
def handleUpBtn(data):
    print('from pydoor',data)
    socketio.emit('upBtn', data, broadcast=True)

@socketio.on('shutDownBtn')
def handleShutDownBtn(data1):
    print('from pydoor',data1)
    socketio.emit('shutDownBtn', data1, broadcast=True)

@socketio.on('downBtn')
def handleDownBtn(data2):
    print('from pydoor',data2)
    socketio.emit('downBtn', data2, broadcast=True)       

@socketio.on('doorLog')
def handleDoorLog(data):
    pass
    # print('from doorlog Server',data)
    # socketio.emit('doorLog', "ping")    
    
# @app.route('/reqtest', methods=['GET', 'POST'])
# def reqtest():
#     print(request.form['num'])
#     data = request.form['num']

#     socketio.emit('log', data)
#     return "hi"
    

@app.route('/')
def index():

    
    return render_template('index.html')
@app.route('/index2')
def index2():

    
    return render_template('index2.html')    


def thread_function():
    logText =0
    while 1:
        logText += 1
        socketio.emit('log',logText)
        time.sleep(0.05)

x = threading.Thread(target=thread_function)
# x.start()


if __name__ == '__main__':
    # socketio.run(app)
    socketio.run(app=app,ssl_context=('cert.pem', 'key.pem'),host='0.0.0.0',port=82)
    #host='0.0.0.0',port=80
   
    