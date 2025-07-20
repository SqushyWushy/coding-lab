def calculate_change(amount):
    amount = round(amount * 100)
    money_value = [25, 10, 5, 1]
    coin_counter = 0

    for value in money_value:
        num_coins = amount // value
        amount = amount % value
        coin_counter += num_coins

    return coin_counter

def input_validation():
    while True:
        amount = input("Change: ")
        if amount.replace(".", "", 1).isdigit():
            amount = float(amount)
            if amount < 0:
                continue
            else:
                return amount
        else:
            continue


print(calculate_change(input_validation()))
