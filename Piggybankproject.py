current_balance=0

 

print("Piggy Bank welcomes you\n")

opt=1

 

while(opt==1):

 

  user_input= int(input("Press 1 to add money\n"

"Press 2 to withdraw money\n"

"Press 3 to check the balance\n"))

 

 

 

  if(user_input==1):

    add_cash=int(input("How much money would you like to add?"))

    current_balance=current_balance+add_cash

    print("After adding, your updated balance is",current_balance)

 

  elif(user_input==2):

    wthdr_cash=int(input("How much money would you like to withdraw?"))

 

    if(current_balance>=wthdr_cash):

      current_balance=current_balance-wthdr_cash

      print("After withdrawing , balance is",current_balance)

    else:

      print("Sorry you don't have sufficient balance to withdraw the money")

 

  

  else:

    current_balance=current_balance

    print("Current balance is",current_balance)

   

  opt=int(input("To continue press 1\n"

  "To exit press 0"))