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
