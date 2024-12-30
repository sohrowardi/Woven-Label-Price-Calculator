def calculate_price(pick, cutter, rate, quantity):
    result = 40000 / pick * cutter
    price_per_pcs = rate / result / 12 * 72
    amount = price_per_pcs * quantity
    return price_per_pcs, amount