import socketio
import requests
import time
import urllib3

urllib3.disable_warnings()

sio = socketio.Client(ssl_verify=False,engineio_logger=False,logger=False)
sio.connect('https://192.168.86.38:82')


state = 1

url = 'http://127.0.0.1:5000/reqtest'
log = {'num': 0}

@sio.on('doorLog')
def handleDoorLog(data):
    global state
    global log
    state = (state + 1) % 2 
    log = {'num': 0}
    print('received doorLog!',state)


while 1:
    if state ==0:
        log['num'] =0
        sio.emit('log', log)

    
    if (state == 1):
        log['num'] +=1
        # x = requests.post(url, data = log)
        sio.emit('log', log)
        # sio.emit('log', "SPIRIT AND CHRIS")
        print('sending...',log['num'])
    time.sleep(0.05)

    

#print the response text (the content of the requested file):

