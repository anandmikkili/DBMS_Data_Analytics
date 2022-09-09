def addition(*x):
    result=0
    for i in x:
        result = result + i
    return result

def subtraction(x,y):
    result=(x-y)
    return result

def multiplication(x,y):
    result=x*y
    return result

def division(x,y):
    result=x/y
    return result


def returns_multiple(x,y):
    return x+5, y+10;

def hello():
    print("Have A Nice Day...!")



print(addition(1,2,3,4,5))
print(subtraction(5,10))
print(multiplication(10,6))
print(division(10,3))

print(type(returns_multiple(1,2)))
print(returns_multiple(1,2))
hello()




        
