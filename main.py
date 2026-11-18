from expenses import *
from validation import CATEGORIES
from reports import *

def showmenu():
  print("=" * 40)
  print("            EXPENSE TRACKER           ")
  print("="  *40)
  print()

  print("""

  1.Add Expense
  2.Show All Expenses
  3.Edit Expense
  4.Delete Expense
  5.Search Expense
  6.Show Total Expenses
  7.Show Categories
  8.Export to CSV

  0.Exit

  """)
  print("=" * 40)

def startApp():
  while True:
    showmenu()

    choice = input("Choise:")

    if choice == "1":
      title = input("Enter title:")
      amount = float(input("Enter amount:")
      category = input("Enter category")
      add Expense(title,amount,category)
      print("Expense added!")

elif choice == "2":
expenses = getAllExpenses():

 for e in expenses:
   print(e)

elif choice == "3":
id = input("Enter ID:")
title = input("Enter new title:")
amount = float(input("Enter new amount")
category = input("Enter new category:")

updateExpense(id,title,amount,category)
print("Expense updated!")

elif choice == "4":
id = input("Enter ID:")

deleteExpense(id)

print("Expense deleted!")


elif choice == "5":
id = input("Enter ID:")
print(searchExpense(id)



elif choice == "6":
print("Total:",totalExpenses())

elif choice == "7":
showCategories()

elif choice == "8":
print("File:",exportToCSV())

elif choice == "9":
print("Goodbye!")
break

else:
print("Wrong choice")

startApp()
