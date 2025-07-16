import time
import websocket
import datetime
import json
class CallModule:
    def __init__(self, host, port):
        self.ws = websocket.create_connection(f"ws://{host}:{port}")

    def call(self, number):
        self.ws.send(json.dumps({
            "command": "call",
            "number": number
            }))
        self.ws.recv()
        start_time = datetime.datetime.now().timestamp()
        while True:
            try:
                self.ws.send(json.dumps({
                "command": "status"
                }))
                if json.loads(self.ws.recv())["sip_client_response"]["status"] == 'active':
                    self.ws.send(json.dumps({
                        "command": "output"
                    }))
                    self.ws.recv()
                    return True

                time.sleep(1)
                if datetime.datetime.now().timestamp() - start_time > 30:
                    self.hangup()
                    return False

            except:
                pass

    def speak(self, text):
        self.ws.send(json.dumps({
            "command": "speak",
            "text": text
        }))
        self.ws.recv()

    def hangup(self):
        self.ws.send(json.dumps({
            "command": "hangup"
        }))
        self.ws.recv()

    def dtmf_received(self, true_code):
        spisok_number = ["0", "0", "0", "0", "0", "0"]
        k = 0
        while k < 6:
            message = json.loads(self.ws.recv())
            if ("event" in message) and (message["event"] == "dtmf_received"):
                spisok_number[k] = message["digit"]
                k += 1
        return true_code == ''.join(spisok_number)

    def work_with_problem(self):
        message = json.loads(self.ws.recv())
        if ("event" in message) and (message["event"] == "dtmf_received"):
            return message["digit"] == "1"
        elif ("event" in message) and (message["event"] == "recognition_partial"):
            return  "\u043f\u0440\u0438\u043d\u044f\u0442\u044c" in message["text"]
        else:
            return self.work_with_problem()









