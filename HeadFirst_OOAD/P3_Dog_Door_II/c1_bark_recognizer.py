
from c1_dog_door import DogDoor

class BarkRecognizer(object):

    def __init__(self, door:DogDoor):
        self.door = door

    def recognize(self, bark: str):
        print('BarkRecognizer: Heard a %s' % bark)
        self.door.open()