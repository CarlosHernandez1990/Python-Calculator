calc_on = True

total = 0

operations {
  "+": add(n1,n2)
}
def add(first_number, second_number)
  return first_number + second_number

def minus(first_number, second_number)
  return first_number - second_number

def multiply(first_number, second_number)
  return first_number * second_number

def divide(first_number, second_number)
  return first_number / second_number

def calculate():
  first_calc = True
  while calc_on:
    
    if first_calc:
      first_number = int(input("What's the first number?: "))
    print("+\n-\n*\n/")
    operation = input('Pick an operation: ')
    second_number = int(input("What's the next number? "))
    if operation == "+":
      total = first_number + second_number
    elif operation == "-":
      total = first_number - second_number
    elif operation == "*":
      total = first_number * second_number
    elif operation == "/":
      total = first_number / second_number
    print(f"{float(first_number)} {operation} {float(second_number)} = {float(total)} ")
    print(f"Type 'y' to continue calculation with {float(total)}, or type 'n' to start a new calculation: ")
    cont =input().lower()
      
    if cont == "y":
      first_number = total
      first_calc = False
    if cont == "n":
      first_calc = True
      

calculate()
