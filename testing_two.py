import json
from websocket import create_connection
import pandas as pd
ws = create_connection("wss://ws.bitso.com")
#ws.connect("wss://api2.bitfinex.com:3000/ws")
ws.send(json.dumps({
    "action": "subscribe",
    "book": "btc_mxn",
    "type": "trades"
}))


x = 1
while x <5:
    result = ws.recv()
    result = json.loads(result)
    #y = result['payload']
    #x = pd.DataFrame.from_dict(result, orient='index')
    print(f'The data type is: {type(result)}' )
    print(result['action'])
    # print ("Received '%s'" % result)
    x += 1
ws.close()