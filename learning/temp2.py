import time

def request():
		time.sleep(10)
		return 10

def main_function():
		response = request()
		return response

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level
 
    def get_info(self):
        infos = {"name" : self.name,
        "level" : self.level}
        return infos

def create_player():
    player = Player("Ranga", 100)
    infos = player.get_info()
    return infos