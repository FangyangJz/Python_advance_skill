
from enum import Enum, unique  # python中的枚举类

@unique  # 保证没有重复的枚举类型
class Type(Enum):
    ACOUSTIC = 'acoustic'
    ELECTRIC = 'electric'

@unique
class Builder(Enum):
    FENDER = 'Fender' 
    MARTIN ='Martin'
    GIBSON = 'Gibson'
    COLLINGS = 'Collings'
    OLSON = 'Olson'
    RYAN = 'Ryan'
    PRS = 'PRS'
    ANY = 'ANY'


@unique
class Wood(Enum):
    ALDER = 'Alder'
    SITKA = 'sitka'
    CEDAR = 'Cedar'
    MAHOGANY = 'mahogany'
    INDIAN_ROSEWOOD = 'indian_rosewood'
    BRAZILIAN_ROSEWOOD = 'brazilian_rosewood'
    MAPLE = 'maple'
