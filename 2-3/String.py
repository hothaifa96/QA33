starbucks = '+ 1,250 USD'


def get_number(text):
    amount = starbucks[2:-4]  # 1,250
    f = float(amount.replace(',', ''))
    return f


number = get_number(starbucks)
print(number)
