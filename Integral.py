#Integral
#https://esolangs.org/wiki/Integral

def parse_single(string):
    "Parses a string of the form ax^n and returns a tuple (a, n)"
    t = ""
    i = 0
    found_x = False
    found_neg = False
    while i < len(string):
        char = string[i]
        if not char.isdigit() and not (char == "-" and i == 0):
            if char == "x":
                found_x = True
                break
            else:
                raise SyntaxError("Invalid character, 'x' expected", ("<program>", 1, i + 1, string))
        elif char == "-":
            found_neg = True
        t += char
        i += 1
    if t == "":
        coeff = 1
    elif t == "-":
        coeff = -1
    else:
        coeff = int(t)
    #Expect either "^" or end of string
    i += 1
    if i < len(string):
        if string[i] != "^":
            raise SyntaxError("Invalid character, '^' expected", ("<program>", 1, i + 1, string))
        i += 1
        e = ""
        while i < len(string):
            char = string[i]
            if not char.isdigit():
                raise SyntaxError("Invalid character, digit expected", ("<program>", 1, i + 1, string))
            e += char
            i += 1
        exponent = int(e)
    else:
        exponent = int(found_x)
    return coeff, exponent
    
def integrate_coeff(string):
    a, n = parse_single(string)
    return a/(n + 1)

def integrate_coeffs(string):
    string = "".join(string.split())
    p = string.replace("-", "+-").split("+")
    return list(map(integrate_coeff, p))
    
def run(code):
    coeffs = integrate_coeffs(code)
    instructions = []
    for c in coeffs:
        c = (int(c) - 1) % 8 + 1
        if c == 1:
            instructions.append(">")
        elif c == 2:
            instructions.append("<")
        elif c == 3:
            instructions.append("+")
        elif c == 4:
            instructions.append("-")
        elif c == 5:
            instructions.append(".")
        elif c == 6:
            instructions.append(",")
        elif c == 7:
            instructions.append("[")
        elif c == 8:
            instructions.append("]")
    cells = [0] * 30000
    pointer = 0
    bracket = 0
    bracketpairs = {}
    pstack = []
    for i, c in enumerate(instructions):
        if c == "[":
            pstack.append(i)
        elif c == "]" and len(pstack) > 0:
            bracketpairs[pstack.pop()] = i
    i = 0
    while i < len(instructions):
        c = instructions[i]
        if c == ">":
            pointer += 1
            if pointer >= len(cells):
                pointer -= 1
        elif c == "<":
            pointer -= 1
            if pointer < 0:
                pointer = 0
        elif c == "+":
            cells[pointer] += 1
            cells[pointer] %= 256
        elif c == "-":
            cells[pointer] -= 1
            cells[pointer] %= 256
        elif c == ".":
            print(chr(cells[pointer]), end="")
        elif c == ",":
            cells[pointer] = ord(input()[0])
        elif c == "[":
            if i in bracketpairs:
                if cells[pointer] == 0:
                    i = bracketpairs[i] + 1
                    continue
        elif c == "]":
            if i in bracketpairs.values():
                index = -1
                for v in bracketpairs:
                    if bracketpairs[v] == i:
                        index = v
                        break
                if index > -1 and cells[pointer] != 0:
                    i = index + 1
                    continue
        i += 1
        
def run_file(filename):
    run(open(filename).read())

if __name__ == "__main__":    
    run("""318x^105 + 315x^104 + 312x^103 + 309x^102 + 306x^101 + 303x^100 + 300x^99 + 297x^98 + 686x^97 + 97x^96 + 
    288x^95 + 285x^94 + 282x^93 + 279x^92 + 644x^91 + 91x^90 + 270x^89 + 267x^88 + 88x^87 + 261x^86 + 
    258x^85 + 255x^84 + 84x^83 + 249x^82 + 246x^81 + 243x^80 + 80x^79 + 237x^78 + 156x^77 + 154x^76 + 
    152x^75 + 150x^74 + 296x^73 + 584x^72 + 72x^71 + 213x^70 + 70x^69 + 207x^68 + 68x^67 + 268x^66 + 
    66x^65 + 65x^64 + 192x^63 + 441x^62 + 124x^61 + 488x^60 + 120x^59 + 236x^58 + 464x^57 + 57x^56 + 
    56x^55 + 275x^54 + 54x^53 + 212x^52 + 208x^51 + 204x^50 + 250x^49 + 147x^48 + 144x^47 + 141x^46 + 
    138x^45 + 135x^44 + 132x^43 + 129x^42 + 210x^41 + 205x^40 + 120x^39 + 117x^38 + 114x^37 + 185x^36 + 
    36x^35 + 35x^34 + 170x^33 + 66x^32 + 128x^31 + 155x^30 + 60x^29 + 145x^28 + 84x^27 + 81x^26 + 
    78x^25 + 125x^24 + 96x^23 + 92x^22 + 88x^21 + 84x^20 + 80x^19 + 76x^18 + 90x^17 + 68x^16 + 
    64x^15 + 60x^14 + 56x^13 + 52x^12 + 48x^11 + 44x^10 + 40x^9 + 45x^8 + 8x^7 + 7x^6 + 
    18x^5 + 25x^4 + 4x^3 + 9x^2 + 6x^1 + 5""")
