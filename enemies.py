from inventory import inventory
import items

class enemy(object):
    def __init__(self, name, desc, hp):
        self.name = name
        self.desc = desc
        self.hp = hp
        self.inv = inventory()

    def __str__(self):
        return 'Name: ' + self.name + '\nDescription: ' + self.desc + '\nHp: ' + str(self.hp)

class cavebat(enemy):
    def __init__(self):
        super(cavebat, self).__init__('Cave Bat', 'Small annoying creature ~ kinda like abe', 10)
        self.inv.add(items.gold, 1)

cavebat = cavebat()
