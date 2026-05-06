name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95

# ACTIVITIES:
#Theere are many ways to complete these tasks. How will you do them?
#1 Increase age by 1 year
#2 Change the address to 17 Park Street
#3 No longer vaccinated (change state of vaccinated)
#4 Prompt user for updated credit card number and save new number
#5 Change owner name to Alex Jones
#6 Subtract $25 from account balance



owner_name = "John"
animal_category = input("What type of animal do you have?")
age = 4
Not_vaccinated = False
creditcard = input("Please Enter new Credit Card Number")
billing_address = "17 Park Street, The Shire 2695"
owner_name = "Alex Jones"
account_balance = 129.95 - 25

def help():
  print('Welcome to the Pet Data Management System')
  print("Every vet's best friend")

def increase_age():
  global age
  age = age + 1

def verify_credit_card(creditcard):
 if len(creditcard) == 19:
if len(creditcard.split()) == 4:
return True
  return False
 num = "5765 7574 7247"
if verify_credit_card(creditcard): == True:
print("VALID")
else:
print("INVALID")



help()
increase_age()
print(age)