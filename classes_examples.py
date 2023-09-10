class Dinosaur(object):
    # attributes
    dino_health = 70
    dino_energy = 2000
    #methods 
    # attack method 
    def dino_attack(self, amount):
        print('The baby dinosaur has attaked')
        print(f'{amount}% of damage from attack was dealt')
        print(mimi)

     # move method 
    def dino_move(self, speed):
    	print('baby dino is moving')
    	print(f'dino is moving at a speed of {speed}km/hr')
mimi = Dinosaur()
mimi.dino_attack(2) # calling the method
mimi.dino_move(1) # method call 

"""
when a method (function in a class) is called, python passes a reference
to the object created by the class as the first argument into the method
"""

# the first parameter of any method always references the object 
# created by the class 
