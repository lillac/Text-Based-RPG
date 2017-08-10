import items

class inventory(object):
    def __init__(self):
        self.store = {}

    def __str__(self):
        out = 'Item : Count\n'
        for item, count in self.store.items():
            out += item.name + ' : ' + str(count) + '\n'
        return out

    def add(self, item, count):
        if (item in self.store):
            self.store[item] += count
            return
        self.store[item] = count
