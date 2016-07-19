"""
Requires code to be edited with personal transactions
Prompts user to which information column to print
  (useful to then copy into an Excel file to easily read/check transactions)
#TODO: Automatically create Excel file
#TODO: Automatically pull information from CapitalOne website
"""

import StringIO

lines_per_transaction = 7

# Copied from the Capital One Transactions & Details page, pasted into plain text
# Make sure the first date is on the top line
# Also make sure the finishing """ are on their own line, below last amount
transactions_string = """7/12/16

GYM
Entertainment
...1234
$100.00
Open Drawer
7/11/16

GROCERY STORE
Merchandise
...1234
$15.15
Open Drawer
7/10/16

BAR
Dining
...1234
$30.00
Open Drawer
7/09/16

RUNNING EVENT
Entertainment
...1234
$68.90
Open Drawer
6/20/16

INTERNET
Phone/Cable
...1234
$29.95
Open Drawer
6/14/16

Amazon
Merchandise
...1234
$5.99
Open Drawer
6/13/16

PAYMENT
Payment
...1234
-$200.00
Open Drawer
"""

def ReadTransaction(buf):
    date = buf.readline().rstrip()
    empty = buf.readline().rstrip()
    merchant = buf.readline().rstrip()
    category = buf.readline().rstrip()
    card = buf.readline().rstrip()
    amount = buf.readline().rstrip()
    transaction_type = buf.readline().rstrip()
    return [date, merchant, category, card, amount]

def ReturnDates(transaction_list):
    for transaction in transaction_list:
        print transaction[0]

def ReturnMerchants(transaction_list):
    for transaction in transaction_list:
        print transaction[1]

def ReturnAmounts(transaction_list):
    for transaction in transaction_list:
        print transaction[4]

def PrintTotal(transaction_list, owed):
    total = float(owed)
    for transaction in transaction_list:
        total = total + float(transaction[4].replace("$", ""))
    print total

def PromptForOptions():
    print
    print
    print " Type \'d\' to print dates,"
    print "      \'m\' to print merchants,"
    print "      \'a\' to print amounts,"
    print "      \'t\' to print amount total,"
    return raw_input("      \'e\' to exit:   ")

num_lines = len(transactions_string.split('\n'))
num_transactions = num_lines / lines_per_transaction

buf = StringIO.StringIO(transactions_string)
transaction_list = []
count = 0
for i in range(num_transactions):
    transaction = ReadTransaction(buf)
    transaction_list.append(transaction)
    count = count + 1

print
print
print num_transactions, " transactions loaded."
owed = raw_input("How much owed from last statement?  ")

input = PromptForOptions()
while input != 'e':
    if input == 'd':
        ReturnDates(transaction_list)
    elif input == 'm':
        ReturnMerchants(transaction_list)
    elif input == 'a':
        ReturnAmounts(transaction_list)
    elif input == 't':
        PrintTotal(transaction_list, owed)
    else:
        print "Don't recognize input. Try again."
    input = PromptForOptions()

print
print
