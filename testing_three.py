import websocket
import _thread
import time
import json
import pandas as pd
import numpy as np
import math

#df = pd.DataFrame()   # Instantiates an empty pandas DataFrame

def on_message(ws, message):
    print('Hello WOrld')
    #print(message)
    y = message
    z = json.loads(y)
    x = pd.DataFrame(z['payload'])
    print(x)

    

    

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    ws.send(json.dumps({
    "action": "subscribe",
    "book": "bat_mxn",
    "type": "trades"
}))
        

if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://ws.bitso.com",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever()