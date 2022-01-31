import websocket
import _thread
import time
import json

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    _thread.start_new_thread(run, ())

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.bitso.com",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error)
    ws.send(json.dumps({
        'action': 'subscribe',
        'book': 'btc_mxn',
        'type':'trades'
    }))

    ws.run_forever()