data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

def print_transactions(transactions):
  for transaction in transactions:
    amount, statement = transaction
    print(f"${amount} - {statement}")


def print_summary(transactions):
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposited = sum(deposits)
  print(f"You have deposited $- {total_deposited}")
  withdrawls = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_withdrawls = sum(withdrawls)
  print(f"You have withdrawl $- {total_withdrawls}")
  balance = total_deposited + total_withdrawls
  print(f"your Balance is $-{balance}")


def analyze_transactions(transactions):

  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposits = sum(deposits)
  if len(deposits) > 0:
    average_deposits = total_deposits /len(deposits)
  else:
    average_deposits = 0
  
  withdrawls = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_withdrawls = sum(withdrawls)
  if len(withdrawls) > 0:
    average_withdrawls = total_withdrawls /len(withdrawls)
  else:
    average_withdrawls = 0

  transactions.sort()
  largest_deposit = transactions[0]
  largest_withdrawl = transactions[-1]
  
  print(f"the largest deposit that you have ever made is : {largest_deposit}")
  print(f"the largest withdrawl that you have ever made is : {largest_withdrawl}")
  print(f"the average of your deposits is: {average_deposits}")
  print(f"the average of your withdrawls is: {average_withdrawls}")

while True:
  choice = input("What do you want to do? \n 1) print \n 2) analyze \n 3) stop \n").strip().lower()

  if choice == "print" or choice == "1":
    print_summary(data)
  elif choice == "analyze" or choice == "2":
    analyze_transactions(data)
  elif choice == "stop" or choice == "3":
    break
  else:
    print("Invalid choice")
