import json, items, enemies

def loadItems(jitem):
    ritems = {}
    for item, count in jitem.items():
        item = eval(item)
        ritems[item] = count
    return ritems

def loadEnemies(jenemies):
    renemies = []
    for enemie in jenemies:
        enemie = eval(enemie)
        renemies.append(enemie)
    return renemies

class tile(object):
    def __init__(self, jfile):
        with open(jfile) as dataFile:
            data = json.load(dataFile)
        self.data = data
        self.name = data['name']
        self.text = data['text']
        self.enemies = loadEnemies(data['enemies'])
        self.items = loadItems(data['items'])
