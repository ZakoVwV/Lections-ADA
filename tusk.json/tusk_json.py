import json
# info = {
#     'name':'book',
#     'price':'250',
#     'availability': False
# }
# json_info = json.dumps(info)
# print(json_info)

# with open ('tusk.json/book.json', 'w') as file:
#     info_book = {
#         'name': 'Hary потный',
#         'autor': 'Doby',
#         'year': '2024',
#         'izadatelstvo': 'dambi'
#     }
#     json_info_book = json.dumps(info_book) 
#     print(json_info_book)

# with open ('tusk.json/book.json', 'a') as file:
#     file.write(json_info_book)

# with open ('tusk.json/book.json', 'r') as file:
#     good = json.load(file)
#     print(good)

# with open ('tusk.json/book.json', 'r') as file:
#     infos = {
#         'name':'Me',
#         'age':'14',
#         'city':'Bishkek'
#     }
#     bredkakoito = json.dumps(infos)
#     json.loads(bredkakoito)


# with open ('tusk.json/products.json', 'w') as file:  
#     products = [
#     {"name": "Laptop", "price": 1200, "quantity": 5},
#     {"name": "Mouse", "price": 25, "quantity": 50},
#     {"name": "Keyboard", "price": 70, "quantity": 20}
# ]
#     json.dump(products, file)

# with open ('tusk.json/products.json', 'r') as file:  
#     products = json.load(file)
# for i in products:
#     i['price'] *= 1.1

# with open ('tusk.json/products.json', 'w') as file2:
#     json.dump(products, file2)
    
# new_product = {
#     'name':'iphone',
#     'price':'1200',
#     'quantity':'5'  
# }
# with open ('tusk.json/products.json', 'r') as file:
#     products = json.load(file)

# products.append(new_product)

# with open ('tusk.json/products.json', 'w') as file:
#     json.dump(products, file)

employees = [
    {'name':'Nikit', 'position': 'Manager', 'salary':1500},
    {'name':'Ertay','posotion':'Data science', 'salary':2000},
    {'name':'Katana','posotion':'Backend Developer','salary':None},
     {'name':'Tima','posotion':'ML ingeener', 'salary': None}
]

with open ('tusk.json/employees.json', 'w') as file:
    json.dump(employees, file)

with open ('tusk.json/employees.json', 'r') as file:
    employees = json.load(file)

for employee in employees:
    if employee['salary'] is not None:
        print(employee)

from datetime import date, timedelta

orders = [
    {
        "order_id": 1,
        "customer": "Alice",
        "date": str(date(2024, 1, 10)),
        "products": [
            {"name": "Laptop", "quantity": 1, "price": 1200},
            {"name": "Mouse", "quantity": 2, "price": 25},
            {"name": "Monitor", "quantity": 1, "price": 300},
            {"name": "Keyboard", "quantity": 1, "price": 70}
        ]
    },
    {
        "order_id": 2,
        "customer": "Bob",
        "date": str(date(2024, 1, 12)),
        "products": [
            {"name": "Monitor", "quantity": 1, "price": 300},
            {"name": "Keyboard", "quantity": 1, "price": 70}
        ]
    },
    {
        "order_id": 3,
        "customer": "Mariya",
        "date": str(date(2023, 12, 12)),
        "products": [
            {"name": "Monitor", "quantity": 2, "price": 300},
        ]
    },
        {
        "order_id": 4,
        "customer": "Marat",
        "date": str(date(2024, 8, 10)),
        "products": [
            {"name": "Mouse", "quantity": 122, "price": 25},
            {"name": "Monitor", "quantity": 12, "price": 300},
            {"name": "Keyboard", "quantity": 11, "price": 70}
        ]
    },
]


# with open ('tusk.json/orders.json', 'w') as file:
#     json.dump(orders, file)

# with open ('tusk.json/orders.json', 'r') as file:
#     orders = json.load(file)
#     for order in orders:
#         if len(order['products']) > 2:
#             print(order)

# with open ('tusk.json/orders.json', 'r') as file:
#     orders = json.load(file)

# month_ago = date.today() - timedelta(days=30)

# for order in orders:
#     order_date = date.fromisoformat(order['date'])

#     if order_date < month_ago:
#         order['status'] = 'delivered'

# with open ('tusk.json/orders.json', 'w') as file:
#     json.dump(orders, file)

with open ('tusk.json/orders.json', 'r') as file:
    orders = json.load(file)

total_quantity = 0
total_sales = 0

for order in orders:
    for product in order['products']:
        total_quantity += product['quantity']
        total_sales += product['quantity'] * product['price']

print(f'Общее количество проданного товара: {total_quantity}')
print(f'Общая сумма всех заказов: {total_sales}')