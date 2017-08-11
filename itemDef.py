class item(object):
    def __init__(self, name, desc, value):
        self.name = name
        self.desc = desc
        self.value = value

    def __str__(self):
        return 'Name: ' + self.name + '\nDescription: ' + self.desc + '\nValue: ' + str(self.value)

class weapon(item):
    def __init__(self, name, desc, value, attack, block):
        super(weapon, self).__init__(name, desc, value)
        self.attack = attack
        self.block = block

    def __str__(self):
        return 'Name: ' + self.name + '\nDescription: ' + self.desc + '\nValue: ' + str(self.value) + '\nAttack: ' + str(self.attack) + '\nBlock: ' + str(self.block)


class armor(item):
    def __init__(self, name, desc, value, block):
        super(armor, self).__init__(name, desc, value)
        self.block = block

    def __str__(self):
        return 'Name: ' + self.name + '\nDescription: ' + self.desc + '\nValue: ' + str(self.value) + '\nBlock: ' + str(self.block)

class questItem(item):
    def __init__(self, name, desc, value, questID):
        super(questItem, self).__init__(name, desc, value)
        self.questID = questID
        
class food(item):
    def __init__(self, name, desc, value, neut):
        super(food, self).__init__(name, desc, value)
        self.neut = neut
