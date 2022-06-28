def listPairImp(list):
        list_pair =[]
        list_impair =[]
        for number in list:
            
            if int(number)%2 == 0:
                list_pair.append(int(number))
            else:
                list_impair.append(int(number))

        return(list_pair,list_impair)    
li = input("enter a list of numbers: ")
s = list(li.split(","))

result = listPairImp(s)
print(result)






























      
