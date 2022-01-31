import websocket
import json
#websocket.enableTrace(True)


while True:

    ws = websocket.WebSocket()
    ws.connect("wss://ws.bitso.com")
    ws.send(json.dumps({
    "action": "subscribe",
    "book": "btc_mxn",
    "type": "trades"
}))
    data = ws.recv() 

    get_data = json.loads(data)

    print(get_data)

#ws.close()