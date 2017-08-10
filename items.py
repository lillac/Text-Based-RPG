import itemDef as i

#Generic Items (Name, Description, Value)

class gold(i.item):
    def __init__(self):
        super(gold, self).__init__('Gold', 'A Small Gold Coin Marked With The Kings Head', 1)

class wood(i.item):
    def __init__(self):
        super(wood, self).__init__('Wood', 'A Log of wood, used for building and burning', 1)

class stone(i.item):
    def __init__(self):
        super(stone, self).__init__('Stone', 'Small fist sized stone, commenly used to line paths and build campfires', 0)

gold = gold()
wood = wood()
stone = stone()

#Weapons (Name, Description, Value, Attack, Block)

class rock(i.weapon):
    def __init__(self):
        super(rock, self).__init__('Rock', 'A medium sized rock, great for bashing abes skull open', 0, 2, 0)

rock = rock()
