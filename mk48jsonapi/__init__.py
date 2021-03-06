import json

class Mk48JSON:
	def __init__(self):
		pass
		
	def Spawn(self, name, ship, new=False):
		PayloadJSON = {
			"type": "spawn",
			"data": {
				"name": name,
				"type": ship,
				"new": new
			}
		}
		return json.dumps(PayloadJSON)
		
	def SendChat(self, message, team=False):
		PayloadJSON = {
			"type": "sendChat",
			"data": {
				"message": message,
				"team": team
			}
		}
		return json.dumps(PayloadJSON)

	def Aim(self, x, y):
		PayloadJSON = {
			"type": "aim",
			"data": {
				"target": {
					"x": x,
					"y": y
				}
			}
		}
		return json.dumps(PayloadJSON)
	
	def Fire(self, index, x, y):
		PayloadJSON = {
			"type": "fire",
			"data": {
				"index": index,
				"positionTarget": {
					"x": x,
					"y": y
				}
			}
		}
		return json.dumps(PayloadJSON)