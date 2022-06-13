from art import logo

# Adds 2 numbers
def add(a, b):
  return a + b

# Subtracts 2 numbers
def subtract(a, b):
  return a - b

# Multiplies 2 numbers
def multiply(a, b):
  return a * b

# Divides 2 numbers
def divide(a, b):
  return a / b

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

print(logo)
def calculator():
  result = n1 = float(input("\nEnter the first operand: "))
  for operation in operations:
    print(operation)
  
  response = 'y'
  
  while response == 'y':
    n1 = result
    op = input("Pick any operation: ")
    n2 = float(input("Enter the next operand: "))
    result = operations[op](n1, n2)
    
    print(f"\nResult: {n1} {op} {n2} = {result}")
    response = input(f"\nType 'y' to continue calculating with {result}, \nor type 'n' to start a new calculation: ")

    if not response == 'y':
      calculator()

calculator()