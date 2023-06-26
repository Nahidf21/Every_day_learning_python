import work as wk

def main():
    name = input("Whats your name : ")
    age=input("Enter your age: ")
    personClass=wk.Person(name, age)
    salary=input("Whats your salary: ")
    employeeClass=wk.Employee(name,age,salary)
    employeeClass.aboutMe()
    employeeClass.doWork()
    personClass.aboutMe()

main()
