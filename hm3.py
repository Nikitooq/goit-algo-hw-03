import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r"\D", "", phone_number)
    if not cleaned_number.startswith("+"):
        if cleaned_number.startswith("380"):
            cleaned_number = "+" + cleaned_number
            return cleaned_number
        else:
            cleaned_number = "+38" + cleaned_number
    return cleaned_number



raw_numbers = "067\\t123 4567"

sanitized_numbers = normalize_phone(raw_numbers)
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


