#Write a function that accepts a non-negative integer n and a string s as parameters, and returns a string of s repeated exactly n times.
#Examples (input -> output)
#6, "I"     -> "IIIIII"
#5, "Hello" -> "HelloHelloHelloHelloHello"

def repeat_str(repeat, string):
    if repeat >= 0:
        repeat_str = string*repeat #why don't include print??, because print doesn't return anything
    return repeat_str
    
print(repeat_str(3,'hello'))