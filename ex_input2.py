
a = int(input("Input 1st number : "))
b = int(input("Input 2nd number : "))
c = (input("input operater(+, *): "))

def add(a,b):
    return a+b
    
def multi(a,b):
    return a*b
    
if c == '+':
    result = add(a,b)
    print(result)
    
elif c == '*':
    result = multi(a,b)
    print(result)
else:
    pass
