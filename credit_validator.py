def credit_card_digit_length(number):
    print(f"Credit card digit length: {len(number)}")


def card_type(number):
    if number.startswith("4"):
        print("Credit card type: Visa card")
    elif number.startswith("5"):
        print("Credit card type: Master card")
    elif number.startswith("37"):
        print("Credit card type: American express card")
    elif number.startswith("6"):
        print("Credit card type: Discover card")
    else:
        print("Credit card type: Invalid")



def credit_card_number(card):
    print(f"Credit card Number: {card}")


def credit_card_validator_status(number):
    sum_even = 0
    sum_odd = 0

   
    for index in range(len(number)):
        digit = int(number[-(index + 1)])

        if index % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
            sum_even += digit
        else:
            sum_odd += digit

    total = sum_even + sum_odd

    if total % 10 == 0:
        print("Credit card validity status: valid")
    else:
        print("Credit card validity status: invalid")

