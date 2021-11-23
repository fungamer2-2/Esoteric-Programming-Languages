#BeeScript
#https://esolangs.org/wiki/BeeScript

from collections import deque

bee_movie = open("bee-movie-script.txt").read()

class BeeScriptError(Exception):
  pass

class Stack():
  
  def __init__(self):
    self.data = deque()
    
  def push(self, value):
    self.data.append(value)
    
  def peek(self):
    if not self.data:
      raise BeeScriptError("stack underflow")
    return self.data[-1]
    
  def pop(self):
    if not self.data:
      raise BeeScriptError("stack underflow")
    return self.data.pop()
    
  def rotate(self, direction):
    if len(self.data) > 1:
      self.data.rotate(direction)
      
def run(code):
  lines = code.splitlines()
  stack = Stack()
  i = 0
  while i < len(lines):
    line = lines[i]
    l = line.split()
    command, arg = l[0], l[1] if len(l) > 1 else None
    if command == "AVIATE":
      try:
        index = int(arg)
      except ValueError:
        raise BeeScriptError("AVIATE value must be an integer")
      stack.push(ord(bee_movie[index]))
    elif command == "BEE":
      stack.push(stack.peek())
    elif command == "BLACK":
      print(chr(stack.pop()), end="")
    elif command == "BARRY":
      a, b = stack.pop(), stack.pop()
      stack.push(b - a)
    elif command == "FLY":
      try:
        line_num = int(arg)
      except ValueError:
        raise BeeScriptError("AVIATE value must be an integer")
      if stack.pop() != 0:
        i = line_num - 1
        continue
    elif command == "ROTATE":
      stack.rotate(-1)
    elif command == "ROTAT":
      stack.rotate(1)
    elif command == "YELLOW":
      stack.push(ord(input()[0]))
      
    i += 1
      
def run_file(filename):
  run(open(filename).read())
  
__all__ = ["run", "run_file"]

if __name__ == "__main__":
  run_file("beescript-example.txt")
