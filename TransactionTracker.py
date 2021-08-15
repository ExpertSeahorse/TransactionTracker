import json
import os
    

class Transaction:
    def __init__(self, sender, receiver, amount) -> None:
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
    
    def toDict(self) -> str:
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount
        }
    def __str__(self) -> str:
        return players[self.sender] + " -> " + players[self.receiver] + ": " + str(self.amount)


players = []
transactions = []


def save(filename="transaction_save_file"):
    filename += ".log"
    if os.path.isfile(filename):
        print("That file already exists!\n")
        i = input("Do you want to overwrite it? (Y/n): ")
        inp = True
        while inp:
            if i[0].lower() == 'y':
                inp = False 
            elif i[0].lower() == 'n':
                return False
            else:
                print("please enter either 'y' or 'n':")            


    with open(filename, 'w') as fout:
        json.dump(str(transactions), fout)
    return True

def load(filename):
    if ".log" not in filename:
        filename += ".log"
    
    flag = True
    while flag:
        try:
            with open(filename, 'r') as fin:
                temp = json.load(fin)
                global transactions
                transactions = [Transaction(trans["sender"], trans["receiver"], trans["amount"]) for trans in temp]
                flag = True
        except FileNotFoundError:
            print("file not found.")
            filename = input("Please enter a new filename: ")


# Input player names at the start
i = input("Please enter the name of the first player: ")
players.append(i)
i = input("Please enter the name of the second player: ")
players.append(i)

flag = True
while flag:
    i = input("Please enter the name of an additional player or 0 to continue: ")
    if i == "0":
        flag = False
        continue
    else:
        players.append(i)


# Start recording transactions
print(
    "Please enter the transactions as (sender, receiver, amount)\n"
    "Enter the transactions like the following:\n"
    "1, 2, 26\n"
    "Players:\n"
)
[print(str(i)+". "+p) for i, p in enumerate(players)]
print(
    "a. save\n"
    "b. load\n"
    "c. exit\n"
)

while True:
    print("enter the next transaction:")
    trans = input().split(",")
    trans = [int(t.strip()) for t in trans]
    transactions.append(Transaction(*trans))

    # for t in transactions:
    #     print(t)