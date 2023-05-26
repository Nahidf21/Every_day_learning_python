import random 

def game():
    luck=random.randint(1, 2)
    
    return int(luck)

def main():
    permission= "y"
    while permission=="y":
        for _ in range(1,11):
            if _ == 1:
                print("First dise result: \n")
                if game()==1:
                    print("Heads")
                else:
                    print("Tails")
                    
            elif _==2: 
                print("Second dise result: \n")
                if game()==1:
                    print("Heads")
                else:
                    print("Tails")
            elif _==3: 
                print("Third dise result: \n")
                if game()==1:
                    print("Heads")
                else:
                    print("Tails")
            elif _==4: 
                print("Forth dise result: \n")
                if game()==1:
                    print("Heads")
                else:
                    print("Tails")
            elif _==5: 
                print("Fifth dise result: \n")
                if game()==1:
                    print("Heads")
                else:
                    print("Tails")
            elif _==6: 
                print("Sixth dise result: \n")
                if game()==1:
                    print("Heads")
                else:
                    print("Tails")
            elif _==7: 
                print("Seventh dise result: \n")
                if game()==1:
                    print("Heads")
                else:
                    print("Tails")
            elif _==8: 
                print("Eighth dise result: \n")
                if game()==1:
                    print("Heads")
                else:
                    print("Tails")
            elif _==9: 
                print("Ninth dise result: \n")
                if game()==1:
                    print("Heads")
                else:
                    print("Tails")
            elif _==10: 
                print("Tenth dise result: \n")
                if game()==1:
                    print("Heads")
                else:
                    print("Tails")
        
        permission= input("If you want to continue then enter y if not the enter n \n = ") 
main()

        