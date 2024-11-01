with open ('tusk/6.txt', 'w') as file:
    text3 = """
123
aaa456
fxdya 5 0 0
"""
    file.write(text3)
total_sum = 0
with open ('tusk/6.txt', 'r') as file:
    for i in file.read():
        if i.isdigit():
            total_sum += int(i)
    print(total_sum)

