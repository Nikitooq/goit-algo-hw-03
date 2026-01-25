import random

def get_numbers_ticket(min, max, quantity):
    random_numbers = set()
    not_valid_number = []
    try:
        if max < min:
            return not_valid_number
        elif min < 1:
            return not_valid_number
        elif max > 1000:
            return not_valid_number
        else:
            while  len(random_numbers) < quantity:    
                number = random.randint(min, max)
                random_numbers.add(number)
            return sorted(random_numbers)
    except KeyboardInterrupt:
        return not_valid_number

print(get_numbers_ticket(10, 14, 6))