class vehicle:
    def __init__(self, make, model, year, color, sound):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self._sound = sound
    
    def honk(self):
        return self._sound

    @property
    def wheels(self):
        return self._wheels

class motorcycle(vehicle):
    def __init__(self, make, model, year, color, sound):
        super().__init__(make, model, year)
        
        self.wheels = 2

class car(vehicle):
    def __init__(self, make, model, year, color, sound):
        super().__init__(make, model, year)
        
        self.wheels = 4
        