print ('''
       + Add
       - substraction
       * multiplication
       / division''')
num1= int (input ("ENTER THE NUMBER:"))
num2= int (input ("ENTER THE VALUE:"))
opr= input ("ENTER THE OPERATOR + - * /:")
if opr=="+":
    print (num1 + num2)
if opr=="-":
    print (num1 - num2)
if opr=="*":
    print (num1 * num2)   
if opr=="/":
    print (num1 / num2) 
if opr !="+" and opr !="-" and opr !="*" and opr != "/":
    print ("INVALID OPERATION")
