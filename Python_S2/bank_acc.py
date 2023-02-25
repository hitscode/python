class Account:
    def __init__(self,account_name,account_num,account_bal):
        self.account_name= account_name
        self.account_num = account_num
        self.account_bal = account_bal
    
    def display(self):
        print("Name : ", self.account_name)
        print("Account Number : ", self.account_num)
        print("Balance : ", self.account_bal)
    
    def deposit(self, d_amount):
        self.account_bal= self.account_bal+ d_amount
        print("Credited Ammount : ", d_amount)
        print("Current Amount : ",self.account_bal)

    def withdrawal(self, w_amount):
        if( w_amount> self.account_bal):
            print("Insuficient Ammount to withdraw .\n")
        else:
            self.account_bal=self.account_bal- w_amount
            print("Debited Ammount : ",w_amount)
            print("Current Amount : ", self.account_bal, "\n")

Account_obj=Account("Sam", 202103103510465 , 35000)
Account_obj.display()
Account_obj.deposit(1000)
Account_obj.withdrawal(37000)

Account_obj=Account("Dad", 9876543210 , 50500)
Account_obj.display()
Account_obj.deposit(5000)
Account_obj.withdrawal(500)