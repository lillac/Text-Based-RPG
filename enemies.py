class enemy(object):
    def __init__(self, name, desc, hp):
        self.name = name
        self.desc = desc
        self.hp = hp

class cavebat(enemy):
    def __init__(self):
        super(CaveBat, self).__init__('Cave Bat', 'Small anoying creature ~ kinda like abe', 10)

cavebat = cavebat()
