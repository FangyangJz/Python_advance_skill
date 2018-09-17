

class GuitarSpec(object):

    def __init__(self, builder, model, types, backWood, topWood):
        self.builder = builder
        self.model = model
        self.types = types
        self.backWood = backWood
        self.topWood = topWood

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


# class Guitar(GuitarSpec):
#     # python中的封装和java有些区别啊, 
#     # java中的封装是封到一个类里去
#     # 可是python这么干的话, 这不就是继承么. python中的封装是加双下划线'__' 变私有封起来的意思
#     # 当然, python在实例化的初始化时, 也可以传个其他的类的实例作为属性
#     def __init__(self, serialNumber, price, builder, model, types, backWood, topWood):
#         self.serialNumber = serialNumber
#         self.price = price
#         super().__init__(builder, model, types, backWood, topWood)

#     def getSerialNumber(self):
#         return self.serialNumber

#     def getPrice(self):
#         return self.price

#     def setPrice(self, newPrice):
#         self.price = newPrice


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

    def search(self, Guitar):
        matchingGuitars = []
        for guitar in self.guitars:
            builder = Guitar.getBuilder()
            if (builder is not None) and (builder is not '') and (builder != guitar.guitar_spec.getBuilder()):
                continue

            # model = Guitar.getModel()
            # if (model is not None) and (model is not '') and (model != guitar.getModel()):
            #     continue

            types = Guitar.getTypes()
            if (types is not None) and (types is not '') and (types != guitar.guitar_spec.getTypes()):
                continue
            
            backWood = Guitar.getBackWood()
            if (backWood is not None) and (backWood is not '') and (backWood != guitar.guitar_spec.getBackWood()):
                continue

            topWood = Guitar.getTopWood()
            if (topWood is not None) and (topWood is not '') and (topWood != guitar.guitar_spec.getTopWood()):
                continue

            matchingGuitars.append(guitar)

        return matchingGuitars
        # return None


if __name__=='__main__':
    inventory = Inventory()
    # inventory.addGuitar('V95693', 1499.95, 'Fender', 'Stratocaster','electric','Alder','Alder')
    # inventory.addGuitar('V95694', 499.95, 'TT', 'Stratocaster','electric','Alder','Alder')
    