

class GuitarSpec(object):

    def __init__(self, builder, model, types, numStrings, backWood, topWood):
        self.builder = builder
        self.model = model
        self.types = types
        self.numStrings = numStrings
        self.backWood = backWood
        self.topWood = topWood

    def getBuilder(self):
        return self.builder

    def getModel(self):
        return self.model
    
    def getTypes(self):
        return self.types

    def getNumStrings(self):
        return self.numStrings
    
    def getBackWood(self):
        return self.backWood

    def getTopWood(self):
        return self.topWood

    def matches(self, otherSpec):
        if self.builder != otherSpec.builder:
            return False
        
        if self.model is not None:
            pass
        
        if self.types != otherSpec.types:
            return False
        
        if self.numStrings != otherSpec.numStrings:
            return False
        
        if self.backWood != otherSpec.backWood:
            return False
        
        if self.topWood != otherSpec.topWood:
            return False
        
        return True


class Guitar(object):
    # python中的封装和java有些区别啊, 
    # java中的封装是封到一个类里去
    # 可是python这么干的话, 这不就是继承么. python中的封装是加双下划线'__' 变私有封起来的意思
    # 当然, python在实例化的初始化时, 也可以传个其他的类的实例作为属性
    def __init__(self, serialNumber, price, guitar_spec:GuitarSpec):
        self.serialNumber = serialNumber
        self.price = price
        self.guitar_spec = guitar_spec

    def getSerialNumber(self):
        return self.serialNumber

    def getPrice(self):
        return self.price

    def setPrice(self, newPrice):
        self.price = newPrice

    def getSpec(self):
        return self.guitar_spec


class Inventory(object):
    
    def __init__(self, guitarsList=[]):
        self.guitars = guitarsList

    def addGuitar(self, serialNumber, price, builder, model, types, backWood, topWood):
        guitar_spec = GuitarSpec(builder, model, types, backWood, topWood)
        guitar = Guitar(serialNumber, price, guitar_spec)
        self.guitars.append(guitar)

    def getGuitar(self, serialNumber):
        for i in self.guitars:
            if i.getSerialNumber() == serialNumber:
                return i
        return None

    def search(self, guitar_spec):
        matchingGuitars = []
        for guitar in self.guitars:
            if guitar.getSpec().matches(guitar_spec):
                matchingGuitars.append(guitar)               
        return matchingGuitars


if __name__=='__main__':
    inventory = Inventory()
    # inventory.addGuitar('V95693', 1499.95, 'Fender', 'Stratocaster','electric','Alder','Alder')
    # inventory.addGuitar('V95694', 499.95, 'TT', 'Stratocaster','electric','Alder','Alder')
    