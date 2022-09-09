operation_type = eval(input("Please enter the operation type: 1-addition 2-subtraction 3-multiplication 4-division"))
#opr = int(operation_type)
opr=operation_type
operand1 = eval(input("Enter First Operand"))
#x = int(operand1)
x=operand1
operand2 = eval(input("Enter Second Operand"))
#y = int(operand2)
y=operand2

if(opr==1):
    print("The result is: ", x+y)
elif(opr==2):
    print("The result is: ",x-y)
elif(opr==3):
    print("The result is: ",x*y)
else:
    print("The result is: ",x/y)
