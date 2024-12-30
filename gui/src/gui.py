from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from calculator import calculate_price

class PriceCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Woven Label Price Calculator")

        self.pick_var = StringVar()
        self.cutter_var = StringVar()
        self.rate_var = StringVar()
        self.quantity_var = StringVar()

        Label(master, text="Pick:").grid(row=0)
        Label(master, text="Cutter:").grid(row=1)
        Label(master, text="Rate:").grid(row=2)
        Label(master, text="Quantity:").grid(row=3)

        Entry(master, textvariable=self.pick_var).grid(row=0, column=1)
        Entry(master, textvariable=self.cutter_var).grid(row=1, column=1)
        Entry(master, textvariable=self.rate_var).grid(row=2, column=1)
        Entry(master, textvariable=self.quantity_var).grid(row=3, column=1)

        Button(master, text="Calculate", command=self.calculate).grid(row=4, column=1)

        self.result_label = Label(master, text="")
        self.result_label.grid(row=5, columnspan=2)

    def calculate(self):
        try:
            pick = int(self.pick_var.get())
            cutter = int(self.cutter_var.get())
            rate = int(self.rate_var.get())
            quantity = int(self.quantity_var.get())

            price_per_pcs, total_amount = calculate_price(pick, cutter, rate, quantity)

            self.result_label.config(text=f"PRICE PER PCS: {price_per_pcs:.2f}\nTOTAL AMOUNT: {total_amount:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers for all fields.")

def main():
    root = Tk()
    app = PriceCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()