class Car:
    def __init__(self,makes,model,horse_power):
        self.make=makes
        self.model=model
        self.horse_power=horse_power
        
    def prints(self):
        print("Make: ", self.make)
        print("Model: ", self.model)
        print("horse_power: ", self.horse_power)
