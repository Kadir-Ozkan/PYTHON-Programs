#This file reviews the built-in functions of Python
#In order to supply a permissive environment for all of the built-in functions a dictionary will be created.
#Built-in functions A: abs(), aiter(), all(), any(), anext(), ascii()
#Built-in functions B: bin(), bool(), breakpoint(), bytearray(), bytes()
#Built-in functions C: callable(), chr(*), classmethod(), compile(), complex()
#Built-in functions D: delattr(), dict(), dir(*), divmod()
#Built-in functions E: enumerate(), eval(), exec()
#Built-in functions F: filter(), float(), format(), frozenset()
#Built-in functions G: getattr(), globals()
#Built-in functions H: hasattr(), hash(), help(), hex()
#Built-in functions I: id(), input(), int(), isinstance(), issubclass(), iter()
#Built-in functions L: len(*), list(*), locals()
#Built-in functions M: map(), max(*), memoryview(), min(*)
#Built-in functions N: next()
#Built-in functions O: object(), oct(), open(), ord(*)
#Built-in functions P: pow(), print(*), property()
#Built-in functions R: range(*), repr(), reversed(), round()
#Built-in functions S: set(), setattr(), slice(), sorted(), staticmethod(), str(), sum(), super()
#Built-in functions T: tuple(), type(*)   
#Built-in functions V: vars()
#Built-in functions Z: zip()

from functions import mylambda

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10] 
lista = ["a", "b", "c", "d", "e"]
listb = ["e", "f", "g", "h", "i"] 
mykey = ""
mydict = {}

def dictionary(x = 1, y = 1, z = "+", t = "d"):
    '''This function is built for studying built-in functions and returns many values with different types:
    1: Returns mathematical results when two numbers (x,y) a math operator(z) and a mod(t="c") are entered as arguments
    2: Returns ASCII calculations as two characters (x,y), a math operator(z) and a mod(t="a") are entered as arguments
    3: Returns string calculations as lists when two string lists (x,y), a math operator(z) and a mod(t="s") are entered as arguments
    4: Returns cyphered text when two lists (x,y), a math operator(z) and a mod(t="*") are entered as arguments
    5: Returns built in functions of a module when a module name and mod(t = "d") are entered as arguments
    6: Add to the personal dictionary when a string with a ":" is given and mode (t = "add") entered as arguments
    '''
    if t == "c" and (type(x) == int and type(y) == int) or (type(x) == float and type(y) == float):
        if z == "+":
            return(x + y)
        elif z == "-":
            return(x - y)
        elif z == "*":
            return(x * y)
        elif z == "/":
            return(x / y)
        elif z == "**":
            return(x ** y)
    if t == "a" and (type(x) == str and type(y) == str):
        if z == "+":
            return chr(ord(x) + ord(y))
        elif z == "-":
            return chr((ord(x) - ord(y)))
        elif z == "*":
            return chr((ord(x) * ord(y)))
        elif z == "/":
            return chr((ord(x) / ord(y)))
        elif z == "**":
            return chr((ord(x) ** ord(y)))
        else:
            return ("invalid") 
    if t == "c" and (type(x) == list and type(y) == list):
        l = list()
        for i in range(len(x)):
            if z == "+":
                l.append(x[i] + y[i])
            elif z == "-":
                l.append(x[i] - y[i])  
            elif z == "*":
                l.append(x[i] * y[i])
            elif z == "/":
                l.append(x[i] / y[i])
            elif z == "**":
                l.append(x[i] ** y[i])
            else:
                return ("invalid") 
        return (l, "min: ", min(l), "max: ", max(l))
    if t == "s" and (type(x) == list and type(y) == list):
        cypher = list()
        index = 0
        for i in x:
            if z == "+":
                cypher.append(chr(ord(x[index]) + ord(y[index])))
            elif z == "-":
                cypher.append(chr(ord(x[i]) - ord(y[i])))
            elif z == "*":
                cypher.append(chr(ord(x[i]) * ord(y[i])))
            elif z == "/":
                cypher.append(chr(ord(x[i]) / ord(y[i])))
            elif z == "**":
                cypher.append(chr(ord(x[i]) ** ord(y[i])))
            else:
                return ("invalid") 
            index += 1
        return (cypher)    
    if t == "d" and type(x) == str: 
        return dir(x) 
    if t == "add" and type(x) == str:
        k = 0
        for harf in x:
            if harf != ":":
                global mykey
                mykey += harf
                k += 1
            else:
                hit = k
                global mydict
                mydict[mykey] = x[hit+1 :]
                break
        return mykey 
    if x == "mydictionary": 
        return mydict 
       
print("Integer calculation: ", dictionary(3, 4, "+", "c"))
print("Float calculation: ", dictionary(3.14, 3.14, "+", "c"))
print("ASCII calculation: ", dictionary("f", "r", "+", "a"))
print("List calculation: ", dictionary(list1, list2, "+", "c"))
print("Cypher Generation: ", dictionary(lista, listb, "+", "s"))
print("Python in-built functions HELPER: ", dictionary("math", t = "d"))
print()
if dictionary("grooming: tımarlamak, saça sakala çeki düzen vermek", t = "add"):
    print(f'{mykey} was added to your dictionary.')
print(f'The contents of your dictionary are: ', mydict)


print(mylambda(-1, t="özet"))