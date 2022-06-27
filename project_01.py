def listPairImp(list):
    list_pair =[]
    list_impair =[]
    for number in list:
        
        if number%2 == 0:
            list_pair.append(number)
        else:
            list_impair.append(number)

    print(list_pair)
    print(list_impair)

listPairImp([0,1,2,3,4,5,6,7,8,9,10])




























      
