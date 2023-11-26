import os

amounts = [] # list to store the amounts

while True:
    try:
        pick = int(input("Pick: "))
        cutter = int(input("Cutter: "))
        rate = int(input("Rate: "))
        quantity = int(input("Quantity: "))

        result = 40000 / pick * cutter
        price_per_pcs = rate / result / 12 * 72
        amount = price_per_pcs * quantity

        print(f"\nPRICE PER PCS : {price_per_pcs:.2f}")
        print(f"TOTAL AMOUNT: {amount:.2f}")

        amounts.append(amount) # add the amount to the list

        repeat = input("\nPress enter to run the calculation again, or type 'n' to exit: ")
        if repeat.lower() == 'n':
            break
        os.system('cls' if os.name == 'nt' else 'clear') # clears the terminal screen
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

os.system('cls' if os.name == 'nt' else 'clear') # clears the terminal screen

if len(amounts) > 0:
    print("PREVIOUS AMOUNTS:")
    for amount in amounts:
        print("       ", amount)
    print(f"\nTOTAL : {sum(amounts):.2f}")
    input("\nPress enter to exit")
else:
    print("\nNo amounts to show")
