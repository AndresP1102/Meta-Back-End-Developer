# Index Error
# Starter code
items = [1,2,3,4,5]

try:
    item = items[6]
    print(item)
except Exception as e:
    print(e, "The index does not exist in the list")

# ZeroDivisionError
# Starter code
def divide_by(a, b):
    return a / b

try:
    ans = divide_by(40, 0)
    print(ans)
except ZeroDivisionError as e:
    print(e, "Number can't be devided by zero")

# FileNotFoundError
# Starter code

try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except Exception as e:
    print(e, "File could not be found")