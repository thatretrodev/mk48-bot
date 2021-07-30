import websocket
import _thread
import time
import json
import secrets
import random
from mk48jsonapi import *

bot_username = "b0t_t3st"

def on_message(ws, message):
	try:
		message_json = json.loads(message)
	except:
		return
	if "data" in message_json:
		if "contacts" in message_json["data"]:
			objects = message_json["data"]["contacts"]
			for i in objects.keys():
				current_object = objects[i]
				if "name" in current_object:
					if current_object["name"] != bot_username:
						print(current_object["name"] + " is at " + str(current_object["position"]["x"]) + ", " + str(current_object["position"]["y"]))

def on_error(ws, error):
	print(error)

def on_close(ws, close_status_code, close_msg):
	print("### closed ###")

def on_open(ws):
	def run(*args):
		mk48json = Mk48JSON()
		ws.send(mk48json.Spawn(bot_username, "pt34"))

		try:
			while True:
				time.sleep(5)
		except:
			ws.close()
			
		print("thread terminating...")
	_thread.start_new_thread(run, ())

if __name__ == "__main__":
	websocket.enableTrace(True)
	ws = websocket.WebSocketApp("ws://localhost:8192/ws", on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
	ws.run_forever()
