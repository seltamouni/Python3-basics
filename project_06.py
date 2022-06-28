class Game:
    
    def __init__(self):
        while True:
            print('''welcome to our game:
            please choose one of following game:
            1-List pair impair
            2-Phrase
            3-Printing numbers
            4-division
            5-common division between two numbers
            
            ''')
            play = input("choose number to play one of games or x to exit :")
            if int(play) ==1:
                li = input("enter a list of numbers: ")
                s = list(li.split(","))

                result = self.listPairImp(s)
                print(f" list of pair number is {result[0]}")
                print(f" list of impair number is {result[1]}")
            if int(play) ==2:
                play1 = input("enter a phrase :")
                    
                i = self.wordsNumber(play1)
                print(i)
                        
            if int(play)==3:
                    numero = int(input("enter a number int to list all the precdent :"))

                    self.numbersInf(numero)
            if int(play)==4:
                x1 = int(input("Please enter the first number :"))
                x2 = int(input("Please enter the second number :"))
                self.division(x1,x2)
            if int(play)==5:
                div1 = int(input("enter the first number :"))
                div2 = int(input("enter the second number :"))
                self.divTwoNumbers(div1,div2)
            if play== 'x':
                break
            
    #---------game01----------            
    def listPairImp(self,list):
        list_pair =[]
        list_impair =[]
        for number in list:
            
            if int(number)%2 == 0:
                list_pair.append(int(number))
            else:
                list_impair.append(int(number))

        return(list_pair,list_impair) 
    #--------game02-----------    
    def wordsNumber(self,phrase):
            li = phrase.split(sep=" ")
            words = []
            for element in li:
                if element not in words:
                    words.append(element)
            return(len(words))
    #--------game03--------------
    def numbersInf(self,number):
        for x in range(0,number+1):
            print(x)

    #--------game04----------
    
    def division(self,number1,number2):
        i =1
        while i < number1:
            if number2%i ==0:
                print(i)
            i+=1  
    #--------game05----------
    def divTwoNumbers(self,number1,number2):
        for i in range(1,101):
            if number1%i ==0 and number2%i ==0:
                print(i)
    
     
    
s = Game()
