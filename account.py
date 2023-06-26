class Account:
   
   def __init__(self, bal):
       self.bal=bal
       
   def add_money(self,nahid):
     
       self.bal=self.bal+nahid
       
   def cash_money(self,cash):
       if self.bal >= cash:
           self.bal=self.bal-cash
       else:
           print("your dont have sufficient balance ")
   def print_bal(self):
       print("Your account Balance is : ", format(self.bal,".2f"))
       
       
       
   
      

     


      
