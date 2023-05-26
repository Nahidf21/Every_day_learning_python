import random as rn

def main():
    print("01 to 10 numbers using random modiul: \n")
    print(random_munbers())

def random_munbers():
    lists=[]
    for _ in range(10):
        numbers= rn.randint(1, 10)
        lists.append(numbers)
    return lists
        

main()