class enemy(object):
    def __init__(self, name, desc, hp):
        self.name = name
        self.desc = desc
        self.hp = hp

    def __str__(self):
        return 'Name: ' + self.name + '\nDescription: ' + self.desc + '\nHp: ' + str(self.hp)

class cavebat(enemy):
    def __init__(self):
        super(cavebat, self).__init__('Cave Bat', 'Small annoying creature ~ kinda like abe', 10)

cavebat = cavebat()
