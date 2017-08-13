from inventory import inventory
import items

class enemy(object):
    def __init__(self, name, desc, hp, damage):
        self.name = name
        self.desc = desc
        self.hp = hp
        self.damage = damage
        self.inv = inventory()

    def __str__(self):
        return 'Name: ' + self.name + '\nDescription: ' + self.desc + '\nHp: ' + str(self.hp)

    def isAlive(self):
        return self.hp > 0

    def attack(self, enemy):
     print(self.name + ' Attacked ' + enemy.name + ' and delt ' + str(self.damage) + 'damage')
     enemy.hp -= self.damage
     return enemy.hp

class cavebat(enemy):
    def __init__(self):
        super(cavebat, self).__init__('Cave Bat', 'Small annoying creature ~ kinda like abe', 10, 5)

class wolf(enemy):
    def __init__(self):
        super(wolf, self).__init__('Wolf', 'An angry wolf, possably rabid', 50, 10)
