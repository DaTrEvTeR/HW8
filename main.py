# Написати валідації за допомогою регулярних виразів:
import re

# - домашній номер телефону (тільки цифри та довжина номера)

# test_phone_numbers = ['7251117', '5263548', '201548', '7251896 ', '725418b', '0327/89', '20154878']
#
# phone_numbers_regex = re.compile(r'[0-9]{7}')
#
# for phone in test_phone_numbers:
#     if phone_numbers_regex.fullmatch(phone):
#         print(f'{phone} is correct')
#     else:
#         print(f'{phone} is not correct')

# - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)

# test_mobile_phone_numbers = ['+380982445600', '380952445600', '0671212370', '+798456513218488', '6440484465', '864dd65d98d8f49v1d9', '09625314 7']
#
# mobile_phone_number_regex = re.compile(r'^\+{,1}\d{10,12}')
#
# for phone in test_mobile_phone_numbers:
#     if mobile_phone_number_regex.fullmatch(phone):
#         print(f'{phone} is correct')
#     else:
#         print(f'{phone} is not correct')

# - email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)



# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)

