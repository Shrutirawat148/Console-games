import random
#back jaane ka system 
MAX_LINES = 3
mbet=100
minbet=1

rows=3
cols=9

symbol_count={
    "A":4,
    "B":6,
    "C":8,
    "D":10
}
symbol_value={
    "A":10,
    "B":8,
    "C":6,
    "D":4
}

def get_slot_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns=[]
    for _ in range(rows):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(cols):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column) 
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i ,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end="|")
            else:
                print(column[row],end="")

        print()

def check_wins(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol !=symbol_to_check:
                break
        else:
            winnings+=values[symbol]*bet
            winning_lines.append(lines+1)
    return winnings,winning_lines



def deposit():
    while True:
       amount= input("enter your deposit money  ")
       if amount.isdigit():
            amount=int(amount)
            if amount  >0:
               break
            else:
               print("amount must be greater than zero")
       else:
            print("enter a number")
    return amount

def num_of_lines():
    while True:
       lines= input("enter the number of lines to bet on (1-" +str(MAX_LINES)+")? " )
       if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <= MAX_LINES:
               break
            else:
               print("Enter the valid number")
       else:
            print("enter a number")
    return lines

def get_bet():
    while True:
       amount= input("enter your bet money on each line ")
       if amount.isdigit():
            amount=int(amount)
            if minbet <= amount <= mbet:
               break
            else:
               print(f"amount must be between {minbet}-{mbet}" )
       else:
            print("enter a number")
    return amount

def spin(balance):
    lines = num_of_lines()
    while True:
       bet=get_bet()
       totalbet=bet*lines
       if totalbet>balance:
           print(f"you do not have enough balance, your current amount is {balance}")
       else:
           break
           
    print(f"you are betting {bet} on {lines}.Your total bet is {totalbet}.")
    slots=get_slot_spin(rows,cols,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines=check_wins(slots,lines,bet,symbol_value)
    print(f"you won {winnings}.")
    print(f"you won on lines:",*winning_lines)
    return winnings-totalbet

def main():
    balance = deposit()
    while True:
        print(f"current balance is {balance}")
        ans =input("press enter to spin or q to quit: ")
        if ans=="q":
            break
        balance += spin(balance)
    print(f"you left with {balance}")

main()   
               