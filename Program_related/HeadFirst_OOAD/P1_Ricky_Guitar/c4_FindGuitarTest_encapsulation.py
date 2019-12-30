import random
from c3_RickGuitar_project_encapsulation import Inventory, Guitar, GuitarSpec
from c1_enums import Builder, Type, Wood


def initializeInventory(guitar_nums=20):
    '''
    默认生产20把吉他
    '''
    Types = ['acoustic', 'electric']
    Builders = ['Fender', 'Martin', 'Gibson', 'Collings', 'Olson', 'Ryan', 'PRS', 'ANY']
    # Builders = ['Fender', 'Martin']
    # Wood = [
    #     'Alder', 'maple'
    #     ]
    Wood = [
        'Alder', 'sitka', 'Cedar', 'mahogany',
        'indian_rosewood', 'brazilian_rosewood', 'maple'
    ]
    
    guitars = [
        ('000000', 1499.95, 'Fender', 'Stratocastor','electric','Alder','Alder'),
        ('000000', 50.95, 'Fender', 'Stratocastor', 'electric', 'Alder', 'Alder')
    ]

    for i in range(guitar_nums):
        i += 1
        serialNumber = '{:0>6d}'.format(i)
        price = random.randrange(100000, 500000, 1) / 100
        builder = random.choice(Builders)
        types = random.choice(Types)
        backWood = random.choice(Wood)
        topWood = random.choice(Wood)
        model = 'fixed-test'
        guitars.append((serialNumber, price, builder, model, types, backWood, topWood))
    
    return guitars


if __name__ == '__main__':
    # 1. 随机生成20把吉他
    rand_gen_guitar_list = initializeInventory(guitar_nums=2000)
    # print(r)
    
    # 2. 生产仓库对象，将20把吉他入库
    inventory = Inventory()
    for guitar in rand_gen_guitar_list:
        inventory.addGuitar(*guitar)

    # #   查看仓库吉他情况
    # r = inventory.guitars
    # # i = 1999 # 设置想看第几把吉他的参数
    # for i in range(0, 20, 2):
    #     print(r[i].getSerialNumber(), r[i].getPrice(), r[i].getBuilder(), r[i].getModel(),
    #     r[i].getTypes(), r[i].getBackWood(), r[i].getTopWood())

    # 3. 生成Erin想要的吉他
    # print(Builder.FENDER) # 注意这里, python中的 Enum 的值, 要 .value 才能访问到
    # 这里用的封装的类 GuitarSpec
    whatErinLikes = GuitarSpec(Builder.FENDER.value, 'Stratocastor', Type.ELECTRIC.value, Wood.ALDER.value, Wood.ALDER.value)

    # 4. 寻找吉他
    search_result_guitar = inventory.search(whatErinLikes)
    if search_result_guitar != []:
        print("Erin, you might like this: ")
        for i in search_result_guitar:
            print('''{0}, {1}, {2}, {3} back, {4} top. You have it for only {5} !'''
                .format(i.guitar_spec.getBuilder(), i.guitar_spec.getModel(), i.guitar_spec.getTypes(),
                        i.guitar_spec.getBackWood(), i.guitar_spec.getTopWood(), i.getPrice()))
    else:
        print('Sorry, Erin, we have nothing for you.')

    print('Total {} guitars'.format(len(search_result_guitar)))