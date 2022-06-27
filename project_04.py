def division(number1,number2):
    i =1
    while i < number2:
        if number1%i ==0:
            print(i)
        i+=1

num1 = int(input("please enter the first number :"))
num2 = int(input("please enter the second number :"))
division(num1,num2)
