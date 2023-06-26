class Person:
      def __init__(self,name,age):
          self.name=name
          self.age=age
      def aboutMe(self):
          print("My name is " + self.name + ". I am" + self.age +
                "Years old")
                  
class Employee(Person):
    def __init__(self, name, age,salary):
        Person.__init__(self, name, age)
        self.salary=salary
        
    def doWork(self):
        print("I work hard")
    
    def aboutMe(self):
        Person.aboutMe(self)
          

