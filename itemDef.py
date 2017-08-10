class item(object):
    def __init__(self, name, desc, value):
        self.name = name
        self.desc = desc
        self.value = value

class weapon(item):
    def __init__(self, name, desc, value, attack, block):
        super(weapon, self).__init__(name, desc, value)
        self.attack = attack
        self.block = block

class armor(item):
    def __init__(self, name, desc, value, block):
        super(armor, self).__init__(name, desc, value)
        self.block = block

class questItem(item):
    def __init__(self, name, desc, value, questID):
        super(questItem, self).__init__(name, desc, value)
        self.questID = questID

