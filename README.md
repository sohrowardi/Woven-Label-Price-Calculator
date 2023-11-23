# Woven Label Price Calculator

## Overview

The "Woven-Label-Price-Calculator.py" script is a simple tool designed to calculate the price of woven labels based on user input. It takes into account parameters such as the pick, cutter, rate, and quantity to provide a per-piece price and total amount for the given order.

## How it Works

1. **Pick:** Number of picks.
2. **Cutter:** Cutter value.
3. **Rate:** Rate value.
4. **Quantity:** Number of labels in the order.

The script uses these inputs to calculate the price per piece and the total amount for the given quantity.

## Usage

1. Run the script in a Python environment.
2. Enter the required parameters when prompted (pick, cutter, rate, quantity).
3. The script will display the price per piece and total amount for the given order.
4. Press Enter to run the calculation again or type 'n' to exit.
5. If you choose to exit, the script will display previous amounts and the total.

**Note:** Ensure that you enter valid numerical values for the parameters. If an invalid input is detected, the script will prompt you to enter a number.
and run pyinstaller Woven-Label-Price-Calculator.py --onefile --windowed to have a .exe file


### Example:

```bash
Pick: 10
Cutter: 5
Rate: 500
Quantity: 100

PRICE PER PCS : 8.00
TOTAL AMOUNT: 800.00

Press enter to run the calculation again, or type 'n' to exit:
