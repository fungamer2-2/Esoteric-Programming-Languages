def run(code):
  from sys import stdout
  stack = []
  x = 0
  y = 0
  xdir = 1
  ydir = 0
  code = code.splitlines()
  while code[y][x] != "@":
    char = code[y][x]
    if char.isdigit():
      stack.append(int(char))
    if char == "+":
      stack.append(stack.pop() + stack.pop())
    elif char == "-":
      a, b = stack.pop(), stack.pop()
      stack.append(b - a)
    elif char == "*":
      stack.append(stack.pop() * stack.pop())
    elif char == "/":
      a, b = stack.pop(), stack.pop()
      if a == 0:
        #"According to the specifications, if a is zero, ask the user what result they want."
        while True:
          value = input(f"Looks like you're trying to diving {b} by zero, what do you want the result to be? (must be an integer)")
          try:
            value = int(value)
          except ValueError:
            pass
          else:
            break
        stack.append(value)
      else:
        stack.append(b // a)
    elif char == ".":
      print(stack.pop())
    elif char == ",":
      print(chr(stack.pop()), end="")
    x += xdir
    y += ydir
    if x >= len(code[y]):
      x = 0
    elif x < 0:
      x = len(code[y]) - 1
    if y >= len(code):
      y = 0
    elif y < 0:
      y = len(code) - 1
      
  stdout.flush()

def run_file(filename):
  run(open(filename).read())
