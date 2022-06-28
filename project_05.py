def divTwoNumbers(number1,number2):
    for i in range(1,101):
        if number1%i ==0 and number2%i ==0:
            print(i)


div1 = int(input("enter the first number :"))
div2 = int(input("enter the second number :"))
divTwoNumbes(div1,div2)
divTwoNumbers(1000,300)
