import random
from c1_RickGuitar_project import Inventory,Guitar

def initializeInventory(guitar_nums=20):
    '''
    默认生产20把吉他
    '''
    Types = ['acoustic', 'electric']
    Builders = ['Fender', 'Martin', 'Gibson', 'Collings', 'Olson', 'Ryan', 'PRS', 'ANY']
    Wood = [
        'Alder', 'sitka', 'Cedar','mahogany', 
        'indian_rosewood','brazilian_rosewood','maple'
        ]
    
    guitars = [
        ('000000', 1499.95, 'Fender', 'Stratocaster','electric','Alder','Alder')
    ]

    for i in range(guitar_nums):
        i += 1
        serialNumber = '{:0>6d}'.format(i)
        price = random.randrange(100000, 500000, 1) / 100
        builder = random.choice(Builders)
        types = random.choice(Types)
        backWood = random.choice(Wood)
        topWood = random.choice(Wood)
        model = 'fixed test'
        guitars.append((serialNumber, price, builder, model, types, backWood, topWood))
    
    return guitars


if __name__ == '__main__':
    rand_gen_guitar_list = initializeInventory()
    # print(r)
    inventory = Inventory()
    for guitar in rand_gen_guitar_list:
        inventory.addGuitar(*guitar)
    
    r = inventory.guitars
    i = 1 # 设置想看第几把吉他的参数
    print(r[i].getSerialNumber(), r[i].getPrice(), r[i].getBuilder())