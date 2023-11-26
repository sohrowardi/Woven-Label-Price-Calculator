import PySimpleGUI as sg

layout = [
    [sg.Text('Pick:'), sg.Input(key='pick')],
    [sg.Text('Cutter:'), sg.Input(key='cutter')],
    [sg.Text('Rate:'), sg.Input(key='rate')],
    [sg.Text('Quantity:'), sg.Input(key='quantity')],
    [sg.Button('Calculate'), sg.Button('Clear'), sg.Button('Previous Amounts')],
    [sg.Text('', size=(30, 2), key='result')],
]

window = sg.Window('Woven Label Price Calculator', layout)

amounts = []  # list to store the amounts

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Calculate':
        try:
            pick = int(values['pick'])
            cutter = int(values['cutter'])
            rate = int(values['rate'])
            quantity = int(values['quantity'])

            result = 40000 / pick * cutter
            price_per_pcs = rate / result / 12 * 72
            amount = price_per_pcs * quantity

            window['result'].update(f"PRICE PER PCS : {price_per_pcs:.2f}\nTOTAL AMOUNT: {amount:.2f}")

            amounts.append(amount)  # add the amount to the list

        except ValueError:
            sg.popup_error("Invalid input. Please enter a number.")
    elif event == 'Clear':
        window['pick'].update('')
        window['cutter'].update('')
        window['rate'].update('')
        window['quantity'].update('')
        window['result'].update('')
    elif event == 'Previous Amounts':
        if amounts:
            sg.popup("\n".join([f"       {amount}" for amount in amounts]), title="Previous Amounts")
        else:
            sg.popup("No amounts to show", title="Previous Amounts")

window.close()
