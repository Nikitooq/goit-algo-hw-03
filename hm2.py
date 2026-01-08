import random

def get_numbers_ticket(min, max, quantity):
    random_numbers = set()
    while  len(random_numbers) < quantity:
        if min < 1:
            print("Мінімальне значення повинне бути не менше 1")
            break
            return None
        elif max > 1000:
            print("Максимальне число не повинно бути більше 1000")
            break
            return None
        else:
            number = random.randint(min, max)
            random_numbers.add(number)
    return sorted(random_numbers)

print(get_numbers_ticket(1, 50, 6))
