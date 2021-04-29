import math

cmd = ""

while cmd !="close":
  cmd = input("(calc) ~ $")

  if cmd == "help":
    print("help - To get help")
    print("close - To close the program")
    print("add - To add 2 numbers")
    print("subtract - To subtract 2 numbers")
    print("multiply - To multiply 2 numbers")
    print("divide - To divide 2 numbers")
    print("pow - To get the powers")
    print("sin - To get the sin of number")
    print("cos - To get the cos of number")
    print("tan - To get the tan of number")

  elif cmd == "add":
    num1 = float(input("(num1) ~ $"))
    num2 = float(input("(num2) ~ $"))
    result = num1 + num2
    print(f"(rslt) ~ ${result}")

  elif cmd == "subtract":
    num1 = float(input("(num1) ~ $"))
    num2 = float(input("(num2) ~ $"))
    result = num1 - num2
    print(f"(rslt) ~ ${result}")

  elif cmd == "multiply":
    num1 = float(input("(num1) ~ $"))
    num2 = float(input("(num2) ~ $"))
    result = num1 * num2
    print(f"(rslt) ~ ${result}")

  elif cmd == "divide":
    num1 = float(input("(num1) ~ $"))
    num2 = float(input("(num2) ~ $"))
    result = num1 / num2
    print(f"(rslt) ~ ${result}")

  elif cmd == "pow":
    num1 = float(input("(num1) ~ $"))
    num2 = float(input("(num2) ~ $"))
    result = num1 ** num2
    print(f"(rslt) ~ ${result}")

  elif cmd == "sin":
    numb = float(input("(numb) ~ $"))
    result = math.sin(math.radians(numb))
    print(f"(rslt) ~ ${result}")

  elif cmd == "cos":
    numb = float(input("(numb) ~ $"))
    result = math.cos(math.radians(numb))
    print(f"(rslt) ~ ${result}")

  elif cmd == "tan":
    numb = float(input("(numb) ~ $"))
    result = math.tan(math.radians(numb))
    print(f"(rslt) ~ ${result}")