import json
import os
import sys


class Transaction:
    def __init__(self, sender, receiver, amount) -> None:
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def toDict(self) -> str:
        return {"sender": self.sender, "receiver": self.receiver, "amount": self.amount}

    def __str__(self) -> str:
        return (
            players[self.sender]
            + " -> "
            + players[self.receiver]
            + ": "
            + str(self.amount)
        )


players = []
transactions = []


def delta(p1, p2):
    total = 0
    for t in transactions:
        if t.sender == p1:
            total -= t.amount
        elif t.sender == p2:
            total += t.amount
    print("####################")
    if total >= 0:
        print(players[p1], "has made $" + str(total), "from", players[p2])
    else:
        print(players[p1], "has lost $" + str(total + (-2 * total)), "to", players[p2])
    print("####################")


def save(filename="transaction_save_file"):
    filename += ".log"
    if os.path.isfile(filename):
        print("That file already exists!\n")
        i = input("Do you want to overwrite it? (Y/n): ")
        inp = True
        while inp:
            if i[0].lower() == "y":
                inp = False
            elif i[0].lower() == "n":
                return False
            else:
                print("please enter either 'y' or 'n':")

    with open(filename, "w") as fout:
        json.dump(str(transactions), fout)
    return True


def load(filename):
    if ".log" not in filename:
        filename += ".log"

    flag = True
    while flag:
        try:
            with open(filename, "r") as fin:
                temp = json.load(fin)
                global transactions
                transactions = [
                    Transaction(trans["sender"], trans["receiver"], trans["amount"])
                    for trans in temp
                ]
                flag = True
        except FileNotFoundError:
            print("file not found.")
            filename = input("Please enter a new filename: ")

    print("####################")


print("####################")
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
print("####################")

# Start recording transactions
print(
    "\nPlease enter the transactions as (sender, receiver, amount)\n"
    "Enter the transactions like the following:\n"
    "1, 2, 26\n"
    "Players:"
)
[print(str(i) + ". " + p) for i, p in enumerate(players)]
print("\n" "a. save\n" "b. load\n" "c. exit\n" "d. delta")

while True:
    # get next transaction
    print("\nEnter the next transaction:")
    trans = input().split(",")
    trans = [t.strip() for t in trans]

    # process edge cases
    if trans[0].lower() == "a":
        filename = input("Save transactions as: ")
        save(filename)
    elif trans[0].lower() == "b":
        # TODO: Detect save files in the same directory
        filename = input("The saved file is called: ")
        load(filename)
    elif trans[0].lower() == "c":
        sys.exit()
    elif trans[0].lower() == "d":
        p = True
        while p:
            player1 = input("enter the sender: ")
            try:
                i1 = players.index(player1)
                p = False
            except ValueError:
                print(player1, "is not a valid player. Please")
        p = True
        while p:
            player2 = input("Enter the receiver: ")
            try:
                i2 = players.index(player2)
                p = False
            except ValueError:
                print(player2, "is not a valid player. Please")

        delta(i1, i2)
    # process main requests
    else:
        trans = [int(t) for t in trans]
        transactions.append(Transaction(*trans))
        # for t in transactions:
        #     print(t)
