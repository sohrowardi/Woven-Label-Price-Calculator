import tkinter as tk
from tkinter import messagebox
from calculator import calculate_price

class PriceCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Woven Label Price Calculator")

        self.create_widgets()
        self.amounts = []  # list to store the amounts

    def create_widgets(self):
        tk.Label(self.root, text="Pick:").grid(row=0, column=0)
        self.pick_entry = tk.Entry(self.root)
        self.pick_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Cutter:").grid(row=1, column=0)
        self.cutter_entry = tk.Entry(self.root)
        self.cutter_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Rate:").grid(row=2, column=0)
        self.rate_entry = tk.Entry(self.root)
        self.rate_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Quantity:").grid(row=3, column=0)
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.grid(row=3, column=1)

        tk.Label(self.root, text="Discount (%):").grid(row=4, column=0)
        self.discount_entry = tk.Entry(self.root)
        self.discount_entry.grid(row=4, column=1)

        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=5, columnspan=2)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=6, columnspan=2)

        self.previous_amounts_label = tk.Label(self.root, text="")
        self.previous_amounts_label.grid(row=7, columnspan=2)

    def calculate(self):
        try:
            pick = int(self.pick_entry.get())
            cutter = int(self.cutter_entry.get())
            rate = int(self.rate_entry.get())
            quantity = int(self.quantity_entry.get())
            discount = float(self.discount_entry.get())

            result = 40000 / pick * cutter
            price_per_pcs = rate / result / 12 * 72
            amount = price_per_pcs * quantity
            discounted_amount = amount * (1 - discount / 100)

            self.amounts.append(amount)  # add the amount to the list

            self.result_label.config(text=f"PRICE PER PCS: {price_per_pcs:.2f}\nTOTAL AMOUNT: {amount:.2f}\nDISCOUNTED AMOUNT: {discounted_amount:.2f}")
            self.update_previous_amounts()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")

    def update_previous_amounts(self):
        if len(self.amounts) > 0:
            amounts_text = "PREVIOUS AMOUNTS:\n" + "\n".join(f"       {amount:.2f}" for amount in self.amounts)
            total_text = f"\nTOTAL: {sum(self.amounts):.2f}"
            self.previous_amounts_label.config(text=amounts_text + total_text)
        else:
            self.previous_amounts_label.config(text="No amounts to show")

if __name__ == "__main__":
    root = tk.Tk()
    app = PriceCalculatorApp(root)
    root.mainloop()