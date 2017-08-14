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
        
#Lighting 
class candle(i.item):
    def __init__(self):
        super(candle, self).__init__('candle', 'A smallish candle, pretty good at giving off a decent amount of light', 2)

gold = gold()
wood = wood()
stone = stone()
candle = candle()

#Food (Name, Description, Value, Neutrition)

class apple(i.food):
    def __init__(self):
        super(apple, self).__init__('Apple', 'A ripe green apple', 1, 5)
        
class raspberry(i.food):
    def __init__(self):
        super(raspberry, self).__init__('Raspberrys', 'A cluster of rasberries', 1, 3)
        
apple = apple()
raspberry = raspberry()

#Weapons (Name, Description, Value, Attack, Block)

class rock(i.weapon):
    def __init__(self):
        super(rock, self).__init__('Rock', 'A medium sized rock, great for bashing abes skull open', 0, 2, 0)

rock = rock()
