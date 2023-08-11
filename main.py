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

# test_emails = ['darkweider0@gmail.com', 'singe r@mac.com', 'pen-na@verizon.net', 'ca_menisch@msn.com', 'jsno.ver@mac..com']
#
# email_regex = re.compile(r"^[A-Za-z0-9]+[._]?[A-Za-z0-9]+@[A-Za-z]+[.][A-Za-z]{2,}$")
#
# for email in test_emails:
#     if email_regex.match(email):
#         print(f"Email: {email} is correct")
#     else:
#         print(f"Email: {email} is not correct")

# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)

# test_FIO = ['Носко Май  Адамович', 'Курпіта Позвізд Адр1анович', 'Андрійович Еміль Мстиславович', 'Сеньків Я Тимурович', 'Стуауст Сарматович']
#
# fio_regex = re.compile(r'[А-Яа-яіІїЇ]{2,20} [А-Яа-яіІїЇ]{2,20} [А-Яа-яіІїЇ]{2,20}')
#
# for fio in test_FIO:
#     if fio_regex.fullmatch(fio):
#         print(f'{fio} is correct')
#     else:
#         print(f'{fio} is not correct')

# ALL TASKS DONE