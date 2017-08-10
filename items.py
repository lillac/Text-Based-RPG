import itemDef as i

#Generic Items

class gold(i.item):
    def __init__(self):
        super(gold, self).__init__('Gold', 'A Small Gold Coin Marked With The Kings Head', 1)

class wood(i.item):
    def __init__(self):
        super(wood, self).__init__('Wood', 'A Log of wood, used for building and burning', 1)

gold = gold()
wood = wood()

#Weapons

class rock(i.weapon):
    def __init__(self):
        super(rock, self).__init__('Rock', 'A medium sized rock, great for bashing abes skull open', 0, 2, 0)

rock = rock()
