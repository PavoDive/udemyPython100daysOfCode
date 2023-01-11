from art import logo

def add(n1, n2):
  """Add two numbers"""
  return n1 + n2

def subtract(n1, n2):
  """Subtract n2 from n1"""
  return n1 - n2

def multiply(n1, n2):
  """Multiply n1 * n2"""
  return n1 * n2

def divide(n1, n2):
  """Divide n1 in n2"""
  return n1 / n2

def calculator():
  print(logo)
  
  operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
  
  num_1 = float(input("Introduce the first number: "))
  
  for operation in operations:
    print(operation)
  
  want_to_quit = False
  

  while not want_to_quit:
    operation_symbol = input("Pick an operation from the lines above: ")
    
    num_2 = float(input("What's the next number?: "))
    
    answer = operations[operation_symbol](num_1, num_2)
    
    print(f"{num_1} {operation_symbol} {num_2} = {answer}")
    
    continue_with_answer = input(f"Want to continue with {answer}? Type 'y' to continue, 'n' to continue with different numbers, or 'q' to quit: ")
    
    if continue_with_answer == "y":
      num_1 = answer
    elif continue_with_answer == "n":
      calculator()
    else:
      break

calculator()
