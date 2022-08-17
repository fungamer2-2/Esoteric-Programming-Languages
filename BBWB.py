#BBWB - Brainfuck But With Buffer
#https://esolangs.org/wiki/Brainfuck_But_With_Buffer

def run(code):
	bracket = 0
	lbrackets = {}
	rbrackets = {}
	pstack = []
	for i, c in enumerate(code):
		if c == "[":
			pstack.append(i)
		elif c == "]" and len(pstack) > 0:
			pos = pstack.pop()
			lbrackets[pos] = i
			rbrackets[i] = pos
	buffer = 0
	pointer = 0
	i = 0
	tape = [0]*30000
	while i < len(code):
		char = code[i]
		if char == "+":
			buffer += 1
			buffer %= 256
		elif char == "-":
			buffer -= 1
			buffer %= 256
		elif char == "#":
			buffer = 0
		elif char == "^":
			tape[pointer] = buffer
		elif char == "v":
			buffer = tape[pointer]
		elif char == "<":
			pointer -= 1
			pointer %= len(tape)
		elif char == ">":
			pointer += 1
			pointer %= len(tape)
		elif char == ".":
			print(buffer, end="")
		elif char == ":":
			print(chr(buffer), end="")
		elif char == ",":
			buffer = int(input())
		elif char == ";":
			buffer = ord(input()[0])
		elif char == "[":
			if tape[pointer] == 0:
				i = lbrackets[i] + 1
				continue
		elif char == "]":
			if tape[pointer] != 0:
				i = rbrackets[i] + 1
				continue
		i += 1
		
def run_file(filename):
	run(open(filename).read())
		
if __name__ == "__main__":		
	code = """
	+++++++++^#[>v++++++++^#<v-^#]>v:
	#
	+++++++++++++++++++++++^#[>v+++^#<v-^#]>v: 
	#
	+++++++++++++++++++^#[>v++++^#<v-^#]>v: :
	#
	++++++++++^#[>v++++++++^#<v-^#]>v-:
	#
	+++++++++++^#[>v++++^#<v-^#]>v:
	#
	++++++++^#[>v++++^#<v-^#]>v:
	#
	+++++++++++^#[>v++++++++^#<v-^#]>v-:
	#
	++++++++++^#[>v++++++++^#<v-^#]>v-:
	#
	++++++++++^#[>v++++++++^#<v-^#]>v++:
	#
	+++++++++++++++++++^#[>v++++^#<v-^#]>v:
	#
	+++++++++++++++++^#[>v++++^#<v-^#]>v:
	#
	+++++++++++^#[>v+++^#<v-^#]>v:
	#
	++++++++++:
	"""
	
	run(code)
