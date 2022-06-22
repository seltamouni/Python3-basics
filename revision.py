#game
class Game:

    def __init__(self):
        print('''welcome
        1- Multiplication table game
        2- count words''')

    choise = int(input("enter votre choise: "))
    if choise ==1:
        start = int(input("enter a number"))
        end = int(input("enter a number"))
        self.multiplication(start,end)

    def multiplication(self,start,end):
        for i in range(start,end+1):
            for j in rang(1,11):
                print(f"{j} x {i} = {i*j}")

g1 = Game()
