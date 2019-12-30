
from c1_dog_door import DogDoor
from c1_bark import Bark

class BarkRecognizer(object):

    def __init__(self, door:DogDoor):
        self.door = door

    def recognize(self, bark: Bark):
        # print('BarkRecognizer: Heard a %s' % bark)
        for b in self.door.getAllowedBark():
            if b.equals(bark):
                self.door.open()
                print('Access Successful !')
                return True
        print('Access Deny !')
        return False
