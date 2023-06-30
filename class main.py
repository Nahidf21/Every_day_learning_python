class Employee:

    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def printData(self):
        print("\nName :", self.name)
        print("ID Number :", self.id_number)

class ProductionWorkers(Employee):
    def __init__(self, name, id_number, shift_number,hourly_rate):
        Employee.__init__(self, name, id_number)
        self.shift_number = shift_number
        self.hourly_rate = hourly_rate

    def printData(self):
        Employee.printData(self)
        print("Shift Name: ", self.shift_number)
        print("Hourly rate: $", format(self.hourly_rate, ".2f"))


def main():
    name = input("Enter your name: ")
    id_number = input("Enter your ID Number: ")
    shift_number = int(input("Enter your shift number: "))
    if shift_number == 1:
        shift_number = "Day Shift"
    elif shift_number == 2:
        shift_number = "Night Shift"

    hourly_rate = int(input("Enter your hourly_rate: "))

    ## lets create instance for ProductionWorkers class

    m = ProductionWorkers(name, id_number, shift_number, hourly_rate)
    m.printData()

if __name__ == '__main__':
    main()