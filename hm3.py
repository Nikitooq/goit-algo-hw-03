import re

def normalize_phone(phone_number):
    pattern = r"[+, 0-9]"
    cleaned_number = re.sub(r"\s", "", phone_number)
    cleaned_number = re.findall(pattern, cleaned_number)
    cleaned_number = "".join(cleaned_number)
    print(cleaned_number)
    if not cleaned_number.startswith("+"):
        if cleaned_number.startswith("380"):
            cleaned_number = "+" + cleaned_number
            return cleaned_number
        else:
            cleaned_number = "+38" + cleaned_number
    return cleaned_number



raw_numbers = "+432 10 123 45 67"

sanitized_numbers = normalize_phone(raw_numbers)
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


