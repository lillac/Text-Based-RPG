import json, items, enemies, player

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
        self.options = data['options']

    def search(self, iore):
        if(iore == 'e'):
            if(self.enemies):
                for e in self.enemies:
                    print(e.name + ' HP: ' + str(e.hp))
            else:
                print('No Enemies to be Found')
        elif(iore == 'i'):
            if(self.items):
                for k, v in self.items.items():
                    print(k.name + ' : ' + format(v, ',d'))
            else:
                print('No Items to be found')

    def take(self):
        e = False
        item = input('Take Item > ')
        for k, v in self.items.items():
            if(k.name.lower() == item.lower()):
                player.player.inv.add(k, v)
                del self.items[k]
                print('Took ' + str(v) + ' ' + k.name)
                break
            else:
                e = True
        if (e):
            print('I can\'t find ' + item)


    def enter(self):
        print(self.name + '\n' + self.text + '\n')
        while(True):
            for k, v in sorted(self.options.items()):
                print(k + ' : ' + v['Text'])
            choice = str(input('> '))
            if(choice not in self.options.keys()):
                print('Thats not something i can do')
            elif(choice == '4'):
                return
            else:
                exec(self.options[choice]['Func'])
