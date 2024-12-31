import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__ (self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed
        if self._cords[2] <= 0:
            print("It's too deep, i can't dive :(")
            self._cords[2] = 0

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        if self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")

    def speak(self,sound):
        self.sound = sound
        print(self.sound)

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        num_eggs = random.randint(1, 4)
        if num_eggs == 1:
            print(f"Here is {num_eggs} egg for you")
        else:
            print(f"Here are {num_eggs} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] = self._cords[2] - abs(dz) * (self.speed/2)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = "Click-click-click"

    def speak(self):
        print(self.sound)



db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
