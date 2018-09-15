class Guitar(object):

    def __init__(self, serialNumber, price, builder, model, types, backWood, topWood):
        self.serialNumber = serialNumber
        self.price = price
        self.builder = builder
        self.model = model
        self.types = types
        self.backWood = backWood
        self.topWood = topWood
    
    def getSerialNumber(self):
        return self.serialNumber
    
    def getPrice(self):
        return self.price

    def setPrice(self, newPrice):
        self.price = newPrice

    def getBuilder(self):
        return self.builder

    def getModel(self):
        return self.model
    
    def getTypes(self):
        return self.types
    
    def getBackWood(self):
        return self.backWood

    def getTopWood(self):
        return self.topWood


class Inventory(object):
    
    def __init__(self, guitarsList=[]):
        self.guitars = guitarsList

    def addGuitar(self, serialNumber, price, builder, model, types, backWood, topWood):
        guitar = Guitar(serialNumber, price, builder, model, types, backWood, topWood)
        self.guitars.append(guitar)

    def getGuitar(self, serialNumber):
        for i in self.guitars:
            if i.getSerialNumber() == serialNumber:
                return i
        return None

    def search(self, Guitar):
        for guitar in self.guitars:
            builder = Guitar.getBuilder()
            if (builder is not None) and (builder is not '') and (builder != guitar.getBuilder()):
                continue

            model = Guitar.getModel()
            if (model is not None) and (model is not '') and (model != guitar.getModel()):
                continue

            types = Guitar.getTypes()
            if (types is not None) and (types is not '') and (types != guitar.getTypes()):
                continue
            
            backWood = Guitar.getBackWood()
            if (backWood is not None) and (backWood is not '') and (backWood != guitar.getBackWood()):
                continue

            topWood = Guitar.getTopWood()
            if (topWood is not None) and (topWood is not '') and (topWood != guitar.getTopWood()):
                continue
            
            return guitar
        return None


if __name__=='__main__':
    inventory = Inventory()
    inventory.addGuitar('V95693', 1499.95, 'Fender', 'Stratocaster','electric','Alder','Alder')
    inventory.addGuitar('V95694', 499.95, 'TT', 'Stratocaster','electric','Alder','Alder')
    