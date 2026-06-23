
print("Welcome To Our Expense Tracker")
print("Track Your Expense with Us ")

adexpense={}
count=0
j=1
while(j<=100): 
  print("======{{{{{MENU}}}}}=======")
  print("1.Add expense\n2.Calculate expense\n3.View all total spending\n4.exit\n")
  sel=int(input("You Want To Enter In : \a"))
  if(sel == 1):
    print("---Add expenses here---")
    date=input("enter date:")
    month=input("enter month:")
    year=input("enter year:")
    items=int(input("no of expenses want to add:"))
    i=1
    while(i<=items):
        print("start:",i)
        e=input("expense name: ")
        a=int(input("Enter Amount: rs "))
        adexpense[e]=a
        i +=1
    print("===={{{{:Your Today Expenses:}}}}====") 
    print(f"your expense date : {date}/{month}/{year}")
    print("SUCCESFULLY ADDED\n\a") 
  if(sel ==2):
      print("--->Viewing Your Expenses<---")
      for el in adexpense:
          print(el,":",adexpense[el])
  if(sel == 3):
      print("-->]Total Expenses[<--")
      count=0
      for el in adexpense:
          print(el,":",adexpense[el])
          count+=adexpense[el]
      print("Total price is :",count)
  if(sel == 4):
      print("======Thank You For Using Our System======")
      print(" ----}}}}}}Do You Want To Rate Our System{{{{{{----")
      kite=int(input("Enter from(1-5){for rating} \nFor Exit {press 6}:"))
      if(kite == 1):
          print("====Thank You For Rating====")
          input(":Please Type Here To Improve Our System:\n ")
          print("--YOUR SUGGESTED WILL BE CONSIDERED--")
      elif(kite == 2):
          print("======Thank You For Rating======")
          input(":Please Type Here To Improve Our System: \n") 
          print("--YOUR SUGGESTED WILL BE CONSIDERED--")
      elif(kite == 3):
          print("=====Thank You For Rating=====")
          input("Feeling Happy🥀\n-Please Type Here To Improve Our System-\n ")
          print("--YOUR SUGGESTED WILL BE CONSIDERED--")
      elif(kite == 4):
          print("=====Thank You For Rating=====")  
          print("✨That's is appreciating✨\n" )
          print("-Please Type Here To Improve Our System-\n ")
          
          print("==That's is a gift for you:🌺==")
      elif(kite == 5):
          print("===Thank You For Rating==")  
          print("✨That's is Marvellous✨\n ")
          print("--You Liked Our Mini Project--\n")
          
          print("===That's is a gift for you:🌹==")
      elif(kite==6):
          print("===thank you for using our system===")
      break      
j+=1