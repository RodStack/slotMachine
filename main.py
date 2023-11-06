import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbols_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbols_value = {
    "A":6,
    "B":4,
    "C":2,
    "D":1
}

def check_wining(columns, bet, lines, values):
    earnings = 0 
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            earnings += values[symbol] * bet
            winning_line.append(line + 1)
    return earnings, winning_line

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbols_count in symbols.items():
        for _ in range(symbols_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def show_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
             

def deposit():
    while True:
        amount = input("How much money would like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print("Deposit must be greater than zero")
        else:
            print("Please enter a number")
    return amount

def get_number_lines():
    while True:
        lines = input("Enter the number of lines to bet (1 -"+ str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
                break
            else: 
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True:
        amount = input("How much money would like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if amount >= MIN_BET and amount <= MAX_BET:
                break
            else: 
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a valid bet")
    return amount

def game(balance):
    lines = get_number_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough money in your account. Your current balance is ${balance}")
        else:
            break
    print(f"You are beting ${bet} on {lines} lines. Total bet is ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    show_slot_machine(slots)
    earning, win_line = check_wining(slots, bet, lines, symbols_value)
    print(f"You have won {earning} from lines:", *win_line)
    return earning - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Your current balance is ${balance}")
        spin = input("Press enter to spin. (q to quit)")
        if spin == "q":
            break
        balance += game(balance)
    print(f"Your money left is ${balance}")

    
main()


        
